import 'dart:convert';

import 'package:coffeebreak/models/ceo.dart';
import 'package:coffeebreak/utils/utils.dart';
import 'package:coffeebreak/widgets/project.dart';
import 'package:coffeebreak/widgets/inputs/input.dart';
import 'package:flutter/material.dart';
import 'package:coffeebreak/models/theme_model.dart';
import 'package:coffeebreak/layouts/layout.dart';
import 'package:provider/provider.dart';

class Search extends StatefulWidget {
  const Search({Key? key}) : super(key: key);

  @override
  _SearchState createState() => _SearchState();
}

class _SearchState extends State<Search> {
  final TextEditingController _controller = TextEditingController();
  Future<List<Project>>? _futureProjects;

  Future<List<Project>> _getPesquisa(String pesquisa) async {
    final response = await getFetch(url: 'projetos/busca?termo=$pesquisa');
    
    if (response != null && response.isNotEmpty) {
      final manipulatedData = response.map<Project>((project) {
        final ceos = project['ceos'];
        return Project(
          id: project['id'],
          description: project['descricao'],
          ceoId: project['ceo_id'],
          macrotheme: project['macrotema_nome'] ?? 'diversidade',
          subtheme: project['subtema_nome'] ?? 'diversidade',
          title: project['nome'],
          ceos: ceos.map<Ceo>((ceo) {
            return Ceo(
              id: ceo['id'],
              name: ceo['nome'],
              enterprise: ceo['empresa_nome'],
              image: ceo['foto'],
            );
          }).toList(),
        );
      }).toList();

      return manipulatedData;
    } else {
      return [];
    }
  }

  @override
  Widget build(BuildContext context) {
    final arguments =
        ModalRoute.of(context)?.settings.arguments as Map<String, String>?;
    final text = arguments?['text'] ?? '';

    final theme = Provider.of<TemaModel>(context).theme;

    return Layout(
      page: text,
      child: Column(
        children: [
          Input(
            labelText: 'Pesquisar',
            controller: _controller,
            onChanged: (text) {
            },
            onSubmitted: (text) {
              setState(() {
                _futureProjects = _getPesquisa(text);
              });
            },
          ),
          SizedBox(height: 20),
          FutureBuilder<List<Project>>(
            future: _futureProjects,
            builder: (context, snapshot) {
              if (snapshot.connectionState == ConnectionState.waiting) {
                return Center(child: CircularProgressIndicator());
              } else if (snapshot.hasError) {
                return Center(child: Text('Error: ${snapshot.error}'));
              } else if (!snapshot.hasData || snapshot.data!.isEmpty) {
                return Center(child: Text('Desculpe, mas não há nada com esse nome.'));
              } else {
                final projects = snapshot.data!;

                return Column(children: [
                  ..._buildProjectList(projects),
                ]);
              }
            },
          ),
        ],
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
