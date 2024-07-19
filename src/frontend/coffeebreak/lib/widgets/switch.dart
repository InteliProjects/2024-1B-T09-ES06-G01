import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:coffeebreak/models/theme_model.dart';

/// Este widget representa um botão para alternar entre os temas do aplicativo.
///
/// Parâmetros:
/// - `valor` (bool): O estado atual do botão, indicando se o tema claro está selecionado (true) ou não (false).
///
/// Comportamento:
/// - Quando clicado, alterna entre os temas claro e escuro do aplicativo.
class SwitchTema extends StatelessWidget {
  final bool valor;

  const SwitchTema({super.key, required this.valor});

  @override
  Widget build(BuildContext context) {
    final theme = Provider.of<TemaModel>(context).theme;
    return Semantics(
      label: 'Botão para mudar o tema do aplicativo',
      child: AnimatedContainer(
        duration: const Duration(milliseconds: 300),
        width: 40,
        height: 20,
        decoration: BoxDecoration(
          borderRadius: BorderRadius.circular(15),
          color: theme.switchBackground,
        ),
        child: Stack(
          alignment: Alignment.center,
          children: [
            AnimatedPositioned(
              duration: const Duration(milliseconds: 300),
              curve: Curves.easeIn,
              left: valor ? 22 : 2,
              child: Container(
                width: 16,
                height: 16,
                decoration: BoxDecoration(
                  shape: BoxShape.circle,
                  color: theme.switchColor,
                ),
              ),
            ),
          ],
        ),
      ),
    );
  }
}
