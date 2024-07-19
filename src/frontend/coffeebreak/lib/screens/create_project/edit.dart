import 'package:coffeebreak/custom/text_styles.dart';
import 'package:coffeebreak/models/project_informations.dart';
import 'package:coffeebreak/screens/create_project/summary.dart';
import 'package:flutter/material.dart';
import 'package:coffeebreak/models/theme_model.dart';
import 'package:coffeebreak/layouts/layout.dart';
import 'package:provider/provider.dart';
import 'package:coffeebreak/widgets/inputs/input.dart';
import 'package:coffeebreak/widgets/buttons/next.dart';
import 'package:coffeebreak/widgets/inputs/text_area.dart';
import 'package:coffeebreak/widgets/profile_card/profile_card.dart';
import 'package:coffeebreak/widgets/profile_card/profile_card_edit.dart';
import 'package:coffeebreak/widgets/buttons/button.dart';
import 'package:coffeebreak/screens/finished.dart';



class EditProject extends StatelessWidget {
  final ProjectInformations projectInformations;
  EditProject({Key? key, required this.projectInformations}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    final theme = Provider.of<TemaModel>(context).theme;

    String title = projectInformations.title ?? '';
    String description = projectInformations.description ?? '';

    return Layout(
      page: 'Editar',
      child: Column(
        children: [
          Column(
            mainAxisSize: MainAxisSize.min,
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Text(
                'Titulo',
                style: CoffebreakTextStyle.input.copyWith(color: theme.input),
              ),
              SizedBox(height: 5),
              Input(
                alt: 'Campo de entrada para o título',
                initialValue: title,
                onChanged: (value) {
                  title = value;
                },
                labelText: '',
              ),
              SizedBox(height: 15),
              Text(
                'Descrição',
                style: CoffebreakTextStyle.input.copyWith(color: theme.input),
              ),
              SizedBox(height: 5),
              Input(
                alt: 'Campo de entrada para a descrição',
                initialValue: description,
                onChanged: (value) {
                  description = value;
                },
                labelText: '',
              ),  
              SizedBox(height: 15),
              CustomButton(
                alt: 'Botão de confirmar',
                text: "Confirmar",
                textColor: Colors.white,
                gradient: theme.secondaryButton,
                height: 55,
                onPressed: () {
                  projectInformations.title = title;
                  projectInformations.description = description;
                  Navigator.push(
                    context,
                    MaterialPageRoute(
                      builder: (context) =>
                          CreateProjectSummary(projectInformations: projectInformations),
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
