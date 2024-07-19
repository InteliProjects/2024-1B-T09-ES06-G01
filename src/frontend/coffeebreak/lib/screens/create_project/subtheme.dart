import 'package:coffeebreak/models/project_informations.dart';
import 'package:coffeebreak/screens/create_project/index.dart';
import 'package:coffeebreak/screens/create_project/name.dart';
import 'package:coffeebreak/widgets/subtheme.dart';
import 'package:flutter/material.dart';
import 'package:coffeebreak/models/theme_model.dart';
import 'package:coffeebreak/layouts/layout.dart';
import 'package:provider/provider.dart';
import 'package:coffeebreak/widgets/buttons/button.dart';

class CreateProjectSubtheme extends StatelessWidget {
  final ProjectInformations projectInformations;
  const CreateProjectSubtheme({Key? key, required this.projectInformations});

  @override
  Widget build(BuildContext context) {
    final theme = Provider.of<TemaModel>(context).theme;

    return Layout(
      page: 'Qual o subtema do projeto?',
      backScreen: CreateProject(projectInformations: projectInformations),
      child: Subtheme(subtheme: 'Cultivo e Regeneração', projectInformations: projectInformations),
    );
  }
}
