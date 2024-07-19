import 'package:coffeebreak/models/project_informations.dart';
import 'package:coffeebreak/screens/create_project/description.dart';
import 'package:coffeebreak/screens/create_project/edit.dart';
import 'package:coffeebreak/screens/edit.dart';
import 'package:coffeebreak/screens/finished.dart';
import 'package:coffeebreak/utils/utils.dart';
import 'package:coffeebreak/widgets/info_card.dart';
import 'package:flutter/material.dart';
import 'package:coffeebreak/models/theme_model.dart';
import 'package:coffeebreak/layouts/layout.dart';
import 'package:provider/provider.dart';
import 'package:coffeebreak/widgets/buttons/button.dart';

class CreateProjectSummary extends StatelessWidget {
  final ProjectInformations projectInformations;
  const CreateProjectSummary({Key? key, required this.projectInformations});

  Future fetchUserData() async {
    final userId = await getUserId();
    return userId;
  }

  @override
  Widget build(BuildContext context) {
    final theme = Provider.of<TemaModel>(context).theme;

    final title = projectInformations.title ?? '';
    final description = projectInformations.description ?? '';

    return FutureBuilder(
      future: fetchUserData(),
      builder: (context, snapshot) {
        if (snapshot.connectionState == ConnectionState.waiting) {
          return Center(child: CircularProgressIndicator());
        } else if (snapshot.hasError) {
          return Center(
              child: Text(
                  'Erro ao carregar informações do usuário: ${snapshot.error}'));
        } else {
          final userId = snapshot.data!;
          return Layout(
            page: 'Resumo',
            backScreen: CreateProjectDescription(
                projectInformations: projectInformations),
            editScreen: EditProject(projectInformations: projectInformations),
            child: Column(
              children: [
                InfoCard(title: 'Título', description: title),
                SizedBox(height: 14),
                InfoCard(title: 'Descrição', description: description),
                SizedBox(height: 14),
                CustomButton(
                  alt: 'Botão de confirmar',
                  text: "Confirmar",
                  textColor: Colors.white,
                  gradient: theme.secondaryButton,
                  height: 55,
                  onPressed: () {
                    postFetch(url: 'projetos/', body: {
                      "ceo_id": userId,
                      "subtema_id": 1,
                      "nome": projectInformations.title,
                      "descricao": projectInformations.description
                    });
                    Navigator.push(
                      context,
                      MaterialPageRoute(
                        builder: (context) =>
                            Finished(type: FinishedType.createProject),
                      ),
                    );
                  },
                ),
              ],
            ),
          );
        }
      },
    );
  }
}
