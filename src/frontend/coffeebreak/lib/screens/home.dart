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


class Home extends StatelessWidget {
  const Home({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return FutureBuilder<List<Project>>(
      future: _getRecomendacao(),
      builder: (context, snapshot) {
        if (snapshot.connectionState == ConnectionState.waiting) {
          return Center(child: CircularProgressIndicator());
        } else if (snapshot.hasError) {
          return Center(child: Text('Erro ao recuperar projetos recomendados: ${snapshot.error}'));
        } else if (!snapshot.hasData || snapshot.data!.isEmpty) {
          return Center(child: Text('Nenhum projeto recomendado encontrado.'));
        } else {
          return Layout(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start, // Assegure alinhamento à esquerda
              children: <Widget>[
                Tabbar(initialTab: 'Explorar'),
                const SizedBox(height: 16),
                const MacrothemeGrid(navigateTo: '/macrotheme', type: 'home'),
                const SizedBox(height: 16),
                Text(
                  'Projetos indicados para você',
                  style: CoffebreakTextStyle.title,
                ),
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

  Future<List<Project>> _getRecomendacao() async {
    SharedPreferences prefs = await SharedPreferences.getInstance();
    int? userId = prefs.getInt('id');
    if (userId == null) {
      throw Exception('ID do usuário não encontrado.');
    }
    final String baseUrl = dotenv.env['BASE_URL'] ?? 'http://0.0.0.0';
    final response = await http.get(Uri.parse('$baseUrl/recomendacoes/recomendar/${userId}'));
    if (response.statusCode == 200) {
      final List<dynamic> data = json.decode(response.body);
      if (data.isNotEmpty) {
        return data.map<Project>((item) {
          final ceo = item['ceos'];
          final projeto = item['projeto'];
          return Project(
            id: projeto['id'],
            description: projeto['descricao'],
            ceoId: projeto['ceo_id'],
            macrotheme: projeto['macrotema_nome'] ?? 'diversidade',
            subtheme: projeto['subtema_nome'] ?? 'diversidade',
            // interations: interation, // Utiliza o valor da variável interation
            title: projeto['nome'],
            ceos: ceo.map<Ceo>((ceo) {
              return Ceo(
                id: ceo['id'],
                name: ceo['nome'],
                enterprise: ceo['empresa_nome'],
                image: ceo['foto'],
              );
            }).toList(),
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
