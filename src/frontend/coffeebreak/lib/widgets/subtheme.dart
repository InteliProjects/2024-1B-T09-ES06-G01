import 'package:coffeebreak/models/project_informations.dart';
import 'package:coffeebreak/models/theme_model.dart';
import 'package:coffeebreak/custom/text_styles.dart';
import 'package:coffeebreak/custom/themes.dart';
import 'package:coffeebreak/screens/create_project/name.dart';
import 'package:coffeebreak/utils/utils.dart';
import 'package:coffeebreak/widgets/buttons/button.dart';
import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:font_awesome_flutter/font_awesome_flutter.dart';
import 'package:flutter_svg/flutter_svg.dart';

/// Este widget representa um subtema de um projeto e é utilizado para selecionar um subtema durante a criação de um novo projeto.
///
/// Parâmetros:
/// - `subtheme` (String): O nome do subtema.
/// - `projectInformations` (ProjectInformations): As informações do projeto em criação.
///
/// Comportamento:
/// - Quando clicado, atualiza as informações do projeto com o subtema selecionado e navega para a tela de inserção do nome do projeto.
class Subtheme extends StatelessWidget {
  final String subtheme;
  final ProjectInformations projectInformations;

  const Subtheme({
    Key? key,
    required this.subtheme,
    required this.projectInformations,
  });

  @override
  Widget build(BuildContext context) {
    final theme = Provider.of<TemaModel>(context).theme;

    return Semantics(
      label: 'Subtema',
      child: CustomButton(
        alt: 'Botão do subtema "${subtheme}"',
        text: subtheme,
        textColor: Colors.white,
        gradient: theme.secondaryButton,
        onPressed: () {
          projectInformations?.subtheme = subtheme;
          Navigator.push(
            context,
            MaterialPageRoute(
              builder: (context) =>
                  CreateProjectName(projectInformations: projectInformations),
            ),
          );
        },
      ),
    );
  }
}
