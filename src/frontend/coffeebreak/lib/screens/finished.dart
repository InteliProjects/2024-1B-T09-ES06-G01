import 'package:coffeebreak/custom/text_styles.dart';
import 'package:coffeebreak/widgets/buttons/button.dart';
import 'package:coffeebreak/widgets/subtheme.dart';
import 'package:flutter/material.dart';
import 'package:coffeebreak/models/theme_model.dart';
import 'package:coffeebreak/layouts/layout.dart';
import 'package:provider/provider.dart';

enum FinishedType {
  createProject,
  sinergy,
}

class Finished extends StatelessWidget {
  final FinishedType type;
  const Finished({Key? key, required this.type});

  @override
  Widget build(BuildContext context) {
    final theme = Provider.of<TemaModel>(context).theme;

    String image = '';
    String text = '';
    String buttonPath = '';

    switch (type) {
      case FinishedType.createProject:
        image = 'created_project.png';
        text = 'Seu projeto já foi submetido. Assim que houver uma atualização você será notificado ;)';
        buttonPath = '/profile';
        break;
      case FinishedType.sinergy:
        image = 'sinergy.jpg';
        text = 'Sua solicitação de sinergia já foi enviada. Logo logo essa pessoa entrará em contato com você ;)';
        buttonPath = '/home';
        break;
    }

    return Layout(
      child: Column(
        children: [
          Container(
            width: double.infinity,
            child: AspectRatio(
              aspectRatio: 1444 / 1628,
              child: FittedBox(
                fit: BoxFit.contain,
                child: Image.asset('assets/img/${image}'),
              ),
            ),
          ),
          SizedBox(height: 14),
          Align(
            alignment: Alignment.centerLeft,
            child: Text(
              'Pronto!',
              style: CoffebreakTextStyle.title.copyWith(
                color: theme.primaryText,
              ),
              textAlign: TextAlign
                  .left, // Garante que o texto está alinhado à esquerda
            ),
          ),
          Align(
            alignment: Alignment.centerLeft,
            child: Text(
              text,
              style: CoffebreakTextStyle.project.copyWith(
                color: theme.primaryText,
              ),
              textAlign: TextAlign
                  .left, // Garante que o texto está alinhado à esquerda
            ),
          ),
          SizedBox(height: 14),
          CustomButton(
            alt: 'Botão de confirmar',
            text: "Ok",
            textColor: Colors.white,
            gradient: theme.secondaryButton,
            height: 55,
            onPressed: () {
              Navigator.of(context).pushNamed(buttonPath);
            },
          ),
        ],
      ),
    );
  }
}
