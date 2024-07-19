import 'package:coffeebreak/models/ceo.dart';
import 'package:coffeebreak/models/theme_model.dart';
import 'package:coffeebreak/custom/text_styles.dart';
import 'package:coffeebreak/widgets/category.dart';
import 'package:coffeebreak/widgets/avatar/avatar_with_name.dart';
import 'package:coffeebreak/widgets/buttons/button.dart';
import 'package:coffeebreak/widgets/interations.dart';
import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

/// Este widget representa um projeto com informações adicionais sobre interesse e tipo de sinergia.
/// Dependendo do estado de `interations`, o widget pode exibir todos os CEOs ou apenas um.
///
/// Parâmetros:
/// - `id` (int): O identificador do projeto.
/// - `macrotheme` (String): O macrotema do projeto.
/// - `interest` (String): O interesse no projeto.
/// - `interestTwo` (String): O tipo de sinergia.
/// - `subtheme` (String): O subtema do projeto.
/// - `interations` (bool): Define se o modo de interações está ativo (padrão: false).
/// - `ceos` (List<Ceo>): A lista de CEOs associados ao projeto.
///
/// Comportamento:
/// - Se `interations` for true, exibe todos os CEOs e os botões de interação.
/// - Se `interations` for false, exibe apenas um CEO e não exibe o botão "Ver mais".
class ProjectSinergy extends StatelessWidget {
  final int id;
  final String macrotheme;
  final String subtheme;
  final bool interations;
  final String interest;
  final String interestTwo;
  final List<Ceo> ceos;

  const ProjectSinergy({
    Key? key,
    required this.id,
    required this.macrotheme,
    required this.interest,
    required this.interestTwo,
    required this.subtheme,
    this.interations = false,
    required this.ceos,
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    final theme = Provider.of<TemaModel>(context).theme;

    int itemCount = ceos.length > 2
        ? interations
            ? ceos.length
            : 1
        : ceos.length;

    return Semantics(
      label: 'Projeto',
      child: Container(
        width: double.infinity,
        decoration: BoxDecoration(
          color: theme.secondaryBackground,
          borderRadius: BorderRadius.circular(6),
        ),
        child: Padding(
          padding: const EdgeInsets.only(
            top: 26,
            bottom: 26,
            left: 27,
            right: 27,
          ),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Row(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Flexible(
                    fit: FlexFit.loose,
                    child: ListView.separated(
                      shrinkWrap: true,
                      itemCount: itemCount,
                      itemBuilder: (context, index) {
                        return AvatarWithName(ceo: ceos[index]);
                      },
                      separatorBuilder: (context, index) =>
                          const SizedBox(height: 7),
                    ),
                  ),
                  Category(macrotheme: macrotheme, subtheme: subtheme)
                ],
              ),
              if (ceos.length > 2 && itemCount == 1) ...[
                SizedBox(height: 7),
                Text(
                  'e outras ${ceos.length - 1} pessoas',
                  style: CoffebreakTextStyle.shortenedName
                      .copyWith(color: theme.primaryText),
                ),
              ],
              SizedBox(height: 25),
              SizedBox(height: 20),
              RichText(
                text: TextSpan(
                  children: [
                    TextSpan(
                      text: 'Interesse no projeto:\n',
                      style: CoffebreakTextStyle.auxiliary.copyWith(
                        color: theme.primaryText,
                      ),
                    ),
                    TextSpan(
                      text: interest,
                      style: CoffebreakTextStyle.activeAuxiliary.copyWith(
                        color: theme.primaryText,
                      ),
                    ),
                  ],
                ),
              ),
              SizedBox(height: 10),
              RichText(
                text: TextSpan(
                  children: [
                    TextSpan(
                      text: 'Tipo de Sinergia:\n',
                      style: CoffebreakTextStyle.auxiliary.copyWith(
                        color: theme.primaryText,
                      ),
                    ),
                    WidgetSpan(
                      child: Icon(Icons.merge_type,
                          color: theme.primaryText, size: 16),
                    ),
                    TextSpan(
                      text: ' $interestTwo',
                      style: CoffebreakTextStyle.activeAuxiliary.copyWith(
                        color: theme.primaryText,
                      ),
                    ),
                  ],
                ),
              ),
              SizedBox(height: 20),
              if (interations) ...[
                Container(
                  alignment: Alignment.bottomRight,
                  child: Interations(),
                ),
              ],
            ],
          ),
        ),
      ),
    );
  }
}
