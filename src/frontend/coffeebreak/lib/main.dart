import 'package:coffeebreak/app.dart';
import 'package:coffeebreak/models/theme_model.dart';
import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:flutter_dotenv/flutter_dotenv.dart';


// Função principal que inicializa o aplicativo.
void main() async {
  await dotenv.load(fileName: ".env");
  runApp(
    ChangeNotifierProvider(
      // Passa o widget App como filho do Provider para fornecer o modelo de tema para toda a árvore de widgets.
      create: (_) => TemaModel(),
      child: const App(),
    ),
  );
}
