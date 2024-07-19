import 'package:coffeebreak/custom/text_styles.dart';
import 'package:coffeebreak/models/project_informations.dart';
import 'package:coffeebreak/screens/finished.dart';
import 'package:coffeebreak/screens/profile/index.dart';
import 'package:coffeebreak/utils/utils.dart';
import 'package:coffeebreak/widgets/info_card.dart';
import 'package:coffeebreak/widgets/inputs/input.dart';
import 'package:coffeebreak/widgets/profile_card/profile_card.dart';
import 'package:coffeebreak/widgets/inputs/text_area.dart';
import 'package:coffeebreak/widgets/profile_card/profile_card_edit.dart';
import 'package:flutter/material.dart';
import 'package:coffeebreak/models/theme_model.dart';
import 'package:coffeebreak/layouts/layout.dart';
import 'package:font_awesome_flutter/font_awesome_flutter.dart';
import 'package:provider/provider.dart';
import 'package:coffeebreak/widgets/buttons/button.dart';

class EditProfile extends StatelessWidget {
  late int userId;
  String name = '';
  String biography = '';
  String role = '';
  String enterprise = '';

  EditProfile({Key? key});

  Future _fetch() async {
    userId = await getUserId();
    final response = getFetch(url: 'ceos/${userId}');
    return response;
  }

  @override
  Widget build(BuildContext context) {
    final theme = Provider.of<TemaModel>(context).theme;

    return FutureBuilder(
      future: _fetch(),
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
            page: 'Editar perfil',
            child: Column(
              mainAxisSize: MainAxisSize.min,
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                ProfileCardEdit(
                  avatarLink: userData["foto"],
                  canEdit: true,
                ),
                SizedBox(height: 15),
                Text(
                  'Nome',
                  style: CoffebreakTextStyle.input.copyWith(color: theme.input),
                ),
                SizedBox(height: 5),
                Input(
                  initialValue: userData["nome"],
                  alt: 'Campo de entrada para o nome',
                  onChanged: (value) {
                    name = value;
                  },
                  labelText: '',
                ),
                SizedBox(height: 15),
                Text(
                  'Cargo',
                  style: CoffebreakTextStyle.input.copyWith(color: theme.input),
                ),
                SizedBox(height: 5),
                Input(
                  initialValue: userData["cargo"],
                  alt: 'Campo de entrada para o cargo',
                  onChanged: (value) {
                    role = value;
                  },
                  labelText: '',
                ),
                SizedBox(height: 15),
                Text(
                  'Empresa',
                  style: CoffebreakTextStyle.input.copyWith(color: theme.input),
                ),
                SizedBox(height: 5),
                Input(
                  initialValue: userData["empresa_nome"],
                  alt: 'Campo de entrada para a empresa',
                  onChanged: (value) {
                    enterprise = value;
                  },
                  labelText: '',
                ),
                SizedBox(height: 15),
                Text(
                  'Sobre',
                  style: CoffebreakTextStyle.input.copyWith(color: theme.input),
                ),
                SizedBox(height: 5),
                TextArea(
                  initialValue: userData["biografia"],
                  alt: 'Campo de entrada para o texto sobre você',
                  maxLength: 500,
                  minLines: 5,
                  onChanged: (value) {
                    biography = value;
                  },
                ),
                SizedBox(height: 15),
                CustomButton(
                  alt: 'Botão de confirmar a edição',
                  text: 'Editar',
                  textColor: Colors.white,
                  onPressed: () async => {
                    await putFetch(url: 'ceos/${userId}', body: {
                      "nome": name != '' ? name : userData["nome"],
                      "biografia":
                          biography != '' ? biography : userData["biografia"],
                      "cargo": role != '' ? role : userData["cargo"],
                      "empresa_nome": enterprise != ''
                          ? enterprise
                          : userData["empresa_nome"],
                    }),
                    Navigator.push(
                      context,
                      MaterialPageRoute(
                        builder: (context) => Profile(id: userId),
                      ),
                    ),
                  },
                  gradient: theme.secondaryButton,
                )
              ],
            ),
          );
        }
      },
    );
  }
}
