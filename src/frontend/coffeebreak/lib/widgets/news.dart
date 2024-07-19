import 'package:coffeebreak/models/theme_model.dart';
import 'package:coffeebreak/custom/text_styles.dart';
import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:coffeebreak/utils/utils.dart';
import 'package:url_launcher/url_launcher.dart';

/// Este widget representa um cartão de notícia que pode ser clicado para abrir o link da notícia em um navegador.
/// Ele exibe uma imagem, o nome do portal e o título da notícia.
///
/// Parâmetros:
/// - `portal` (String): O nome do portal de notícias.
/// - `news` (String): O título da notícia.
/// - `link` (String): O link para a notícia completa.
/// - `image` (String): A URL da imagem a ser exibida.
///
/// Comportamento:
/// - Ao clicar no cartão, o link da notícia é aberto em um navegador utilizando o pacote `url_launcher`.
/// - Se o link não puder ser aberto, uma exceção é lançada.
///
/// Este widget fornece uma forma visualmente atraente e interativa para exibir e acessar notícias.
class NewsCard extends StatelessWidget {
  final String portal;
  final String news;
  final String link;
  final String image;

  const NewsCard({
    Key? key,
    required this.portal,
    required this.news,
    required this.link,
    required this.image,
  }) : super(key: key);

  void goTo(String url) async {
    final Uri _url = Uri.parse(url);
    if (await canLaunchUrl(_url)) {
      await launchUrl(_url);
    } else {
      throw 'Não foi possível abrir $_url';
    }
  }

  @override
  Widget build(BuildContext context) {
    final theme = Provider.of<TemaModel>(context).theme;

    return Semantics(
      label: 'Notícia',
      child: Card(
        child: InkWell(
          onTap: () => goTo(link),
          child: Container(
            width: double.infinity,
            decoration: BoxDecoration(
              border: Border.all(
                color: theme.outline,
                width: 2,
              ),
              borderRadius: BorderRadius.circular(6),
            ),
            child: Column(
              children: [
                SizedBox(
                  height: 164,
                  width: double.infinity,
                  child: FadeInImage.assetNetwork(
                    placeholder: '../assets/img/placeholder.png', // Caminho para o placeholder
                    image: image,
                    fit: BoxFit.cover,
                  ),
                ),
                Padding(
                  padding: const EdgeInsets.only(
                    top: 11,
                    bottom: 22,
                    left: 22,
                    right: 22,
                  ),
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Text(
                        portal,
                        maxLines: 1,
                        overflow: TextOverflow.ellipsis,
                        style: CoffebreakTextStyle.auxiliary
                            .copyWith(color: theme.primaryText),
                      ),
                      const SizedBox(height: 5.5),
                      Text(
                        news,
                        maxLines: 3,
                        overflow: TextOverflow.ellipsis,
                        style: CoffebreakTextStyle.auxiliary
                            .copyWith(color: theme.primaryText),
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
