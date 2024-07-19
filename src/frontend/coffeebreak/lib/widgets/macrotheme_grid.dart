import 'package:coffeebreak/models/project_informations.dart';
import 'package:coffeebreak/models/theme_model.dart';
import 'package:coffeebreak/custom/themes.dart';
import 'package:coffeebreak/custom/text_styles.dart';
import 'package:coffeebreak/widgets/macrotheme.dart';
import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

/// Este widget representa uma grade de macrotemas dispostos em linhas e colunas.
/// Cada macrotema é representado por um `Macrotheme` widget, que pode ser clicado para navegação.
///
/// Parâmetros:
/// - `navigateTo` (String): A rota para a qual cada `Macrotheme` deve navegar quando clicado.
/// - `type` (String): Define o comportamento da navegação (`home` ou `create_project`).
/// - `projectInformations` (ProjectInformations?, opcional): Informações sobre o projeto a serem passadas durante a navegação.
///
/// Este widget facilita a exibição e navegação por diferentes macrotemas em uma interface organizada.
class MacrothemeGrid extends StatelessWidget {
  final String navigateTo;
  final String type;
  final ProjectInformations? projectInformations;

  const MacrothemeGrid({super.key, required this.navigateTo, required this.type, this.projectInformations});

  @override
  Widget build(BuildContext context) {
    return Column(
      children: [
        Row(children: [Macrotheme(macrotheme: 'bem-estar', text: 'Bem-Estar, Saúde e Felicidade', navigateTo: navigateTo, type: type, projectInformations: projectInformations), SizedBox(width: 16), Macrotheme(macrotheme: 'diversidade', text: 'Diversidade e Inclusão', navigateTo: navigateTo, type: type, projectInformations: projectInformations)],),
        SizedBox(height: 16),
        Row(children: [Macrotheme(macrotheme: 'produtividade', text: 'Produtividade e Competitividade', navigateTo: navigateTo, type: type, projectInformations: projectInformations), SizedBox(width: 16), Macrotheme(macrotheme: 'integridade', text: 'Integridade e Práticas Éticas', navigateTo: navigateTo, type: type, projectInformations: projectInformations)],),
        SizedBox(height: 16),
        Row(children: [Macrotheme(macrotheme: 'redução', text: 'Redução do Impacto Ambiental', navigateTo: navigateTo, type: type, projectInformations: projectInformations), SizedBox(width: 16), Macrotheme(macrotheme: 'conservação', text: 'Conservação do Planeta', navigateTo: navigateTo, type: type, projectInformations: projectInformations)],),
      ],
    );
  }
}
