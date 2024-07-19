import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:coffeebreak/models/theme_model.dart';
import 'package:like_button/like_button.dart';

/// Este widget representa uma linha de botões de interação, incluindo botões de curtir e de salvar.
/// Cada botão usa o pacote `like_button` para fornecer animações e contagens de interações.
///
/// Propriedades:
/// - `buttonSize` (double): Define o tamanho dos botões de interação.
///
/// Comportamento:
/// - O botão de curtir alterna entre ícone de coração cheio e contorno, com animações e bolhas coloridas.
/// - O botão de salvar alterna entre ícone de marcador cheio e contorno, com animações e bolhas coloridas.
/// - A contagem de interações é exibida ao lado dos ícones e ajusta conforme o estado de interação.
class Interations extends StatelessWidget {
  final double buttonSize = 30.0;

  @override
  Widget build(BuildContext context) {
    final theme = Provider.of<TemaModel>(context).theme;

    return Semantics(
      label: 'Interações',
      child: Row(
        mainAxisSize: MainAxisSize.min,
        children: [
          LikeButton(
            size: buttonSize,
            circleColor:
                CircleColor(start: Color(0xff00ddff), end: Color(0xff0099cc)),
            bubblesColor: BubblesColor(
              dotPrimaryColor: Color(0xff33b5e5),
              dotSecondaryColor: Color(0xff0099cc),
            ),
            likeBuilder: (bool isLiked) {
              return Icon(
                isLiked ? Icons.favorite : Icons.favorite_border,
                color: isLiked ? theme.input : theme.input,
                size: buttonSize,
              );
            },
            likeCount: 10, // Exemplo de número inicial de curtidas
            countBuilder: (int? count, bool isLiked, String text) {
              return Text(
                text,
                style: TextStyle(color: isLiked ? theme.input : theme.input),
              );
            },
          ),
          SizedBox(width: 16),
          LikeButton(
            size: buttonSize,
            circleColor:
                CircleColor(start: Color(0xff00ddff), end: Color(0xff0099cc)),
            bubblesColor: BubblesColor(
              dotPrimaryColor: Color(0xff33b5e5),
              dotSecondaryColor: Color(0xff0099cc),
            ),
            likeBuilder: (bool isLiked) {
              return Icon(
                isLiked ? Icons.bookmark : Icons.bookmark_border,
                color: isLiked ? theme.input : theme.input,
                size: buttonSize,
              );
            },
            countBuilder: (int? count, bool isLiked, String text) {
              return Text(
                text,
                style: TextStyle(color: isLiked ? theme.input : theme.input),
              );
            },
          ),
        ],
      ),
    );
  }
}
