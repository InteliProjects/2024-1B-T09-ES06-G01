import 'package:flutter/material.dart';
import 'package:coffeebreak/models/theme_model.dart';
import 'package:coffeebreak/layouts/layout.dart';
import 'package:provider/provider.dart';
import 'package:coffeebreak/widgets/inputs/text_area.dart';
import 'package:coffeebreak/widgets/buttons/next.dart';
import 'package:coffeebreak/screens/submit_sinergy/synergy_summary.dart';

class SynergyReason extends StatefulWidget {
  final String synergyType;

  const SynergyReason({Key? key, required this.synergyType}) : super(key: key);

  @override
  _SynergyReasonState createState() => _SynergyReasonState();
}

class _SynergyReasonState extends State<SynergyReason> {
  String reason = '';

  @override
  Widget build(BuildContext context) {
    final theme = Provider.of<TemaModel>(context).theme;

    return Layout(
      page: 'Por que você deseja realizar uma sinergia com esse projeto?',
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          TextArea(
            alt: 'Campo de entrada para a descrição',
            onChanged: (value) {
              setState(() {
                reason = value;
              });
            },
          ),
          SizedBox(height: 20),
          Row(
            children: [
              Spacer(), // Empurra o botão para a direita
              NextButton(
                canContinue: reason.isNotEmpty,
                onPressed: () {
                  Navigator.push(
                    context,
                    MaterialPageRoute(
                      builder: (context) => SynergySummary(
                        reason: reason,
                        synergyType: widget.synergyType,
                      ),
                    ),
                  );
                },
                text: 'Próximo',
              ),
            ],
          ),
        ],
      ),
    );
  }
}
