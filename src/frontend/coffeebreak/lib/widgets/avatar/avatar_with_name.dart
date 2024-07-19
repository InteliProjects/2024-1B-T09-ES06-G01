import 'package:coffeebreak/models/ceo.dart';
import 'package:coffeebreak/models/theme_model.dart';
import 'package:coffeebreak/custom/text_styles.dart';
import 'package:coffeebreak/screens/profile/index.dart';
import 'package:coffeebreak/screens/projects.dart';
import 'package:coffeebreak/widgets/avatar/avatar.dart';
import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

/// Este widget exibe a imagem do avatar do usuário juntamente com o nome e a empresa.
///
/// Parâmetros:
/// - `ceo` (Ceo): O objeto Ceo contendo as informações do usuário.
///
/// Estrutura:
/// - Uma linha contendo o avatar do usuário e um espaço reservado para o nome e a empresa.
///
/// Comportamento:
/// - Exibe a imagem do avatar do usuário, nome e empresa.
class AvatarWithName extends StatelessWidget {
  final Ceo ceo;

  const AvatarWithName({
    super.key,
    required this.ceo,
  });

  @override
  Widget build(BuildContext context) {
    final theme = Provider.of<TemaModel>(context).theme;

    return Semantics(
      label: 'Imagem do avatar do usuário com o nome e a empresa',
      child: GestureDetector(
        onTap: () => Navigator.push(
          context,
          MaterialPageRoute(
            builder: (context) => Profile(id: ceo.id),
          ),
        ),
        child: Padding(
          padding: const EdgeInsets.all(4),
          child: Container(
            child: Row(
              children: [
                Avatar(image: ceo.image),
                SizedBox(width: 11),
                Expanded(
                  child: Column(
                    mainAxisAlignment: MainAxisAlignment.center,
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Text(
                        ceo.name,
                        style: CoffebreakTextStyle.shortenedName.copyWith(
                          color: theme.primaryText,
                        ),
                      ),
                      Text(
                        ceo.enterprise,
                        style: CoffebreakTextStyle.shortenedCompany.copyWith(
                          color: theme.primaryText,
                        ),
                      ),
                    ],
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
