import 'package:coffeebreak/models/theme_model.dart';
import 'package:coffeebreak/custom/text_styles.dart';
import 'package:coffeebreak/screens/profile/avatar.dart';
import 'package:coffeebreak/utils/utils.dart';
import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:url_launcher/url_launcher.dart';
import 'package:flutter_svg/flutter_svg.dart';

/// Este widget representa um cartão de perfil do usuário, que inclui um avatar editável.
/// Ele permite que o usuário edite o avatar se a propriedade `canEdit` for verdadeira.
///
/// Parâmetros:
/// - `avatarLink` (String): O link para o avatar do usuário.
/// - `canEdit` (bool): Indica se o usuário pode editar o avatar.
///
/// Propriedades:
/// - `avatarLink` (String): O link do avatar do usuário.
/// - `canEdit` (bool): Indica se o avatar pode ser editado.
///
/// Comportamento:
/// - Se `canEdit` for verdadeiro, um ícone de lápis é exibido no canto superior direito.
/// - Ao tocar no ícone de lápis, o usuário é direcionado para a página de edição do avatar.
class ProfileCardEdit extends StatelessWidget {
  late String avatarLink = '';
  final bool canEdit;

  ProfileCardEdit({
    super.key,
    required this.avatarLink,
    required this.canEdit,
  });

  @override
  Widget build(BuildContext context) {
    final theme = Provider.of<TemaModel>(context).theme;

    return Semantics(
      label: 'Componente do perfil do usuário editável',
      child: Stack(
        children: [
          Container(
            width: double.infinity,
            height: 343,
            decoration: BoxDecoration(
              color: Colors.black,
              borderRadius: BorderRadius.circular(10),
            ),
            child: Center(
              child: LayoutBuilder(
                builder: (context, constraints) {
                  return SvgPicture.network(
                    avatarLink,
                    width: constraints.maxWidth,
                    height: constraints.maxHeight,
                    fit: BoxFit.cover,
                  );
                },
              ),
            ),
          ),
          if (canEdit)
            Padding(
              padding: const EdgeInsets.only(top: 18, right: 18),
              child: Align(
                alignment: Alignment.topRight,
                child: GestureDetector(
                  onTap: () => Navigator.push(
                    context,
                    MaterialPageRoute(
                      builder: (context) => EditAvatar(avatarLink: avatarLink),
                    ),
                  ),
                  child: SvgPicture.asset(
                    'assets/icons/pencil.svg',
                    height: 18,
                    width: 18,
                    colorFilter: const ColorFilter.mode(
                      Colors.white,
                      BlendMode.srcIn,
                    ),
                  ),
                ),
              ),
            ),
        ],
      ),
    );
  }
}
