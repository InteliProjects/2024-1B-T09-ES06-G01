import 'package:coffeebreak/widgets/switch.dart';
import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:coffeebreak/models/theme_model.dart';
import 'package:font_awesome_flutter/font_awesome_flutter.dart'; // Para o ícone da lua
import 'package:coffeebreak/custom/text_styles.dart'; // Estilos de texto

/// Este widget representa um botão para alternar entre os temas claro e escuro do aplicativo.
///
/// Comportamento:
/// - Ao ser tocado, o botão alterna entre os temas claro e escuro do aplicativo.
class TemaSwitchButton extends StatefulWidget {
  const TemaSwitchButton({super.key});

  @override
  TemaSwitchButtonState createState() => TemaSwitchButtonState();
}

class TemaSwitchButtonState extends State<TemaSwitchButton> {
  bool _valor = false;

  @override
  void initState() {
    super.initState();
    _valor = Provider.of<TemaModel>(context, listen: false).isLightTheme;
  }

  void _toggleSwitch() {
    setState(() {
      _valor = !_valor;
      Provider.of<TemaModel>(context, listen: false).switchTheme(_valor);
    });
  }

  @override
  Widget build(BuildContext context) {
    final theme = Provider.of<TemaModel>(context).theme;

    return Semantics(
      label: 'Botão para mudar o tema do aplicativo',
      child: ElevatedButton(
        onPressed: _toggleSwitch,
        style: ElevatedButton.styleFrom(
          foregroundColor: theme.switchColor,
          backgroundColor: theme.primaryButton,
          minimumSize: const Size(double.infinity, 55),
          shape: RoundedRectangleBorder(
            borderRadius: BorderRadius.circular(6),
          ),
          padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 8),
        ),
        child: Row(
          mainAxisAlignment: MainAxisAlignment.spaceBetween,
          children: [
            const Padding(
              padding: EdgeInsets.only(left: 16),
              child: Icon(FontAwesomeIcons.sun),
            ),
            const Text("Tema claro", style: CoffebreakTextStyle.input),
            Padding(
              padding: const EdgeInsets.only(right: 16),
              child: SwitchTema(valor: _valor),
            ),
          ],
        ),
      ),
    );
  }
}
