import 'package:flutter/material.dart';
import 'package:coffeebreak/models/theme_model.dart';
import 'package:coffeebreak/widgets/avatar/avatar_with_name.dart';
import 'package:coffeebreak/widgets/buttons/button.dart';
import 'package:provider/provider.dart';
import 'package:coffeebreak/custom/text_styles.dart';
import 'package:coffeebreak/widgets/buttons/back.dart';
import 'package:coffeebreak/models/ceo.dart';

/// Este widget exibe a solicitação de sinergia para um projeto.
///
/// Comportamento:
/// - Exibe uma mensagem perguntando se deseja realizar uma sinergia.
/// - Mostra o CEO do projeto e o macrotema relacionado.
/// - Oferece um botão "Ver Mais" para visualizar detalhes adicionais.
///
/// Estrutura:
/// - Um container com bordas arredondadas contendo a mensagem, avatar, macrotema e o botão "Ver Mais".
class Synergy extends StatelessWidget {
  const Synergy({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    final theme = Provider.of<TemaModel>(context).theme;

    return Semantics(
      label: 'Solicitação de sinergia',
      child: Center(
        child: SizedBox(
          child: Container(
            decoration: BoxDecoration(
              borderRadius: BorderRadius.circular(10),
              color: theme.secondaryBackground,
            ),
            child: Padding(
              padding: EdgeInsets.all(16.0),
              child: Column(
                mainAxisAlignment: MainAxisAlignment.center,
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text(
                    'Deseja realizar uma sinergia: ',
                    style: CoffebreakTextStyle.project.copyWith(
                      color: theme.primaryText,
                    ),
                  ),
                  SizedBox(height: 20),
                  AvatarWithName(
                    ceo: Ceo(
                      id: 70,
                      name: 'João Dono',
                      enterprise: 'Google',
                      image:
                          'https://api.dicebear.com/8.x/micah/svg?seed=Tigger',
                    ),
                  ),
                  SizedBox(height: 20),
                  Text(
                    'Redução de emissão de carbono',
                    style: CoffebreakTextStyle.macrotheme.copyWith(
                      color: theme.primaryText,
                    ),
                  ),
                  SizedBox(height: 20),
                  CustomButton(
                    alt: 'Botão de "ver mais"',
                    text: "Ver Mais",
                    textColor: Colors.white,
                    gradient: theme.secondaryButton,
                    height: 42,
                    onPressed: () => Navigator.of(context).pushNamed(
                        "/request-sinergy",
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
