// import 'package:coffeebreak/layouts/layout.dart';
// import 'package:coffeebreak/models/ceo.dart';
// import 'package:coffeebreak/widgets/buttons/add_project.dart';
// import 'package:coffeebreak/widgets/macrotheme_grid.dart';
// import 'package:coffeebreak/widgets/project.dart';
// import 'package:flutter/material.dart';
// import 'package:provider/provider.dart';

// final projects = [
//   Project(
//     id: 1001,
//     ceoId: 1001,
//     description: 'aaa',
//     macrotheme: 'conservação',
//     subtheme: 'Descarbonização',
//     interations: false,
//     title:
//         'Apoio a agenda de descarbonização na cadeia de suprimentos. Apoio a agenda de descarbonização na cadeia de suprimentos. Apoio a agenda de descarbonização na cadeia de suprimentos. Apoio a agenda de descarbonização na cadeia de suprimentos.',
//     ceos: [
//       Ceo(
//         name: 'Ana',
//         enterprise: 'Nubank',
//         image: 'https://api.dicebear.com/8.x/micah/svg?seed=Spooky',
//         id: 1001,
//       ),
//       Ceo(
//         name: 'Ana',
//         enterprise: 'Nubank',
//         image: 'https://api.dicebear.com/8.x/micah/svg?seed=Spooky',
//         id: 1001,
//       ),
//     ],
//   ),
//   Project(
//     id: 13,
//         description: 'aaa',

//     ceoId: 1001,
//     macrotheme: 'diversidade',
//     subtheme: 'Feminismo',
//     interations: false,
//     title:
//         'Apoio a agenda de descarbonização na cadeia de suprimentos. Apoio a agenda de descarbonização na cadeia de suprimentos. Apoio a agenda de descarbonização na cadeia de suprimentos. Apoio a agenda de descarbonização na cadeia de suprimentos.',
//     ceos: [
//       Ceo(
//         name: 'Ana',
//         enterprise: 'Nubank',
//         image: 'https://api.dicebear.com/8.x/micah/svg?seed=Spooky',
//         id: 1001,
//       ),
//       Ceo(
//         name: 'Ana',
//         enterprise: 'Nubank',
//         image: 'https://api.dicebear.com/8.x/micah/svg?seed=Spooky',
//         id: 1001,
//       ),
//     ],
//   ),
// ];

// class MyProjects extends StatelessWidget {
//   const MyProjects({super.key});

//   @override
//   Widget build(BuildContext context) {
//     return Layout(
//       page: 'Meus Projetos',
//       child: Column(
//         children: [
//           AddProject(),
//           SizedBox(height: 23),
//           ListView.separated(
//             shrinkWrap: true,
//             itemCount: projects.length,
//             itemBuilder: (context, index) {
//               return projects[index];
//             },
//             separatorBuilder: (context, index) => SizedBox(height: 17),
//           ),
//         ],
//       ),
//     );
//   }
// }

import 'package:coffeebreak/widgets/info_card.dart';
import 'package:coffeebreak/widgets/macrotheme_grid.dart';
import 'package:coffeebreak/widgets/tabbar.dart';
import 'package:coffeebreak/widgets/buttons/switch.dart';
import 'package:flutter/material.dart';
import 'package:coffeebreak/models/theme_model.dart';
import 'package:coffeebreak/widgets/buttons/button.dart';
import 'package:coffeebreak/layouts/layout.dart';
import 'package:font_awesome_flutter/font_awesome_flutter.dart';
import 'package:coffeebreak/models/ceo.dart';
import 'package:coffeebreak/widgets/project.dart';
import 'package:provider/provider.dart';
import 'package:coffeebreak/widgets/buttons/back.dart';
import 'package:coffeebreak/custom/text_styles.dart';
import 'package:shared_preferences/shared_preferences.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';
import 'package:flutter_dotenv/flutter_dotenv.dart';


class MyProjects extends StatelessWidget {
  const MyProjects({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return FutureBuilder<List<Project>>(
      future: _getProjetos(),
      builder: (context, snapshot) {
        if (snapshot.connectionState == ConnectionState.waiting) {
          return Center(child: CircularProgressIndicator());
        } else if (snapshot.hasError) {
          return Center(child: Text('Erro ao recuperar projetos recomendados: ${snapshot.error}'));
        } else if (!snapshot.hasData || snapshot.data!.isEmpty) {
          return Center(child: Text('Nenhum projeto recomendado encontrado.'));
        } else {
          return Layout(
            page: 'Projetos',
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start, // Assegure alinhamento à esquerda
              children: <Widget>[
                const SizedBox(height: 16),
                const MacrothemeGrid(navigateTo: '/macrotheme', type: 'home'),
                const SizedBox(height: 16),
                // Aqui, transformamos os dados em widgets Project, com espaçamento entre eles.
                ..._buildProjectList(snapshot.data!),
              ],
            ),
          );
        }
      },
    );
  }

  List<Widget> _buildProjectList(List<Project> projects) {
    List<Widget> projectWidgets = [];
    for (var project in projects) {
      projectWidgets.add(project);
      projectWidgets.add(const SizedBox(height: 40));
    }
    return projectWidgets;
  }

  Future<List<Project>> _getProjetos() async {
    SharedPreferences prefs = await SharedPreferences.getInstance();
    int? userId = prefs.getInt('id');
    if (userId == null) {
      throw Exception('ID do usuário não encontrado.');
    }
    final String baseUrl = dotenv.env['BASE_URL'] ?? 'http://0.0.0.0';
    final response = await http.get(Uri.parse('$baseUrl/projetos/ceo/${userId}'));
    if (response.statusCode == 200) {
      final List<dynamic> data = json.decode(response.body);
      if (data.isNotEmpty) {
        return data.map<Project>((item) {
          final ceo = item['ceos'][0];
          final projeto = item['projeto'];

          var interation = projeto['estado'] ?? 'Desconhecido';
          if (interation == 'Desconhecido') {
            interation = false; // Define como false se for 'Desconhecido'
          }

          return Project(
            id: item['id'],
            description: projeto['descricao'],
            ceoId: projeto['ceo_id'],
            macrotheme: projeto['macrotema_nome'] ?? 'diversidade',
            subtheme: projeto['subtema_nome'] ?? 'diversidade',
            interations: interation, // Utiliza o valor da variável interation
            title: projeto['nome'],
            ceos: [
              Ceo(
                id: ceo['id'],
                name: ceo['nome'],
                enterprise: ceo['empresa_nome'],
                image: ceo['foto'],
              )
            ],
          );
        }).toList();
      } else {
        throw Exception('A resposta não contém uma lista válida de projetos');
      }
    } else {
      throw Exception('Falha ao carregar dados: ${response.statusCode}');
    }
  }
}
