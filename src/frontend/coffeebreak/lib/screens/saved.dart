import 'package:coffeebreak/layouts/layout.dart';
import 'package:coffeebreak/models/ceo.dart';
import 'package:coffeebreak/widgets/macrotheme_grid.dart';
import 'package:coffeebreak/widgets/project.dart';
import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

final projects = [
  Project(
    id: 1,
    ceoId: 1001,
    description: 'aaa',
    macrotheme: 'conservação',
    subtheme: 'Descarbonização',
    interations: false,
    title:
        'Apoio a agenda de descarbonização na cadeia de suprimentos. Apoio a agenda de descarbonização na cadeia de suprimentos. Apoio a agenda de descarbonização na cadeia de suprimentos. Apoio a agenda de descarbonização na cadeia de suprimentos.',
    ceos: [
      Ceo(
          id: 60,
          name: 'Maria',
          enterprise: 'Google',
          image: 'https://api.dicebear.com/8.x/micah/svg?seed=Spooky'),
    ],
  ),
  Project(
    id: 3,
    description: 'aaa',
    ceoId: 1001,
    macrotheme: 'conservação',
    subtheme: 'Ambiental',
    interations: false,
    title:
        'Apoio a agenda de descarbonização na cadeia de suprimentos. Apoio a agenda de descarbonização na cadeia de suprimentos. Apoio a agenda de descarbonização na cadeia de suprimentos. Apoio a agenda de descarbonização na cadeia de suprimentos.',
               ceos: [
                    Ceo(
        id: 1,
        name: 'Ana',
        enterprise: 'Nubank',
        image: 'https://api.dicebear.com/8.x/micah/svg?seed=Spooky',
      ),
                Ceo(
        id: 1,
        name: 'Ana',
        enterprise: 'Nubank',
        image: 'https://api.dicebear.com/8.x/micah/svg?seed=Spooky',
      ),
            ],
  ),
];

class Saved extends StatelessWidget {
  const Saved({super.key});

  @override
  Widget build(BuildContext context) {
    return Layout(
      page: 'Salvos',
      child: SingleChildScrollView(
        // Permite a rolagem da página
        child: Column(
          children: [
            ListView.separated(
              physics:
                  NeverScrollableScrollPhysics(), // Desabilita a rolagem da ListView
              shrinkWrap:
                  true, // Garante que a ListView ocupe o espaço de seus filhos
              itemCount: projects.length,
              itemBuilder: (context, index) {
                return projects[index];
              },
              separatorBuilder: (context, index) => SizedBox(height: 17),
            ),
          ],
        ),
      ),
    );
  }
}
