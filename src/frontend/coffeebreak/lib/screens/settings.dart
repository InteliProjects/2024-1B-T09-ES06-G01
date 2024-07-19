import 'package:coffeebreak/layouts/layout.dart';
import 'package:coffeebreak/models/ceo.dart';
import 'package:coffeebreak/models/theme_model.dart';
import 'package:coffeebreak/custom/text_styles.dart';
import 'package:coffeebreak/widgets/buttons/button.dart';
import 'package:coffeebreak/widgets/macrotheme_grid.dart';
import 'package:coffeebreak/widgets/project.dart';
import 'package:coffeebreak/widgets/buttons/switch.dart';
import 'package:flutter/material.dart';
import 'package:font_awesome_flutter/font_awesome_flutter.dart';
import 'package:provider/provider.dart';

class Settings extends StatelessWidget {
  const Settings({super.key});

  @override
  Widget build(BuildContext context) {
    final theme = Provider.of<TemaModel>(context).theme;

    return Layout(
      page: 'Configurações',
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          TemaSwitchButton(),
          SizedBox(height: 12),
          CustomButton(
            alt: 'Botão de ajdua',
            text: "Preciso de ajuda",
            textColor: theme.input,
            icon: Icons.support_agent,
            backgroundColor: theme.primaryButton,
            onPressed: () => Navigator.of(context).pushNamed("/help"),
          ),
          SizedBox(height: 12),
          GestureDetector(
            onTap: () => Navigator.of(context).pushNamed("/login"),
            child: Text(
              'Sair',
              style: CoffebreakTextStyle.macrotheme.copyWith(
                color: Color(0xFFC84666),
              ),
            ),
          ),
        ],
      ),
    );
  }
}
