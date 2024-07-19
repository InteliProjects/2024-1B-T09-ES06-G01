import 'package:coffeebreak/screens/edit.dart';
import 'package:flutter/material.dart';
import 'package:coffeebreak/layouts/layout.dart';
import 'package:coffeebreak/models/theme_model.dart';
import 'package:coffeebreak/models/ceo.dart';
import 'package:coffeebreak/widgets/project.dart';
import 'package:coffeebreak/widgets/info_card.dart'; // Importação do widget Description
import 'package:provider/provider.dart';
import 'package:coffeebreak/widgets/buttons/button.dart';
import 'dart:convert';
import 'package:shared_preferences/shared_preferences.dart';

class ProjectDetails extends StatelessWidget {
  final String title;
  final String description;
  final int id;
  final int ceoId;
  final List<Ceo> ceos;
  final String subtheme;
  final String macrotheme;

  const ProjectDetails({super.key, required this.title, required this.description, required this.ceoId, required this.subtheme, required this.macrotheme, required this.ceos, required this.id});

  @override
  Widget build(BuildContext context) {
    final theme = Provider.of<TemaModel>(context).theme;


    // Dados Mockados do Projeto específico para detalhamento
    final project = Project(
      id: id,
      ceoId: ceoId,
      description: description,
      macrotheme: macrotheme,
      subtheme: subtheme,
      interations: true, // Aqui interações devem ser ativadas como pedido
      title: title,
      ceos: ceos,
    );

    // Descrição detalhada do projeto
    final projectDescription  = description;

    // Use o macrotheme do projeto para obter o gradiente
    final projectMacrotheme = project.macrotheme;
    

    return FutureBuilder<int>(
      future: _getUserId(),
      builder: (context, snapshot) {
        if (snapshot.connectionState == ConnectionState.waiting) {
          return CircularProgressIndicator();
        } else if (snapshot.hasError) {
          return Text('Erro ao recuperar ID do usuário: ${snapshot.error}');
        } else {
          final userId = snapshot.data!;
          final editScreen = ceoId == userId ? EditDetail(ceoId: ceoId, description: description, title: title, id: userId,) : null;
          
          return Layout(
            page: 'Projeto',
            editScreen: editScreen,
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                project, // Inserir o widget Project já configurado
                SizedBox(height: 20), // Espaçamento entre os widgets
                InfoCard(title: 'Descrição', description: projectDescription),
                SizedBox(height: 20),
                CustomButton(
                  alt: 'Botão de solicitar sinergia',
                  text: "Solicitar Sinergia",
                  textColor: Colors.white,
                  gradient: theme.getGradienteCategoria(projectMacrotheme),
                  onPressed: () =>
                      Navigator.of(context).pushNamed("/select-synergy-type"),
                ),
              ],
            ),
          );
        }
      },
    );
  }

  Future<int> _getUserId() async {
    SharedPreferences prefs = await SharedPreferences.getInstance();
    int? userId = prefs.getInt('id');
    return userId ?? -1; // Retorna -1 se o ID não puder ser recuperado
  }
}
