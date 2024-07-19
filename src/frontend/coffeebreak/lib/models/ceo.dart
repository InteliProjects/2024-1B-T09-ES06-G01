/// Esta classe armazena informações sobre um CEO (Chief Executive Officer).
///
/// Atributos:
/// - `name` (String): O nome do CEO.
/// - `enterprise` (String): A empresa do CEO.
/// - `image` (String): O link para a imagem do avatar do CEO.
class Ceo {
  int id;
  String name;
  String enterprise;
  String image;

  Ceo(
      {required this.id,
      required this.name,
      required this.enterprise,
      required this.image});

  factory Ceo.fromJson(Map<String, dynamic> json) {
    return Ceo(
      id: json['id'],
      name: json['nome'],
      enterprise: json['empresa_nome'],
      image: json['foto'],
    );
  }
}
