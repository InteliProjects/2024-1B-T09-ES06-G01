import 'package:coffeebreak/custom/text_styles.dart';
import 'package:coffeebreak/models/project_informations.dart';
import 'package:coffeebreak/screens/create_project/summary.dart';
import 'package:flutter/material.dart';
import 'package:coffeebreak/models/theme_model.dart';
import 'package:coffeebreak/layouts/layout.dart';
import 'package:flutter/widgets.dart';
import 'package:provider/provider.dart';
import 'package:coffeebreak/widgets/inputs/input.dart';
import 'package:coffeebreak/widgets/buttons/next.dart';
import 'package:coffeebreak/widgets/inputs/text_area.dart';
import 'package:coffeebreak/widgets/profile_card/profile_card.dart';
import 'package:coffeebreak/widgets/profile_card/profile_card_edit.dart';
import 'package:coffeebreak/widgets/buttons/button.dart';
import 'package:coffeebreak/screens/finished.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';
import 'package:flutter_dotenv/flutter_dotenv.dart';


class EditDetail extends StatefulWidget {
  EditDetail({
    Key? key,
    required this.ceoId,
    required this.title,
    required this.description,
    required this.id,
  }) : super(key: key);

  final int id;
  final int ceoId;
  final String title;
  final String description;

  @override
  _EditDetailState createState() => _EditDetailState();
}

class _EditDetailState extends State<EditDetail> {
  late String title;
  late String description;

  @override
  void initState() {
  super.initState();
  title = widget.title.isNotEmpty ? widget.title : 'Título Padrão';
  description = widget.description.isNotEmpty ? widget.description : 'Descrição Padrão';
}


  Future<void> updateProject() async {
    final String baseUrl = dotenv.env['BASE_URL'] ?? 'http://0.0.0.0';
    final url = Uri.parse('$baseUrl/projetos/${widget.id}');

    final response = await http.put(
      url,
      headers: <String, String>{
        'Content-Type': 'application/json; charset=UTF-8',
      },
      body: jsonEncode(<String, dynamic>{
        'nome': title,
        'descricao': description,
      }),
    );

    if (response.statusCode == 200) {
      Navigator.pop(context);  // Volta para a tela anterior
    } else {
      // Handle the error accordingly
      print('Failed to update project.');
    }
  }

  @override
  Widget build(BuildContext context) {
    final theme = Provider.of<TemaModel>(context).theme;

    return Layout(
      page: 'Detalhamento',
      child: Column(
        children: [
          Column(
            mainAxisSize: MainAxisSize.min,
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              SizedBox(height: 15),
              Text(
                'Titulo',
                style: CoffebreakTextStyle.input.copyWith(color: theme.input),
              ),
              SizedBox(height: 5),
              Input(
                alt: 'Campo de entrada para o título',
                onChanged: (value) {
                  setState(() {
                    title = value;
                  });
                },
                labelText: '',
                initialValue: title,
              ),
              SizedBox(height: 15),
              Text(
                'Descrição',
                style: CoffebreakTextStyle.input.copyWith(color: theme.input),
              ),
              SizedBox(height: 5),
              Input(
                alt: 'Campo de entrada para a descrição',
                onChanged: (value) {
                  setState(() {
                    description = value;
                  });
                },
                labelText: '',
                initialValue: description,
              ),
              SizedBox(height: 20),
              CustomButton(
                alt: 'Botão de confirmar',
                text: "Confirmar",
                textColor: Colors.white,
                gradient: theme.secondaryButton,
                height: 55,
                onPressed: () {
                  updateProject();
                },
              ),
            ],
          ),
        ],
      ),
    );
  }
}
