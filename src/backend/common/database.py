from psycopg2 import pool


class Database:
    _connection_pool = None

    @classmethod
    def initialize(cls, database_url):
        cls._connection_pool = pool.SimpleConnectionPool(1, 10, dsn=database_url)

    @classmethod
    def get_connection(cls):
        if cls._connection_pool is None:
            raise Exception("Pool do banco de dados não inicializado.")
        return cls._connection_pool.getconn()

    @classmethod
    def return_connection(cls, connection):
        if cls._connection_pool is None:
            raise Exception("Pool do banco de dados não inicializado.")
        cls._connection_pool.putconn(connection)

    @classmethod
    def close_all_connections(cls):
        if cls._connection_pool is not None:
            cls._connection_pool.closeall()
            cls._connection_pool = None


class BaseModel:
    nome_tabela = None  # Deve ser definido nas subclasses

    def __init__(self, id=None):
        self.id = id

    @classmethod
    def find_by_id(cls, _id):
        conn = Database.get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute(f"SELECT * FROM {cls.nome_tabela} WHERE id = %s", (_id,))
            result = cursor.fetchone()
            if result:
                return cls.from_db_row(result)
            return None
        finally:
            cursor.close()
            Database.return_connection(conn)
            
    @classmethod
    def find_by_ids(cls, ids):
        conn = Database.get_connection()
        try:
            cursor = conn.cursor()
            formatted_ids = ', '.join(map(str, ids))
            cursor.execute(f"SELECT * FROM {cls.nome_tabela} WHERE id IN ({formatted_ids})")
            result = cursor.fetchall()
            return [cls.from_db_row(row) for row in result]
        finally:
            cursor.close()
            Database.return_connection(conn)

    @classmethod
    def find_all(cls):
        conn = Database.get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute(f"SELECT * FROM {cls.nome_tabela}")
            result = cursor.fetchall()
            return [cls.from_db_row(row) for row in result]
        finally:
            cursor.close()
            Database.return_connection(conn)

    @classmethod
    def insert(cls, **kwargs):
        conn = Database.get_connection()
        try:
            cursor = conn.cursor()
            columns = ', '.join(kwargs.keys())
            values = tuple(kwargs.values())
            placeholders = ', '.join(['%s'] * len(kwargs))
            cursor.execute(f"INSERT INTO {cls.nome_tabela} ({columns}) VALUES ({placeholders}) RETURNING id", values)
            conn.commit()
            return cursor.fetchone()[0]
        finally:
            cursor.close()
            Database.return_connection(conn)

    @classmethod
    def update(cls, id, **kwargs):
        conn = Database.get_connection()
        try:
            cursor = conn.cursor()
            set_clause = ', '.join([f"{key} = %s" for key in kwargs])
            values = list(kwargs.values()) + [id]
            cursor.execute(f"UPDATE {cls.nome_tabela} SET {set_clause} WHERE id = %s", values)
            conn.commit()
        finally:
            cursor.close()
            Database.return_connection(conn)

    @classmethod
    def delete(cls, id):
        conn = Database.get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute(f"DELETE FROM {cls.nome_tabela} WHERE id = %s", (id,))
            conn.commit()
        finally:
            cursor.close()
            Database.return_connection(conn)
    @classmethod
    def execute_query(cls, query, params=None, count_query=False):
        conn = Database.get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute(query, params or ())
            if query.strip().upper().startswith('SELECT'):
                results = cursor.fetchall()
                if count_query:
                    # Retorna o resultado diretamente para consultas de contagem
                    return results
                return [cls.from_db_row(row) for row in results] if results else None
            conn.commit()
        finally:
            cursor.close()
            Database.return_connection(conn)


    @classmethod
    def from_db_row(cls, row):
        """ Este método deve ser implementado nas subclasses para converter uma linha do BD em uma instância da classe """
        raise NotImplementedError("Este método deve ser implementado nas subclasses.")
    
    # método to_dict
    def to_dict(self):
        return {k: v for k, v in self.__dict__.items() if not k.startswith('_')}
