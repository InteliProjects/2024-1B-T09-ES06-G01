import 'package:flutter/material.dart';
import 'package:coffeebreak/models/theme_model.dart';
import 'package:coffeebreak/layouts/layout.dart';
import 'package:provider/provider.dart';
import 'package:coffeebreak/widgets/buttons/button.dart';
import 'package:coffeebreak/widgets/info_card.dart';
import 'package:coffeebreak/screens/finished.dart'; // Importa a página Finished

class SynergySummary extends StatelessWidget {
  final String reason;
  final String synergyType;

  const SynergySummary(
      {Key? key, required this.reason, required this.synergyType})
      : super(key: key);

  @override
  Widget build(BuildContext context) {
    final theme = Provider.of<TemaModel>(context).theme;

    IconData getIcon() {
      switch (synergyType) {
        case 'Aprender':
          return Icons.school;
        case 'Integrar':
          return Icons.merge_type;
        case 'Unificar':
          return Icons.link;
        default:
          return Icons.info_outline; // Default icon if no match is found
      }
    }

    return Layout(
      page: 'Resumo',
      child: Column(
        children: [
          CustomButton(
            alt: 'Botão de do tipo "${synergyType}"',
            text: synergyType,
            textColor: theme.input,
            icon: getIcon(), // Ícone determinado dinamicamente
            backgroundColor: theme.primaryButton,
            onPressed: () {}, // Função vazia para deixar o botão inativo
          ),
          SizedBox(height: 14),
          InfoCard(title: 'Descrição', description: reason),
          SizedBox(height: 14),
          CustomButton(
            alt: 'Botão de confirmar',
            text: "Confirmar",
            textColor: Colors.white,
            gradient: theme.secondaryButton,
            height: 55,
            onPressed: () {
              // Navega para a página Finished com o tipo sinergy
              Navigator.push(
                context,
                MaterialPageRoute(
                  builder: (context) => Finished(type: FinishedType.sinergy),
                ),
              );
            },
          ),
        ],
      ),
    );
  }
}
