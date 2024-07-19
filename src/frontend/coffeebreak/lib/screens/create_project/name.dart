import 'package:coffeebreak/models/project_informations.dart';
import 'package:coffeebreak/screens/create_project/description.dart';
import 'package:coffeebreak/screens/create_project/subtheme.dart';
import 'package:flutter/material.dart';
import 'package:coffeebreak/models/theme_model.dart';
import 'package:coffeebreak/layouts/layout.dart';
import 'package:provider/provider.dart';
import 'package:coffeebreak/widgets/inputs/input.dart';
import 'package:coffeebreak/widgets/buttons/next.dart';

class CreateProjectName extends StatefulWidget {
  final ProjectInformations projectInformations;
  CreateProjectName({Key? key, required this.projectInformations});

  @override
  _CreateProjectNameState createState() => _CreateProjectNameState();
}

class _CreateProjectNameState extends State<CreateProjectName> {
  late String _title;

  @override
  void initState() {
    super.initState();
    _title = widget.projectInformations.title ?? '';
  }

  Widget build(BuildContext context) {
    final theme = Provider.of<TemaModel>(context).theme;

    return Layout(
      page: 'Qual o nome do projeto?',
      backScreen: CreateProjectSubtheme(
          projectInformations: widget.projectInformations),
      child: Row(
        children: [
          Expanded(
            child: Input(
              alt: 'Campo de entrada para o nome do projeto',
              initialValue: widget.projectInformations.title,
              labelText: '',
              icon: null,
              onChanged: (value) {
                _title = value;
              },
            ),
          ),
          NextButton(
            text: _title,
            canContinue: true,
            onPressed: () {
              widget.projectInformations?.title = _title;
              Navigator.push(
                context,
                MaterialPageRoute(
                  builder: (context) => CreateProjectDescription(
                      projectInformations: widget.projectInformations),
                ),
              );
            },
          ),
        ],
      ),
    );
  }
}
