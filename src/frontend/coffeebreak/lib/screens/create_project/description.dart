import 'package:coffeebreak/models/project_informations.dart';
import 'package:coffeebreak/screens/create_project/name.dart';
import 'package:coffeebreak/screens/create_project/summary.dart';
import 'package:flutter/material.dart';
import 'package:coffeebreak/models/theme_model.dart';
import 'package:coffeebreak/layouts/layout.dart';
import 'package:provider/provider.dart';
import 'package:coffeebreak/widgets/inputs/input.dart';
import 'package:coffeebreak/widgets/buttons/next.dart';
import 'package:coffeebreak/widgets/inputs/text_area.dart';

class CreateProjectDescription extends StatefulWidget {
  final ProjectInformations projectInformations;

  const CreateProjectDescription({Key? key, required this.projectInformations})
      : super(key: key);

  @override
  _CreateProjectDescriptionState createState() =>
      _CreateProjectDescriptionState();
}

class _CreateProjectDescriptionState extends State<CreateProjectDescription> {
  late String _description;

  @override
  void initState() {
    super.initState();
    _description = widget.projectInformations.description ?? '';
  }

  @override
  Widget build(BuildContext context) {
    final theme = Provider.of<TemaModel>(context).theme;

    return Layout(
      page: 'Como você descreveria \nesse projeto?',
      backScreen:
          CreateProjectName(projectInformations: widget.projectInformations),
      child: Column(
        children: [
          TextArea(
            alt: 'Campo de entrada para a descrição',
            initialValue: widget.projectInformations.description,
            onChanged: (value) {
              _description = value;
            },
          ),
          Row(
            children: [
              Spacer(),
              NextButton(
                text: _description,
                canContinue: true,
                onPressed: () {
                  widget.projectInformations.description = _description;
                  Navigator.push(
                    context,
                    MaterialPageRoute(
                      builder: (context) => CreateProjectSummary(
                          projectInformations: widget.projectInformations),
                    ),
                  );
                },
              ),
            ],
          ),
        ],
      ),
    );
  }
}
