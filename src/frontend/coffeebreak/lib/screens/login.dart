import 'dart:convert';
import 'package:coffeebreak/layouts/layout.dart';
import 'package:coffeebreak/models/theme_model.dart';
import 'package:coffeebreak/custom/text_styles.dart';
import 'package:coffeebreak/utils/utils.dart';
import 'package:coffeebreak/widgets/buttons/button.dart';
import 'package:flutter/material.dart';
import 'package:coffeebreak/widgets/inputs/input.dart';
import 'package:http/http.dart' as http;
import 'package:provider/provider.dart';
import 'package:shared_preferences/shared_preferences.dart';

class Login extends StatelessWidget {
  const Login({super.key});

  Future<void> login(String email, String password, BuildContext context) async {
    void func(String responseBody) async {
      final int? id = jsonDecode(responseBody)['id'];
      if (id != null) {
        final SharedPreferences user = await SharedPreferences.getInstance();
        user.setInt('id', id);
        Navigator.of(context).pushNamed("/home");
      }
    }

    await postFetch(
      url: 'ceos/login',
      body: {"email": email, "senha": password},
      customFunction: func
    );
  }

  @override
  Widget build(BuildContext context) {
    final theme = Provider.of<TemaModel>(context).theme;

    String email = '';
    String password = '';

    return MaterialApp(
      home: Scaffold(
        backgroundColor: theme.primaryBackground,
        body: Padding(
          padding: const EdgeInsets.all(16.0),
          child: Center(
            child: Column(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                Text(
                  'Seja bem-vindo!',
                  style: CoffebreakTextStyle.title.copyWith(color: theme.primaryText),
                  textAlign: TextAlign.center,
                ),
                SizedBox(height: 20),
                Input(
                  icon: Icons.person,
                  labelText: 'Email',
                  onChanged: (value) => email = value,
                ),
                SizedBox(height: 20),
                Input(
                  icon: Icons.lock,
                  labelText: 'Senha',
                  onChanged: (value) => password = value,
                  isPassword: true,  // Indicate this field is for the password
                ),
                SizedBox(height: 20),
                GestureDetector(
                  onTap: () {},  // Add functionality for password recovery
                  child: Align(
                    alignment: Alignment.centerRight,
                    child: Text(
                      'Esqueceu a senha?!',
                      style: CoffebreakTextStyle.auxiliary.copyWith(
                        color: theme.secondaryButton.colors[0],
                        fontWeight: FontWeight.bold,
                      ),
                      textAlign: TextAlign.right,
                    ),
                  ),
                ),
                SizedBox(height: 20),
                CustomButton(
                  text: "Entrar",
                  textColor: Colors.white,
                  gradient: theme.secondaryButton,
                  onPressed: () => login(email, password, context),
                ),
                SizedBox(height: 20),
Row(
                  mainAxisAlignment: MainAxisAlignment.center,
                  children: [
                    Expanded(
                      child: Container(
                        height: 1,
                        color: theme.secondaryText,
                      ),
                    ),
                    Padding(
                      padding: const EdgeInsets.symmetric(horizontal: 8),
                      child: Text(
                        'OU',
                        style: TextStyle(
                          color: theme.secondaryText,
                          fontSize: 16,
                        ),
                      ),
                    ),
                    Expanded(
                      child: Container(
                        height: 1,
                        color: theme.secondaryText,
                      ),
                    ),
                  ],
                ),
                SizedBox(height: 20),
                CustomButton(
                  text: "Entrar com Google",
                  backgroundColor: theme.primaryButton,
                  textColor: theme.input,
                  onPressed: () => Navigator.of(context).pushNamed("/googleLogin"),
                ),
                SizedBox(height: 20),
                RichText(
                  text: TextSpan(
                    style: CoffebreakTextStyle.auxiliary.copyWith(color: theme.primaryText),
                    children: [
                      const TextSpan(text: 'Não tem uma conta? '),
                      TextSpan(
                        text: 'Solicitar cadastro',
                        style: TextStyle(color: theme.secondaryButton.colors[0]),
                      ),
                    ],
                  ),
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }
}
