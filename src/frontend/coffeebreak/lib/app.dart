import 'package:coffeebreak/models/theme_model.dart';
import 'package:coffeebreak/screens/create_project/index.dart';
import 'package:coffeebreak/screens/help.dart';
import 'package:coffeebreak/screens/home.dart';
import 'package:coffeebreak/screens/liked.dart';
import 'package:coffeebreak/screens/macrotheme.dart';
import 'package:coffeebreak/screens/projects.dart';
import 'package:coffeebreak/screens/profile/avatar.dart';
import 'package:coffeebreak/screens/profile/edit.dart';
import 'package:coffeebreak/screens/profile/index.dart';
import 'package:coffeebreak/screens/notification.dart';
import 'package:coffeebreak/screens/saved.dart';
import 'package:coffeebreak/screens/search.dart';
import 'package:coffeebreak/screens/settings.dart';
import 'package:coffeebreak/screens/project_details.dart';
import 'package:coffeebreak/screens/splash.dart';
import 'package:coffeebreak/screens/login.dart';
import 'package:provider/provider.dart';
import 'package:flutter/material.dart';
import 'package:coffeebreak/screens/create_project/subtheme.dart';
import 'package:coffeebreak/screens/create_project/name.dart';
import 'package:coffeebreak/screens/create_project/description.dart';
import 'package:coffeebreak/screens/requestSinergy.dart';
import 'package:coffeebreak/screens/news.dart';
import 'package:coffeebreak/screens/submit_sinergy/select_synergy_type.dart';
import 'package:coffeebreak/screens/create_project/edit.dart';
import 'package:coffeebreak/screens/edit.dart';

/// Este widget é o ponto de entrada da aplicação, onde são definidas as rotas e o tema global.
///
/// Comportamento:
/// - Define o tema global da aplicação com base no `TemaModel`.
/// - Define as rotas para cada tela da aplicação.
///
/// Estrutura:
/// - Um `MaterialApp` com o título da aplicação, o tema definido e as rotas para cada tela.
class App extends StatelessWidget {
  const App({super.key});

  @override
  Widget build(BuildContext context) {
    final theme = Provider.of<TemaModel>(context).theme;
    return MaterialApp(
      title: 'Coffeebreak',
      theme: theme.themeData,
      initialRoute: '/',
      routes: {
        '/': (context) => const Splash(),
        '/login': (context) => const Login(),
        '/home': (context) => const Home(),
        '/notification': (context) => const NotificationScreen(),
        '/liked': (context) => const Liked(),
        '/saved': (context) => const Saved(),
        '/settings': (context) => const Settings(),
        '/help': (context) => const Help(),
        '/create-project': (context) => CreateProject(),
        '/request-sinergy': (context) => const RequestSinergy(),
        '/news': (context) => News(),
        '/macrotheme': (context) => const Macrotheme(),
        '/search': (context) => const Search(),
        '/select-synergy-type': (context) => const SelectSynergyType(),
      },
    );
  }
}
