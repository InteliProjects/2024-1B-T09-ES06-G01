import 'package:flutter/material.dart';

/// Este widget representa um botão para navegar para a próxima página.
///
/// Parâmetros:
/// - `canContinue` (bool): Indica se o botão está habilitado para avançar para a próxima página.
/// - `onPressed` (VoidCallback): A função de retorno de chamada chamada quando o botão é pressionado.
///
/// Comportamento:
/// - O botão só é habilitado para pressionar se `canContinue` for verdadeiro.
/// - Ao ser tocado, o botão executa a função de retorno de chamada fornecida.
class NextButton extends StatefulWidget {
  final bool canContinue;
  final VoidCallback onPressed;

  const NextButton({
    Key? key,
    required this.canContinue,
    required this.onPressed,
    required String text,
  }) : super(key: key);

  @override
  _NextButtonState createState() => _NextButtonState();
}

class _NextButtonState extends State<NextButton> {
  @override
  Widget build(BuildContext context) {
    return Semantics(
      label: 'Botão para navegar à próxima página',
      child: GestureDetector(
        onTap: widget.canContinue ? widget.onPressed : null,
        child: Container(
          decoration: BoxDecoration(
            color: widget.canContinue ? Color(0xFF3B8C88) : Color(0xFF18342D),
            borderRadius: BorderRadius.circular(40),
          ),
          padding: EdgeInsets.symmetric(horizontal: 11, vertical: 11),
          child: Icon(
            Icons.arrow_forward,
            color: Colors.white,
            size: 21,
          ),
        ),
      ),
    );
  }
}
