import 'package:flutter/material.dart';

/// Este mapa associa uma categoria a um gradiente linear específico.
final Map<String, LinearGradient> gradientCategories = {
  'diversidade':
      const LinearGradient(colors: [Color(0xFFC84666), Color(0xFFCB7087)]),
  'produtividade':
      const LinearGradient(colors: [Color(0xFFCBA154), Color(0xFFFFDEA1)]),
  'integridade':
      const LinearGradient(colors: [Color(0xFFE39145), Color(0xFFFFC086)]),
  'bem-estar':
      const LinearGradient(colors: [Color(0xFFB66184), Color(0xFFFFB2C5)]),
  'redução':
      const LinearGradient(colors: [Color(0xFF11758C), Color(0xFF7AC5D7)]),
  'conservação':
      const LinearGradient(colors: [Color(0xFF468E74), Color(0xFF76D1B0)]),
};

/// Este mapa associa um macrotema a uma cor específica.
final Map<String, Color> macrothemeColors = {
  'diversidade': Color(0xFFC84666),
  'produtividade': Color(0xFFCBA154),
  'integridade': Color(0xFFE39145),
  'bem-estar': Color(0xFFB66184),
  'redução': Color(0xFF11758C),
  'conservação': Color(0xFF468E74),
};

/// Esta classe define o tema personalizado do aplicativo Coffeebreak.
class CoffeebreakTheme {
  final ThemeData themeData;
  final String lightLogo;
  final String darkLogo;
  final Color primaryBackground;
  final Color secondaryBackground;
  final Color primaryText;
  final Color secondaryText;
  final Color buttonText;
  final Color switchColor;
  final Color icon;
  final Color primaryButton;
  final LinearGradient secondaryButton;
  final Color switchBackground;
  final Color outline;
  final Color input;
  final Color description;

  /// Retorna o gradiente linear associado a uma categoria específica.
  LinearGradient getGradienteCategoria(String categoria) {
    return gradientCategories[categoria] ??
        const LinearGradient(colors: [Colors.white, Colors.white]);
  }

  /// Retorna a cor associada a um macrotema específico.
  Color getMacrothemeColor(String macrotheme) {
    return macrothemeColors[macrotheme] ?? Colors.white;
  }

  CoffeebreakTheme({
    required this.themeData,
    required this.lightLogo,
    required this.darkLogo,
    required this.primaryBackground,
    required this.secondaryBackground,
    required this.primaryText,
    required this.secondaryText,
    required this.switchBackground,
    required this.buttonText,
    required this.icon,
    required this.primaryButton,
    required this.secondaryButton,
    required this.switchColor,
    required this.outline,
    required this.input,
    required this.description,
  });
}

/// Este é o tema claro padrão do aplicativo Coffeebreak.
CoffeebreakTheme lightTheme = CoffeebreakTheme(
  themeData: ThemeData.light(),
  lightLogo: 'assets/img/logo-branco.png',
  darkLogo: 'assets/img/logo-preto.png',
  primaryBackground: const Color(0xFFFFFFFF),
  secondaryBackground: const Color(0xFFD4F4EC),
  primaryText: const Color(0xFF383830),
  buttonText: const Color(0xFFFFFFF0),
  secondaryText: const Color(0xFF42988C),
  switchColor: const Color(0xFF42988C),
  icon: const Color(0xFF383830),
  primaryButton: const Color(0xFFD4F4EC),
  secondaryButton:
      const LinearGradient(colors: [Color(0xFF3A8A88), Color(0xFF55BB98)]),
  switchBackground: const Color(0xFF89C7BE),
  outline: const Color(0xFFE3E3E3),
  input: const Color(0xFF42988C),
  description: Color(0xFFD4F4EC),
);

/// Este é o tema escuro padrão do aplicativo Coffeebreak.
CoffeebreakTheme darkTheme = CoffeebreakTheme(
  themeData: ThemeData.dark(),
  lightLogo: 'assets/img/logo-branco.png',
  darkLogo: 'assets/img/logo-preto.png',
  primaryBackground: const Color(0xFF1B211F),
  secondaryBackground: const Color(0xFF223D36),
  primaryText: const Color(0xFFFFFFF0),
  secondaryText: const Color(0xFF42988C),
  buttonText: const Color(0xFFFFFFF0),
  switchColor: const Color(0xFF42988C),
  icon: const Color(0xFFFFFFF0),
  primaryButton: const Color(0xFF223D36),
  secondaryButton:
      const LinearGradient(colors: [Color(0xFF3A8A88), Color(0xFF55BB98)]),
  switchBackground: const Color(0xFF1B211F),
  outline: const Color(0xFF242D2C),
  input: const Color(0xFF42988C),
  description: Color(0xFF18342D),
);
