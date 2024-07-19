import 'package:shared_preferences/shared_preferences.dart';
import 'package:url_launcher/url_launcher.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';
import 'package:flutter_dotenv/flutter_dotenv.dart';


/// Abre o link especificado no navegador.
///
/// Parâmetros:
/// - `link` (String): O link para abrir no navegador.
void goTo(String link) async {
  Uri uri = Uri.parse(link);
  if (await canLaunchUrl(uri)) {
    await launchUrl(uri);
  }
}

/// Obtém o ID do usuário.
///
/// Comportamento:
/// - Retorna o ID.
/// - Retorna -1 se o ID não puder ser obtido.
Future<int> getUserId() async {
  SharedPreferences prefs = await SharedPreferences.getInstance();
  int? userId = prefs.getInt('id');
  return userId ?? -1;
}

/// Faz uma requisição GET para o serviço especificado.
///
/// Parâmetros:
/// - `url` (String): A URl da query.
Future<dynamic> getFetch({String url = ''}) async {
  final String baseUrl = dotenv.env['BASE_URL'] ?? 'http://0.0.0.0';
  final response = await http.get(Uri.parse('$baseUrl/${url}'));

  if (response.statusCode == 200) {
    return json.decode(response.body);
  }
}

/// Faz uma requisição POST para o serviço especificado.
///
/// Parâmetros:
/// - `url` (String): A URl da query.
/// - `body` (String): O objeto do body.
/// - `customFunction` (String): Função a ser executada (é obrigatório passar um parâmetro para o response.body).
Future<dynamic> postFetch({
  String url = '',
  dynamic body = const {},
  Function? customFunction,
}) async {
  final String baseUrl = dotenv.env['BASE_URL'] ?? 'http://0.0.0.0';
  final response = await http.post(
    Uri.parse('$baseUrl/${url}'),
    body: json.encode(body),
    headers: {
      'Content-Type': 'application/json',
    },
  );

  if (response.statusCode == 200) {
    if (customFunction != null) {
      customFunction(response.body);
    } else {
      return json.decode(response.body);
    }
  }
}


/// Faz uma requisição PUT para o serviço especificado.
///
/// Parâmetros:
/// - `url` (String): A URl da query.
/// - `body` (String): O objeto do body.
/// - `customFunction` (String): Função a ser executada (é obrigatório passar um parâmetro para o response.body).
Future<dynamic> putFetch({
  String url = '',
  dynamic body = const {},
  Function? customFunction,
}) async {
  final String baseUrl = dotenv.env['BASE_URL'] ?? 'http://0.0.0.0';
  final response = await http.put(
    Uri.parse('$baseUrl/${url}'),
    body: json.encode(body),
    headers: {
      'Content-Type': 'application/json',
    },
  );

  if (response.statusCode == 200) {
    if (customFunction != null) {
      customFunction(response.body);
    } else {
      return json.decode(response.body);
    }
  }
}
