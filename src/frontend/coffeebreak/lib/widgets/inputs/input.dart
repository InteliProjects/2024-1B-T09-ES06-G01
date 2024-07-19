import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:coffeebreak/models/theme_model.dart';

class Input extends StatefulWidget {
  final IconData? icon;
  final String labelText;
  final String? initialValue;
  final String? alt;
  final void Function(String) onChanged;
  final bool isPassword;
  final TextEditingController? controller;
  final void Function(String)? onSubmitted;

  const Input({
    Key? key,
    this.icon,
    required this.labelText,
    required this.onChanged,
    this.initialValue,
    this.alt,
    this.isPassword = false,
    this.controller,
    this.onSubmitted,
  }) : super(key: key);

  @override
  _InputState createState() => _InputState();
}

class _InputState extends State<Input> {
  late TextEditingController _defaultController;
  bool _obscureText = true;

  @override
  void initState() {
    super.initState();
    _defaultController = TextEditingController(text: widget.initialValue);
    _obscureText = widget.isPassword;
  }

  @override
  Widget build(BuildContext context) {
    final theme = Provider.of<TemaModel>(context).theme;
    final controller = widget.controller ?? _defaultController;

    return Semantics(
      label: widget.alt ?? 'Campo de entrada',
      child: SizedBox(
        width: double.infinity,
        child: TextField(
          controller: controller,
          onChanged: widget.onChanged,
          onSubmitted: widget.onSubmitted,
          obscureText: _obscureText,
          style: TextStyle(color: theme.primaryText),
          decoration: InputDecoration(
            labelText: widget.labelText,
            labelStyle: TextStyle(color: theme.input),
            prefixIcon: widget.icon != null ? Icon(widget.icon, color: theme.input) : null,
            suffixIcon: widget.isPassword
                ? IconButton(
                    icon: Icon(_obscureText ? Icons.visibility_off : Icons.visibility),
                    onPressed: () {
                      setState(() {
                        _obscureText = !_obscureText;
                      });
                    },
                  )
                : null,
            border: OutlineInputBorder(
              borderRadius: BorderRadius.circular(6.0),
              borderSide: BorderSide(color: theme.input, width: 1.0),
            ),
            focusedBorder: OutlineInputBorder(
              borderRadius: BorderRadius.circular(6.0),
              borderSide: BorderSide(color: theme.input, width: 2.0),
            ),
            enabledBorder: OutlineInputBorder(
              borderRadius: BorderRadius.circular(6.0),
              borderSide: BorderSide(color: theme.input, width: 1.0),
            ),
            disabledBorder: OutlineInputBorder(
              borderRadius: BorderRadius.circular(6.0),
              borderSide: BorderSide(color: theme.input.withOpacity(0.5), width: 1.0),
            ),
          ),
        ),
      ),
    );
  }
}
