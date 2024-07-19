import 'package:coffeebreak/models/ceo.dart';
import 'package:coffeebreak/models/theme_model.dart';
import 'package:coffeebreak/custom/text_styles.dart';
import 'package:coffeebreak/widgets/category.dart';
import 'package:coffeebreak/widgets/avatar/avatar_with_name.dart';
import 'package:coffeebreak/widgets/buttons/button.dart';
import 'package:coffeebreak/widgets/interations.dart';
import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:coffeebreak/screens/project_details.dart';

/// Este widget representa um projeto, exibindo informações sobre os CEOs associados, a categoria do projeto, e permitindo interações.
/// Dependendo do estado de `interations`, o widget pode exibir todos os CEOs ou apenas um.
///
/// Parâmetros:
/// - `id` (int): O identificador do projeto.
/// - `macrotheme` (String): O macrotema do projeto.
/// - `subtheme` (String): O subtema do projeto.
/// - `interations` (bool): Define se o modo de interações está ativo (padrão: false).
/// - `title` (String): O título do projeto.
/// - `ceos` (List<Ceo>): A lista de CEOs associados ao projeto.
///
/// Comportamento:
/// - Se `interations` for true, exibe todos os CEOs e os botões de interação.
/// - Se `interations` for false, exibe apenas um CEO e um botão "Ver mais".
/// - O botão "Ver mais" navega para a página de detalhes do projeto.
class Project extends StatelessWidget {
  final int id;
  final int ceoId;
  final String macrotheme;
  final String subtheme;
  final bool interations;
  final String title;
  final List<Ceo> ceos;
  final String description;

  const Project({
    super.key,
    required this.id,
    required this.ceoId,
    required this.macrotheme,
    required this.subtheme,
    this.interations = false,
    required this.title,
    required this.ceos,
    required this.description,
  });

  @override
  Widget build(BuildContext context) {
    final theme = Provider.of<TemaModel>(context).theme;
    int displayCount = interations
        ? ceos.length
        : 1; // Exibe todos se interations é true, caso contrário, exibe apenas um.

    return Semantics(
      label: 'Projeto',
      child: Container(
        width: double.infinity,
        decoration: BoxDecoration(
          color: theme.secondaryBackground,
          borderRadius: BorderRadius.circular(6),
        ),
        child: Padding(
          padding: const EdgeInsets.all(26),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Row(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Expanded(
                    child: Column(
                      children: ceos
                          .sublist(0, displayCount)
                          .map((ceo) => AvatarWithName(ceo: ceo))
                          .toList(),
                    ),
                  ),
                  Category(macrotheme: macrotheme, subtheme: subtheme),
                ],
              ),
              if (ceos.length > 2 && !interations) ...[
                SizedBox(height: 7),
                Text(
                  'e outras ${ceos.length - 1} pessoas',
                  style: CoffebreakTextStyle.shortenedName
                      .copyWith(color: theme.primaryText),
                ),
              ],
              SizedBox(height: 25),
              Text(
                title,
                maxLines: 3,
                overflow: TextOverflow.ellipsis,
                style: CoffebreakTextStyle.project
                    .copyWith(color: theme.primaryText),
              ),
              SizedBox(height: 20),
              Align(
                alignment: Alignment.centerRight,
                child: interations ? Interations() : Container(),
              ),
              SizedBox(height: 20),
              if (!interations)
                CustomButton(
                  alt: 'Botão de "ver mais"',
                  text: "Ver mais",
                  gradient: theme.getGradienteCategoria(macrotheme),
                  textColor: Colors.white,
                  onPressed: () {
                    Navigator.push(
                      context,
                      MaterialPageRoute(
                        builder: (context) => ProjectDetails(title: title, description: description, ceoId: ceoId, subtheme: subtheme, macrotheme: macrotheme, ceos: ceos, id: id,),
                      ),
                    );
                  },
                ),
            ],
          ),
        ),
      ),
    );
  }
}
