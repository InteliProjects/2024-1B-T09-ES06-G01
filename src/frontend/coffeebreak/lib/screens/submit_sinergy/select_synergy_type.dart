import 'package:flutter/material.dart';
import 'package:coffeebreak/models/theme_model.dart';
import 'package:coffeebreak/layouts/layout.dart';
import 'package:coffeebreak/screens/submit_sinergy/synergy_reason.dart';
import 'package:coffeebreak/widgets/buttons/button.dart';
import 'package:provider/provider.dart';

class SelectSynergyType extends StatelessWidget {
  const SelectSynergyType({super.key});

  @override
  Widget build(BuildContext context) {
    final theme = Provider.of<TemaModel>(context).theme;

    return Layout(
      page: 'Qual tipo de sinergia você deseja solicitar?',
      child: Column(
        children: [
          CustomButton(
            alt: 'Botão do tipo "aprender"',
            text: "Aprender",
            textColor: theme.input,
            icon: Icons.school, // Ícone para aprender
            backgroundColor: theme.primaryButton,
            onPressed: () {
              Navigator.push(
                context,
                MaterialPageRoute(builder: (context) => SynergyReason(synergyType: 'Aprender')),
              );
            },
          ),
          SizedBox(height: 10),
          CustomButton(
            alt: 'Botão do tipo "confirmar"',
            text: "Integrar",
            textColor: theme.input,
            icon: Icons.merge_type, // Ícone já sugerido para integrar
            backgroundColor: theme.primaryButton,
            onPressed: () {
              Navigator.push(
                context,
                MaterialPageRoute(builder: (context) => SynergyReason(synergyType: 'Integrar')),
              );
            },
          ),
          SizedBox(height: 10),
          CustomButton(
            alt: 'Botão do tipo "unificar"',
            text: "Unificar",
            textColor: theme.input,
            icon: Icons.link, // Ícone para unificar
            backgroundColor: theme.primaryButton,
            onPressed: () {
              Navigator.push(
                context,
                MaterialPageRoute(builder: (context) => SynergyReason(synergyType: 'Unificar')),
              );
            },
          ),
        ],
      ),
    );
  }
}
