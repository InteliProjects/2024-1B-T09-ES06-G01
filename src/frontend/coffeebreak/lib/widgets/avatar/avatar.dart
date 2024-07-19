import 'package:coffeebreak/models/theme_model.dart';
import 'package:flutter/material.dart';
import 'package:flutter_svg/flutter_svg.dart';
import 'package:provider/provider.dart';

/// Este widget exibe a imagem do avatar do usuário em um círculo.
///
/// Parâmetros:
/// - `image` (String): O link da imagem do avatar do usuário.
///
/// Estrutura:
/// - Um contêiner com forma de círculo que envolve a imagem do avatar do usuário.
class Avatar extends StatelessWidget {
  final String image;

  const Avatar({
    super.key,
    required this.image,
  });

  @override
  Widget build(BuildContext context) {
    final theme = Provider.of<TemaModel>(context).theme;

    return Semantics(
      label: 'Imagem do avatar do usuário',
      child: Container(
        decoration: BoxDecoration(
          color: theme.primaryBackground,
          shape: BoxShape.circle,
        ),
        child: ClipOval(
          child: SvgPicture.network(
            image,
            width: 35,
            height: 35,
            fit: BoxFit.cover,
          ),
        ),
      ),
    );
  }
}
