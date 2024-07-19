import 'package:coffeebreak/models/theme_model.dart';
import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

/// Este widget representa um campo de entrada de texto multilinha.
///
/// Parâmetros:
/// - `onChanged` (void Function(String)?): A função de retorno de chamada que será chamada sempre que o texto for alterado.
/// - `maxLength` (int): O número máximo de caracteres permitidos no campo de entrada.
/// - `minLines` (int): O número mínimo de linhas visíveis no campo de entrada.
/// - `initialValue` (String?, opcional): O valor inicial do campo de entrada.
/// - `alt` (String?, opcional): Texto alternativo para acessibilidade.
///
/// Comportamento:
/// - As cores do rótulo e da borda do campo de entrada são definidas pelo tema atual.
/// - O número máximo de caracteres permitidos é especificado pelo parâmetro `maxLength`.
class TextArea extends StatefulWidget {
  final void Function(String)? onChanged;
  final int maxLength;
  final int minLines;
  final String? initialValue;
  final String? alt;

  const TextArea({
    Key? key,
    required this.onChanged,
    this.maxLength = 1000,
    this.minLines = 14,
    this.initialValue,
    this.alt
  }) : super(key: key);

  @override
  _TextAreaState createState() => _TextAreaState();
}

class _TextAreaState extends State<TextArea> {
  late TextEditingController _controller;

  @override
  void initState() {
    super.initState();
    _controller = TextEditingController(text: widget.initialValue);
  }

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    final theme = Provider.of<TemaModel>(context).theme;

    return Semantics(
      label: widget.alt ?? 'Campo de entrada',
      child: SizedBox(
        width: double.infinity,
        child: TextField(
          controller: _controller,
          onChanged: widget.onChanged,
          keyboardType: TextInputType.multiline,
          minLines: widget.minLines,
          maxLines: null,
          maxLength: widget.maxLength,
          obscureText: false,
          style: TextStyle(color: theme.primaryText),
          decoration: InputDecoration(
            labelStyle: TextStyle(color: theme.input),
            border: OutlineInputBorder(
              borderRadius: BorderRadius.all(Radius.circular(6.0)),
              borderSide: BorderSide(
                color: theme.input,
                width: 1.0,
              ),
            ),
            focusedBorder: OutlineInputBorder(
              borderRadius: BorderRadius.all(Radius.circular(6.0)),
              borderSide: BorderSide(
                color: theme.input,
                width: 2.0,
              ),
            ),
            enabledBorder: OutlineInputBorder(
              borderRadius: BorderRadius.all(Radius.circular(6.0)),
              borderSide: BorderSide(
                color: theme.input,
                width: 1.0,
              ),
            ),
            disabledBorder: OutlineInputBorder(
              borderRadius: BorderRadius.all(Radius.circular(6.0)),
              borderSide: BorderSide(
                color: theme.input.withOpacity(0.5),
                width: 1.0,
              ),
            ),
          ),
        ),
      ),
    );
  }
}
