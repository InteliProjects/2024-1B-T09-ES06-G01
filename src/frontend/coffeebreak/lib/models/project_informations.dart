/// Esta classe armazena informações sobre um projeto em sua criação.
///
/// Atributos:
/// - `userId` (int): O ID do usuário criador do projeto.
/// - `macrotheme` (String?): O macrotema do projeto.
/// - `subtheme` (String?): O subtema do projeto.
/// - `title` (String?): O título do projeto.
/// - `description` (String?): A descrição do projeto.
class ProjectInformations {
  int userId;
  String? macrotheme;
  String? subtheme;
  String? title;
  String? description;

  ProjectInformations({required this.userId, this.macrotheme, this.subtheme, this.title, this.description});
}
