import 'package:flutter/material.dart';
import 'package:coffeebreak/custom/text_styles.dart';

/// Este widget representa um botão personalizado, que pode incluir texto, ícone e/ou gradiente.
///
/// Parâmetros:
/// - `text` (String): O texto exibido no botão.
/// - `gradient` (Gradient?, opcional): O gradiente de cores aplicado ao botão.
/// - `backgroundColor` (Color): A cor de fundo do botão quando nenhum gradiente é fornecido.
/// - `textColor` (Color): A cor do texto e do ícone no botão.
/// - `icon` (IconData?, opcional): O ícone exibido no botão.
/// - `onPressed` (VoidCallback): A função de retorno de chamada chamada quando o botão é pressionado.
/// - `width` (double?, opcional): A largura do botão.
/// - `height` (double): A altura do botão.
/// - `routeName` (String?, opcional): O nome da rota para navegação ao pressionar o botão.
/// - `routeArguments` (Object?, opcional): Os argumentos passados para a rota quando o botão é pressionado.
/// - `alt` (String?, opcional): Texto alternativo para acessibilidade.
///
/// Comportamento:
/// - Ao ser tocado, o botão executa a função de retorno de chamada fornecida ou navega para a rota especificada.
class CustomButton extends StatelessWidget {
  final String text;
  final Gradient? gradient;
  final Color backgroundColor;
  final Color textColor;
  final IconData? icon;
  final VoidCallback onPressed;
  final double? width;
  final double height;
  final String? routeName;
  final Object? routeArguments;
  final String? alt;

  const CustomButton({
    super.key,
    required this.text,
    this.gradient,
    this.backgroundColor = Colors.white,
    required this.textColor,
    this.icon,
    required this.onPressed,
    this.width,
    this.height = 55.0,
    this.routeName,
    this.routeArguments,
    this.alt,
  });

  @override
  Widget build(BuildContext context) {
    return Semantics(
      label: alt ?? 'Botão',
      child: Container(
        width: width,
        height: height,
        decoration: BoxDecoration(
          gradient: gradient,
          color: gradient == null
              ? backgroundColor
              : null, // Background color if gradient not provided.
          borderRadius: BorderRadius.circular(6),
        ),
        child: ElevatedButton(
          style: ElevatedButton.styleFrom(
            foregroundColor:
                textColor, // Set the foreground color for the text and icons.
            backgroundColor: Colors
                .transparent, // Set the background color to transparent to display the container's gradient.
            shape: RoundedRectangleBorder(
              borderRadius: BorderRadius.circular(6),
            ),
            padding: const EdgeInsets.symmetric(horizontal: 16),
            elevation: 0,
          ),
          onPressed: () {
            if (routeName != null) {
              Navigator.of(context)
                  .pushNamed(routeName!, arguments: routeArguments);
            } else {
              onPressed();
            }
          },
          child: Row(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              if (icon != null)
                Icon(icon, color: textColor), // Icon with defined color.
              const SizedBox(width: 8),
              Text(text,
                  style: CoffebreakTextStyle.input), // Imported style text.
            ],
          ),
        ),
      ),
    );
  }
}

// Buttons to be used.:

  // "Sign in" button
  
          // CustomButton(
          //   text: "Entrar",
          //   textColor: Colors.white,
          //   gradient: theme.secondaryButton,
          //   onPressed: () => Navigator.of(context).pushNamed(w"/login"),
          // ),

  // "Sign in with Google" button

          // CustomButton(
          //   text: "Entrar com Google",
          //   textColor: theme.input,
          //   icon: FontAwesomeIcons.google,
          //   backgroundColor: theme.primaryButton,
          //   onPressed: () => Navigator.of(context).pushNamed("/googleLogin"),
          // ),

  // "See more" button.

          // CustomButton(
          //   text: "Ver Mais",
          //   textColor: Colors.white,
          //   backgroundColor: theme.getMacrothemeColor(macrotheme), 
          //   height: 42,
          //   width: 312,
          //   onPressed: () => Navigator.of(context).pushNamed(
          //   "/projectDetails",
          //   arguments: {'projectId': '123'}
          //   ),
          // ),