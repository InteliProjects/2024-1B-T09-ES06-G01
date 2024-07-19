import 'package:coffeebreak/layouts/layout.dart';
import 'package:coffeebreak/models/ceo.dart';
import 'package:coffeebreak/widgets/macrotheme_grid.dart';
import 'package:coffeebreak/widgets/project.dart';
import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

final projects = [
  Project(
    id: 1,
    ceoId: 1003,
    description: 'aaa',
    macrotheme: 'conservação',
    subtheme: 'Descarbonização',
    interations: false,
    title:
        'Apoio a agenda de descarbonização na cadeia de suprimentos. Apoio a agenda de descarbonização na cadeia de suprimentos. Apoio a agenda de descarbonização na cadeia de suprimentos. Apoio a agenda de descarbonização na cadeia de suprimentos.',
    ceos: [
      Ceo(
          id: 1,
          name: 'Pedro',
          enterprise: 'Google',
          image: 'https://api.dicebear.com/8.x/miniavs/svg'),
    ],
  ),
  Project(
    id: 13,
    description: 'aaa',
    ceoId: 1003,
    macrotheme: 'diversidade',
    subtheme: 'Feminismo',
    interations: false,
    title:
        'Apoio a agenda de descarbonização na cadeia de suprimentos. Apoio a agenda de descarbonização na cadeia de suprimentos. Apoio a agenda de descarbonização na cadeia de suprimentos. Apoio a agenda de descarbonização na cadeia de suprimentos.',
    ceos: [
      Ceo(
          id: 22,
          name: 'João',
          enterprise: 'Google',
          image: 'https://api.dicebear.com/8.x/micah/svg?seed=Bear'),
      Ceo(
          id: 32,
          name: 'Arthur',
          enterprise: 'Nubank',
          image: 'https://api.dicebear.com/8.x/big-ears/svg?seed=Gizmo'),
      Ceo(
          id: 24,
          name: 'Ana',
          enterprise: 'Nubank',
          image: 'https://api.dicebear.com/8.x/micah/svg?seed=Spooky'),
    ],
  ),
  Project(
    id: 3,
    description: 'aaa',
    ceoId: 1003,
    macrotheme: 'conservação',
    subtheme: 'Ambiental',
    interations: false,
    title:
        'Apoio a agenda de descarbonização na cadeia de suprimentos. Apoio a agenda de descarbonização na cadeia de suprimentos. Apoio a agenda de descarbonização na cadeia de suprimentos. Apoio a agenda de descarbonização na cadeia de suprimentos.',
    ceos: [
      Ceo(
          id: 15,
          name: 'João',
          enterprise: 'Google',
          image: 'https://api.dicebear.com/8.x/big-ears/svg?seed=Gizmo'),
      Ceo(
          id: 16,
          name: 'Ana',
          enterprise: 'Nubank',
          image: 'https://api.dicebear.com/8.x/micah/svg?seed=Spooky'),
    ],
  ),
];

class Liked extends StatelessWidget {
  const Liked({super.key});

  @override
  Widget build(BuildContext context) {
    return Layout(
      page: 'Curtidos',
      child: SingleChildScrollView(
        child: Column(
          children: [
            ListView.separated(
              physics: NeverScrollableScrollPhysics(),
              shrinkWrap: true,
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
