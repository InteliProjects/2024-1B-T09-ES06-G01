import 'package:coffeebreak/models/theme_model.dart';
import 'package:coffeebreak/custom/text_styles.dart';
import 'package:coffeebreak/screens/profile/edit.dart';
import 'package:coffeebreak/utils/utils.dart';
import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:url_launcher/url_launcher.dart';
import 'package:flutter_svg/flutter_svg.dart';

/// Este widget representa um cartão de perfil do usuário, exibindo informações como nome, empresa, quantidade de projetos,
/// e-mails e links do LinkedIn, bem como um avatar.
///
/// Parâmetros:
/// - `name` (String): O nome do usuário.
/// - `isOwn` (bool): O card pertence ou não ao usuário.
/// - `enterprise` (String): A empresa em que o usuário trabalha.
/// - `projectsQuantity` (int): A quantidade de projetos associados ao usuário.
/// - `email` (String): O endereço de e-mail do usuário.
/// - `linkedin` (String): O link do perfil do LinkedIn do usuário.
/// - `avatarLink` (String): O link para o avatar do usuário.
/// - `role` (String): O cargo do usuário.
///
/// Estrutura:
/// - Um contêiner que contém um avatar e informações do usuário.
///
/// Comportamento:
/// - Um ícone de lápis é exibido no canto superior direito para edição do perfil.
/// - Ao tocar no ícone de lápis, o usuário é direcionado para a página de edição do perfil.
/// - Ícones de e-mail e LinkedIn são exibidos abaixo das informações do usuário e são clicáveis.
class ProfileCard extends StatelessWidget {
  final bool isOwn;
  final String name;
  final String enterprise;
  final int projectsQuantity;
  final String email;
  final String linkedin;
  final String avatarLink;
  final String role;

  const ProfileCard({
    super.key,
    required this.isOwn,
    required this.name,
    required this.enterprise,
    required this.projectsQuantity,
    required this.email,
    required this.linkedin,
    required this.avatarLink,
    required this.role,
  });

  // Function that redirects to email
  void sendEmail(String email) async {
    final emailAddress = email;

    final url = Uri(
      scheme: 'mailto',
      path: emailAddress,
    );

    if (await canLaunchUrl(url)) {
      await launchUrl(url);
    }
  }

  @override
  Widget build(BuildContext context) {
    final theme = Provider.of<TemaModel>(context).theme;

    return Semantics(
      label: 'Componente do perfil do usuário',
      child: Stack(
        children: [
          Container(
              width: double.infinity,
              height: 343,
              decoration: BoxDecoration(
                color: Colors.black,
                borderRadius: BorderRadius.circular(10),
              ),
              child: Stack(children: [
                Center(
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
                Positioned(
                  bottom: 0,
                  left: 0,
                  right: 0,
                  child: Container(
                    height: 170,
                    decoration: BoxDecoration(
                      borderRadius: BorderRadius.circular(10),
                      gradient: LinearGradient(
                        begin: Alignment.topCenter,
                        end: Alignment.bottomCenter,
                        colors: [
                          Colors.transparent,
                          Colors.black.withOpacity(0.8),
                        ],
                      ),
                    ),
                  ),
                ),
              ])),
          SizedBox(
            width: double.infinity,
            height: 343,
            child: Padding(
              padding: const EdgeInsets.only(
                  top: 23, bottom: 23, left: 26, right: 26),
              child: Align(
                alignment: Alignment.bottomLeft,
                child: Column(
                  mainAxisSize: MainAxisSize.min,
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Text(
                      name,
                      style: CoffebreakTextStyle.name.copyWith(
                        color: Colors.white,
                      ),
                    ),
                    Row(
                      children: [
                        Column(
                            crossAxisAlignment: CrossAxisAlignment.start,
                            children: [
                              Text(
                                '$role | $enterprise',
                                style: CoffebreakTextStyle.auxiliary.copyWith(
                                  color: Colors.white,
                                ),
                              ),
                              Text(
                                '$projectsQuantity ${projectsQuantity > 1 ? 'projetos' : 'projeto'}',
                                style: CoffebreakTextStyle.auxiliary.copyWith(
                                  color: Colors.white,
                                ),
                              ),
                            ]),
                        const Spacer(),
                        Row(
                          mainAxisSize: MainAxisSize.min,
                          crossAxisAlignment: CrossAxisAlignment.end,
                          children: [
                            GestureDetector(
                              onTap: () => sendEmail(email),
                              child: const ImageIcon(
                                AssetImage('assets/icons/email.png'),
                                size: 26,
                                color: Colors.white,
                              ),
                            ),
                            const SizedBox(width: 16),
                            GestureDetector(
                                onTap: () => goTo(linkedin),
                                child: const ImageIcon(
                                  AssetImage('assets/icons/linkedin.png'),
                                  size: 26,
                                  color: Colors.white,
                                )),
                          ],
                        )
                      ],
                    ),
                  ],
                ),
              ),
            ),
          ),
          if (isOwn)
          Padding(
            padding: const EdgeInsets.only(top: 18, right: 18),
            child: Align(
              alignment: Alignment.topRight,
              child: GestureDetector(
                onTap: () => Navigator.push(
                  context,
                  MaterialPageRoute(
                    builder: (context) => EditProfile(),
                  ),
                ),
                child: SvgPicture.asset(
                  'assets/icons/pencil.svg',
                  height: 18,
                  width: 18,
                  colorFilter: ColorFilter.mode(
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
