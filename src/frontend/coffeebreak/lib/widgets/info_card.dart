import 'package:coffeebreak/models/theme_model.dart';
import 'package:coffeebreak/custom/text_styles.dart';
import 'package:coffeebreak/widgets/info_card.dart';
import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

/// Este widget representa um cartão de informações com um título e uma descrição.
/// Ele é construído utilizando um `Container` que contém um `Column` para dispor o título e a descrição verticalmente.
///
/// Parâmetros:
/// - `title` (String): O título do cartão de informações.
/// - `description` (String): A descrição detalhada do cartão.
class InfoCard extends StatelessWidget {
  final String description;
  final String title;

  const InfoCard({super.key, required this.title, required this.description});

  @override
  Widget build(BuildContext context) {
    final theme = Provider.of<TemaModel>(context).theme;

    return Semantics(
      label: 'Texto',
      child: Container(
        width: double.infinity,
        padding: EdgeInsets.symmetric(vertical: 20, horizontal: 26),
        decoration: BoxDecoration(
          color: theme.description,
          borderRadius: BorderRadius.circular(10),
        ),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: <Widget>[
            Text(title,
                style: CoffebreakTextStyle.title
                    .copyWith(color: theme.primaryText)),
            SizedBox(height: 8),
            Text(
              description,
              style: CoffebreakTextStyle.auxiliary
                  .copyWith(color: theme.primaryText),
            ),
          ],
        ),
      ),
    );
  }
}
