// import 'package:coffeebreak/layouts/layout.dart';
// import 'package:coffeebreak/models/ceo.dart';
// import 'package:coffeebreak/utils/utils.dart';
// import 'package:coffeebreak/widgets/buttons/add_project.dart';
// import 'package:coffeebreak/widgets/macrotheme_grid.dart';
// import 'package:coffeebreak/widgets/project.dart';
// import 'package:flutter/material.dart';
// import 'package:provider/provider.dart';

// class Projects extends StatelessWidget {
//   final int id;
//   bool isOwn = false;

//   Projects({super.key, required this.id});

//   Future<List<Map<String, dynamic>>> fetch() async {
//     final userId = await getUserId();
//     isOwn = id == userId;
//     final response = await getFetch(url: 'projetos/ceo/$id');
//     final responseUpdated = response.map<Map<String, dynamic>>((projectJson) {
//       final ceos = (projectJson['ceos'] as List).map((ceoJson) {
//         return Ceo.fromJson(ceoJson);
//       }).toList();

//       return {
//         ...projectJson,
//         'ceos': ceos,
//       };
//     }).toList();
//     return responseUpdated;
//   }

//   @override
//   Widget build(BuildContext context) {
//     return FutureBuilder<List<Map<String, dynamic>>>(
//       future: fetch(),
//       builder: (context, snapshot) {
//         if (snapshot.connectionState == ConnectionState.waiting) {
//           return Center(child: CircularProgressIndicator());
//         } else if (snapshot.hasError) {
//           return Center(
//               child: Text(
//                   'Erro ao carregar informações do usuário: ${snapshot.error}'));
//         } else if (snapshot.hasData) {
//           final projects = snapshot.data!;

//           return Layout(
//             page: isOwn ? 'Meus Projetos' : 'Projetos',
//             child: SingleChildScrollView(
//               child: Column(
//                 children: [
//                   if (isOwn) AddProject(),
//                   SizedBox(height: 23),
//                   ListView.separated(
//                     physics: NeverScrollableScrollPhysics(),
//                     shrinkWrap: true,
//                     itemCount: projects.length,
//                     itemBuilder: (context, index) {
//                       // Debug prints
//                       print('Description: ${projects[index]['descricao']}');
//                       print('State: ${projects[index]['estado']}');

//                       return Project(
//                         id: projects[index]["id"],
//                         description: 'a',
//                         ceoId: id,
//                         macrotheme: 'diversidade',
//                         subtheme: projects[index]["subtema_nome"],
//                         interations: projects[index]['estado'],
//                         title: projects[index]["nome"],
//                         ceos: projects[index]["ceos"],
//                       );
//                     },
//                     separatorBuilder: (context, index) => SizedBox(height: 17),
//                   ),
//                 ],
//               ),
//             ),
//           );
//         } else {
//           return Center(child: Text('Nenhum projeto encontrado.'));
//         }
//       },
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
import 'package:coffeebreak/widgets/buttons/add_project.dart';
import 'package:flutter_dotenv/flutter_dotenv.dart';



class Projects extends StatelessWidget {
  Projects({Key? key, required this.id}) : super(key: key);
  final int id;
  bool isOwn = false;

  @override
  Widget build(BuildContext context) {
    return FutureBuilder<List<Project>>(
      future: _getProjetos(),
      builder: (context, snapshot) {
        if (snapshot.connectionState == ConnectionState.waiting) {
          return Center(child: CircularProgressIndicator());
        } else if (snapshot.hasError) {
          return Center(child: Text('Erro ao recuperar projetos do CEO: ${snapshot.error}'));
        } else if (!snapshot.hasData || snapshot.data!.isEmpty) {
          return Center(child: Text('Nenhum projeto encontrado.'));
        } else {
          return Layout(
            page: 'Projetos',
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start, // Assegure alinhamento à esquerda
              children: <Widget>[
                if (isOwn) AddProject(),
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
      projectWidgets.add(const SizedBox(height: 45));
    }
    return projectWidgets;
  }

  Future<List<Project>> _getProjetos() async {
    SharedPreferences prefs = await SharedPreferences.getInstance();
    int? userId = prefs.getInt('id');
    if (userId == null) {
      throw Exception('ID do usuário não encontrado.');
    }
    isOwn = id == userId;
    final String baseUrl = dotenv.env['BASE_URL'] ?? 'http://0.0.0.0';
    final response = await http.get(Uri.parse('$baseUrl/projetos/ceo/${userId}'));
    if (response.statusCode == 200) {
      final List<dynamic> data = json.decode(response.body);
      if (data.isNotEmpty) {
        return data.map<Project>((item) {
        final ceo = item['ceos'][0];
        final projeto = item; 

        // var interation = projeto['estado'] ?? 'Desconhecido';
        // if (interation == 'Desconhecido') {
        //   interation = false; // Define como false se for 'Desconhecido'
        // }

        return Project(
          id: item['id'],
          description: projeto['descricao'],
          ceoId: projeto['ceo_id'],
          macrotheme: projeto['macrotema_nome'] ?? 'diversidade',
          subtheme: projeto['subtema_nome'] ?? 'diversidade',
          // interations: interation, // Utiliza o valor da variável interation
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
