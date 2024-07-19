import 'package:coffeebreak/models/project_informations.dart';
import 'package:coffeebreak/widgets/macrotheme_grid.dart';
import 'package:flutter/material.dart';
import 'package:coffeebreak/models/theme_model.dart';
import 'package:coffeebreak/layouts/layout.dart';
import 'package:provider/provider.dart';

class CreateProject extends StatelessWidget {
  final ProjectInformations projectInformations;

  CreateProject({Key? key, ProjectInformations? projectInformations})
      : projectInformations =
            projectInformations ?? ProjectInformations(userId: 1),
        super(key: key);

  @override
  Widget build(BuildContext context) {
    final theme = Provider.of<TemaModel>(context).theme;

    return Layout(
      page: 'Qual o macrotema do projeto?',
      child: MacrothemeGrid(
        navigateTo: '/create-project/subtheme',
        type: 'create_project',
        projectInformations: projectInformations,
      ),
    );
  }
}
