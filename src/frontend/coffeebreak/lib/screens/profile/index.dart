import 'package:coffeebreak/layouts/layout.dart';
import 'package:coffeebreak/models/theme_model.dart';
import 'package:coffeebreak/screens/projects.dart';
import 'package:coffeebreak/utils/utils.dart';
import 'package:coffeebreak/widgets/info_card.dart';
import 'package:coffeebreak/widgets/buttons/button.dart';
import 'package:coffeebreak/widgets/news.dart';
import 'package:coffeebreak/widgets/profile_card/profile_card.dart';
import 'package:coffeebreak/widgets/buttons/switch.dart';
import 'package:flutter/material.dart';
import 'package:font_awesome_flutter/font_awesome_flutter.dart';
import 'package:provider/provider.dart';
import 'dart:convert';
import 'package:http/http.dart' as http;

class Profile extends StatefulWidget {
  final int id;
  const Profile({super.key, required this.id});

  @override
  _ProfileState createState() => _ProfileState();
}

class _ProfileState extends State<Profile> {
  late Future userDataFuture;
  late int userId;
  late bool isOwn = false;

  @override
  void initState() {
    super.initState();
    userDataFuture = _fetchUserData();
  }

  Future _fetchUserData() async {
    userId = await getUserId();
    isOwn = userId == widget.id;
    final response = getFetch(url: 'ceos/${widget.id}');
    return response;
  }

  @override
  Widget build(BuildContext context) {
    final theme = Provider.of<TemaModel>(context).theme;

    return FutureBuilder(
      future: userDataFuture,
      builder: (context, snapshot) {
        if (snapshot.connectionState == ConnectionState.waiting) {
          return Center(child: CircularProgressIndicator());
        } else if (snapshot.hasError) {
          return Center(
              child: Text(
                  'Erro ao carregar informações do usuário: ${snapshot.error}'));
        } else {
          final userData = snapshot.data!;
          return Layout(
            child: Column(
              children: [
                ProfileCard(
                  isOwn: isOwn,
                  name: userData['nome'] ?? 'Nome não encontrado',
                  role: userData['cargo'] ?? 'Cargo não encontrado',
                  enterprise:
                      userData['empresa_nome'] ?? 'Empresa não encontrada',
                  projectsQuantity: userData['quantidade_projetos'] ?? 0,
                  linkedin: userData['linkedin'] ?? '',
                  email: userData['email_contato'] ?? '',
                  avatarLink: userData['foto'] ?? '',
                ),
                SizedBox(height: 10),
                InfoCard(
                  title: 'Sobre',
                  description:
                      userData['biografia'] ?? 'Descrição não encontrada',
                ),
                SizedBox(height: 10),
                if (isOwn)
                  Column(
                    children: [
                      CustomButton(
                        alt: 'Botão de projetos curtidos',
                        text: "Curtidos",
                        textColor: theme.input,
                        icon: FontAwesomeIcons.solidHeart,
                        backgroundColor: theme.primaryButton,
                        onPressed: () =>
                            Navigator.of(context).pushNamed("/liked"),
                      ),
                      SizedBox(height: 10),
                      CustomButton(
                        alt: 'Botão de projetos salvos',
                        text: "Salvos",
                        textColor: theme.input,
                        icon: FontAwesomeIcons.bookmark,
                        backgroundColor: theme.primaryButton,
                        onPressed: () =>
                            Navigator.of(context).pushNamed("/saved"),
                      ),
                      SizedBox(height: 10),
                    ],
                  ),
                CustomButton(
                  alt: isOwn
                      ? 'Botão de "Meus projetos"'
                      : 'Botão de "Projetos"',
                  text: isOwn ? "Meus projetos" : 'Projetos',
                  textColor: theme.input,
                  icon: Icons.layers_outlined,
                  backgroundColor: theme.primaryButton,
                  onPressed: () {
                    print(widget.id);  // Adiciona esta linha para printar o widget.id
                    Navigator.push(
                      context,
                      MaterialPageRoute(
                        builder: (context) => Projects(id: widget.id),
                      ),
                    );
                  },
                ),
                SizedBox(height: 10),
                if (isOwn)
                  CustomButton(
                    alt: 'Botão de configurações',
                    text: "Configurações",
                    textColor: theme.input,
                    icon: Icons.settings,
                    backgroundColor: theme.primaryButton,
                    onPressed: () =>
                        Navigator.of(context).pushNamed("/settings"),
                  ),
              ],
            ),
          );
        }
      },
    );
  }
}
