import 'package:coffeebreak/models/theme_model.dart';
import 'package:flutter/material.dart';
import 'package:flutter_svg/flutter_svg.dart';
import 'package:provider/provider.dart';

/// Este widget representa um cartão de avatar do usuário.
///
/// Parâmetros:
/// - `image` (String): O link da imagem do avatar do usuário.
/// - `onTap` (void Function(String)): A função de retorno de chamada chamada quando o cartão de avatar é tocado.
///
/// Comportamento:
/// - Ao ser tocado, o cartão de avatar executa a função de retorno de chamada fornecida.
class AvatarCard extends StatelessWidget {
  final String image;
  final void Function(String) onTap;

  const AvatarCard({
    super.key,
    required this.image,
    required this.onTap,
  });

  @override
  Widget build(BuildContext context) {
    final theme = Provider.of<TemaModel>(context).theme;

    return Semantics(
      label: 'Imagem do avatar do usuário',
      child: GestureDetector(
        onTap: () => onTap(image),
        child: Container(
          width: 78,
          height: 78,
          decoration: BoxDecoration(
            color: theme.description,
            borderRadius: BorderRadius.circular(10),
          ),
          child: SvgPicture.network(
            image,
            fit: BoxFit.cover,
          ),
        ),
      ),
    );
  }
}
