import 'package:flutter/material.dart';
import 'package:coffeebreak/models/theme_model.dart';
import 'package:coffeebreak/widgets/avatar/avatar_with_name.dart';
import 'package:coffeebreak/widgets/buttons/button.dart';
import 'package:provider/provider.dart';
import 'package:coffeebreak/custom/text_styles.dart';
import 'package:coffeebreak/widgets/buttons/back.dart';
import 'package:coffeebreak/models/ceo.dart';

/// Este widget exibe o estado da solicitação de sinergia de um projeto.
///
/// Comportamento:
/// - Exibe uma mensagem de parabéns junto com o nome do projeto aprovado.
/// - Oferece um botão "Ok" para confirmar a mensagem.
class SynergyStatus extends StatelessWidget {
  const SynergyStatus({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    final theme = Provider.of<TemaModel>(context).theme;

    return Semantics(
      label: 'Estado da solicitação de sinergia',
      child: Center(
        child: SizedBox(
          child: Container(
            decoration: BoxDecoration(
              borderRadius: BorderRadius.circular(6.0),
              color: theme.secondaryBackground,
            ),
            child: Padding(
              padding: EdgeInsets.all(16.0),
              child: Column(
                mainAxisAlignment: MainAxisAlignment.center,
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text(
                    'Parabéns! Seu projeto foi aprovado e adicionado a sua página de projetos: ',
                    style: CoffebreakTextStyle.project.copyWith(
                      color: theme.primaryText,
                    ),
                  ),
                  SizedBox(height: 20),
                  SizedBox(height: 20),
                  Text(
                    'Ética no ambiente empresarial.',
                    style: CoffebreakTextStyle.macrotheme.copyWith(
                      color: theme.primaryText,
                    ),
                  ),
                  SizedBox(height: 20),
                  CustomButton(
                    alt: 'Botão de confirmar',
                    text: "Ok",
                    textColor: Colors.white,
                    gradient: theme.secondaryButton,
                    height: 42,
                    onPressed: () => Navigator.of(context).pushNamed(
                        "/project-details",
                        arguments: {'projectId': '123'}),
                  ),
                ],
              ),
            ),
          ),
        ),
      ),
    );
  }
}
