import 'package:coffeebreak/models/theme_model.dart';
import 'package:coffeebreak/custom/text_styles.dart';
import 'package:coffeebreak/custom/themes.dart';
import 'package:coffeebreak/utils/utils.dart';
import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:font_awesome_flutter/font_awesome_flutter.dart';
import 'package:flutter_svg/flutter_svg.dart';

/// Este widget representa um ícone associado a um macrotema específico. Ele carrega um arquivo SVG
/// baseado no macrotema fornecido e aplica estilos conforme o tema atual e os parâmetros opcionais.
///
/// Parâmetros:
/// - `macrotheme` (String): O nome do macrotema que define o ícone exibido.
/// - `overlay` (bool?, opcional): Define se uma sobreposição de cor deve ser aplicada ao ícone. Padrão é `false`.
/// - `height` (double?, opcional): A altura do ícone. Padrão é `20.0`.
/// - `width` (double?, opcional): A largura do ícone. Padrão é `20.0`.
///
/// Comportamento:
/// - O ícone é carregado de um arquivo SVG localizado na pasta `assets/icons/macrothemes/`.
/// - A cor do ícone é determinada pelo tema atual ou pela sobreposição se `overlay` for `true`.
class ProjectIcon extends StatelessWidget {
  final String macrotheme;
  final bool? overlay;
  final double? height;
  final double? width;

  const ProjectIcon({
    Key? key,
    required this.macrotheme,
    this.overlay = false,
    this.height = 20.0,
    this.width = 20.0,
  });

  @override
  Widget build(BuildContext context) {
    final theme = Provider.of<TemaModel>(context).theme;
    return Semantics(
      label: 'Ícone do macrotema "${macrotheme}"',
      child: SvgPicture.asset(
        'assets/icons/macrothemes/${macrotheme}.svg',
        height: height,
        width: width,
        colorFilter: ColorFilter.mode(
          overlay!
              ? Color.fromARGB(23, 0, 0, 0)
              : theme.getMacrothemeColor(macrotheme),
          BlendMode.srcIn,
        ),
      ),
    );
  }
}
