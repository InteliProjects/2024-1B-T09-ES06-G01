import 'package:coffeebreak/custom/themes.dart';
import 'package:flutter/material.dart';

/// Esta classe gerencia o tema do aplicativo, permitindo alternar entre os temas claro e escuro.
///
/// Propriedades:
/// - `isLightTheme` (bool): Indica se o tema atual é claro.
/// - `theme` (CoffeebreakTheme): Retorna o tema atual do aplicativo.
///
/// Métodos:
/// - `switchTheme(bool isLight)`: Altera o tema do aplicativo com base no parâmetro fornecido.
///
/// Observador:
/// - Notifica os ouvintes quando o tema é alterado.
class TemaModel with ChangeNotifier {
  bool _isLightTheme = true;

  bool get isLightTheme => _isLightTheme;

  CoffeebreakTheme get theme => _isLightTheme ? lightTheme : darkTheme;

  void switchTheme(bool isLight) {
    _isLightTheme = isLight;
    notifyListeners();
  }
}
