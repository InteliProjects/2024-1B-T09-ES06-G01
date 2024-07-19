import 'dart:convert';

import 'package:coffeebreak/models/ceo.dart';
import 'package:coffeebreak/utils/utils.dart';
import 'package:coffeebreak/widgets/project.dart';
import 'package:flutter/material.dart';
import 'package:coffeebreak/models/theme_model.dart';
import 'package:coffeebreak/layouts/layout.dart';
import 'package:provider/provider.dart';

class Macrotheme extends StatelessWidget {
  const Macrotheme({Key? key});

  @override
  Widget build(BuildContext context) {
    final arguments =
        ModalRoute.of(context)?.settings.arguments as Map<String, String>?;
    final text = arguments?['text'] ?? '';
    final macrotheme = arguments?['macrotheme'] ?? '';

    Future _fetchProjects() async {
      final response =
          await getFetch(url: 'projetos/macrotema?nome=${macrotheme}');
      if (response.isNotEmpty) {
        final manipulatedData = response.map<Project>((project) {
          final ceos = project['ceos'];

          return Project(
            id: project['id'],
            description: project['descricao'],
            ceoId: project['ceo_id'],
            macrotheme: project['macrotema_nome'] ?? 'diversidade',
            subtheme: project['subtema_nome'] ?? 'diversidade',
            title: project['nome'],
            ceos: ceos.map<Ceo>(
              (ceo) {
                return Ceo(
                  id: ceo['id'],
                  name: ceo['nome'],
                  enterprise: ceo['empresa_nome'],
                  image: ceo['foto'],
                );
              },
            ).toList(),
          );
        }).toList();

        return manipulatedData;
      }
    }

    final theme = Provider.of<TemaModel>(context).theme;

    return Layout(
      page: text,
      child: FutureBuilder(
        future: _fetchProjects(),
        builder: (context, snapshot) {
          if (snapshot.connectionState == ConnectionState.waiting) {
            return Center(child: CircularProgressIndicator());
          } else if (snapshot.hasError) {
            return Center(child: Text('Error: ${snapshot.error}'));
          } else if (!snapshot.hasData || snapshot.data.isEmpty) {
            return Center(child: Text('No data available'));
          } else {
            final projects = snapshot.data
                as List<Project>; // Assuming your data is a list of Projects

            return Column(children: [
              ..._buildProjectList(snapshot.data!),
            ]);
          }
        },
      ),
    );
  }

  List<Widget> _buildProjectList(List<Project> projects) {
    List<Widget> projectWidgets = [];
    for (var project in projects) {
      projectWidgets.add(project);
      projectWidgets.add(const SizedBox(height: 45));
    }
    return projectWidgets;
  }
}
