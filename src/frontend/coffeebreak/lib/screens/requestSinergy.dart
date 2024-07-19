import 'package:coffeebreak/models/theme_model.dart';
import 'package:coffeebreak/custom/themes.dart';
import 'package:coffeebreak/widgets/buttons/button.dart';
import 'package:coffeebreak/widgets/info_card.dart';
import 'package:flutter/material.dart';
import 'package:coffeebreak/layouts/layout.dart';
import 'package:provider/provider.dart';
import 'package:coffeebreak/widgets/projectSinergy.dart';
import 'package:coffeebreak/models/ceo.dart';

class RequestSinergy extends StatelessWidget {
  const RequestSinergy({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    final theme = Provider.of<TemaModel>(context).theme;

    return Layout(
      page: 'Solicitação de Sinergia',
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.stretch,
        children: [
          ProjectSinergy(
            id: 1,
            macrotheme: 'diversidade',
            interest: 'Redução de emissão de gás carbono',
            interestTwo: 'Integrar',
            subtheme: 'Descarbonização',
            interations: false,
            ceos: [ 
              Ceo(
                id: 59,
                name: 'João Dono',
                enterprise: 'Google',
                image: 'https://api.dicebear.com/8.x/miniavs/svg',
              ),
            ],
          ),
          SizedBox(height: 20),
          const InfoCard(
            title: 'Motivo do Interesse',
            description:
                'Este projeto visa aumentar a representatividade de mulheres em cargos de liderança e operacionais dentro de nossa empresa. Através de iniciativas como mentorias, workshops de desenvolvimento profissional, e políticas de contratação inclusivas, buscamos não apenas equilibrar a proporção de gênero em todos os níveis hierárquicos, mas também fortalecer uma cultura de igualdade e respeito. O programa inclui parcerias com universidades e organizações não governamentais para recrutamento e formação de talentos femininos, garantindo uma trajetória sustentável e inclusiva.',
          ),
          SizedBox(height: 20),
          CustomButton(
            alt: 'Botão de aceitar sinergia',
            text: "Aceitar",
            textColor: Colors.white,
            gradient: theme.secondaryButton,
            height: 42,
            width: 312,
            onPressed: () => Navigator.of(context).pushNamed(
              "/projectDetails",
              arguments: {'projectId': '123'},
            ),
          ),
          SizedBox(height: 10), // Espaçamento entre os CustomButtons
          CustomButton(
            alt: 'Botão de negar sinergia',
            text: "Negar",
            textColor: Colors.white,
          backgroundColor: Color(0xFFC84666),
            height: 42,
            width: 312,
            onPressed: () => Navigator.of(context).pushNamed(
              "/projectDetails",
              arguments: {'projectId': '123'},
            ),
          ),
        ],
      ),
    );
  }
}
