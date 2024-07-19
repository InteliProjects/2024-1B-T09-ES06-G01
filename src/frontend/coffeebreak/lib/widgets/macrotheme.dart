import 'package:coffeebreak/models/project_informations.dart';
import 'package:coffeebreak/models/theme_model.dart';
import 'package:coffeebreak/custom/themes.dart';
import 'package:coffeebreak/custom/text_styles.dart';
import 'package:coffeebreak/screens/create_project/subtheme.dart';
import 'package:coffeebreak/widgets/icons.dart';
import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

/// Este widget representa um macrotema que pode ser clicado para navegação. Ele exibe um ícone e um texto descritivo.
/// Dependendo do tipo especificado, a navegação pode direcionar para diferentes telas.
///
/// Parâmetros:
/// - `macrotheme` (String): O nome do macrotema que define a cor e o ícone exibido.
/// - `text` (String): O texto descritivo exibido no cartão do macrotema.
/// - `navigateTo` (String): A rota para a qual o widget deve navegar quando clicado.
/// - `type` (String): Define o comportamento da navegação (`home` ou `create_project`).
/// - `projectInformations` (ProjectInformations?, opcional): Informações sobre o projeto a serem passadas durante a navegação.
///
/// Comportamento:
/// - Quando o tipo é `home`, a navegação é feita para a rota especificada passando os argumentos do macrotema e texto.
/// - Quando o tipo é `create_project`, atualiza as informações do projeto e navega para a tela de criação de subtema.
class Macrotheme extends StatelessWidget {
  final String macrotheme;
  final String text;
  final String navigateTo;
  final String type;
  ProjectInformations? projectInformations;

  Macrotheme(
      {super.key,
      required this.macrotheme,
      required this.text,
      required this.navigateTo,
      required this.type,
      this.projectInformations});

  void _navigate(BuildContext context) {
    if (type == 'home') {
      Navigator.of(context).pushNamed(
        navigateTo,
        arguments: {'macrotheme': macrotheme, 'text': text},
      );
    } else if (type == 'create_project') {
      projectInformations?.macrotheme = macrotheme;
      Navigator.push(
        context,
        MaterialPageRoute(
          builder: (context) =>
              CreateProjectSubtheme(projectInformations: projectInformations!),
        ),
      );
    }
  }

  @override
  Widget build(BuildContext context) {
    final theme = Provider.of<TemaModel>(context).theme;

    return Expanded(
      child: Semantics(
        label: 'Macrotema',
        child: GestureDetector(
          onTap: () => _navigate(context),
          child: Container(
            height: 74,
            decoration: BoxDecoration(
              color: theme.getMacrothemeColor(macrotheme),
              borderRadius: BorderRadius.circular(6),
            ),
            child: Stack(
              children: [
                Padding(
                  padding: EdgeInsets.only(right: 10),
                  child: Align(
                    alignment: Alignment.bottomRight,
                    child: LayoutBuilder(
                      builder: (context, constraints) {
                        return ProjectIcon(
                          macrotheme: macrotheme,
                          height: 74,
                          overlay: true,
                        );
                      },
                    ),
                  ),
                ),
                Padding(
                  padding: EdgeInsets.only(bottom: 5, left: 10, right: 15),
                  child: Align(
                    alignment: Alignment.bottomLeft,
                    child: Text(
                      text,
                      style: CoffebreakTextStyle.macrotheme.copyWith(
                        color: Colors.white,
                      ),
                    ),
                  ),
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }
}
