import 'package:coffeebreak/models/theme_model.dart';
import 'package:coffeebreak/custom/text_styles.dart';
import 'package:coffeebreak/widgets/icons.dart';
import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

/// Este widget representa uma categoria com um ícone associado ao macrotema e um texto do subtema.
/// Ele é construído utilizando um `Row` que contém um ícone e um texto, estilizados conforme o tema atual.
///
/// Parâmetros:
/// - `macrotheme` (String): O macrotema que define o ícone exibido.
/// - `subtheme` (String): O texto que descreve o subtema.
class Category extends StatelessWidget {
  final String macrotheme;
  final String subtheme;

  const Category({
    super.key,
    required this.macrotheme,
    required this.subtheme,
  });

  @override
  Widget build(BuildContext context) {
    final theme = Provider.of<TemaModel>(context).theme;
    final ProjectIcon icon = ProjectIcon(macrotheme: macrotheme);

    return Semantics(
      label: 'Categoria',
      child: Row(
        children: [
          icon,
          SizedBox(width: 8),
          Text(subtheme,
              style: CoffebreakTextStyle.subtheme.copyWith(
                color: theme.primaryText,
              )),
        ],
      ),
    );
  }
}
