import 'package:flutter/material.dart';
import 'package:coffeebreak/widgets/news.dart';
import 'package:coffeebreak/models/theme_model.dart';
import 'package:coffeebreak/layouts/layout.dart';
import 'package:provider/provider.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';
import 'package:shared_preferences/shared_preferences.dart';
import 'package:coffeebreak/utils/utils.dart';
import 'package:coffeebreak/widgets/tabbar.dart';
import 'package:flutter_dotenv/flutter_dotenv.dart';


class News extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Layout(
      child: Column(
        children: [
        Tabbar(initialTab: 'Notícias'),
        SizedBox(height: 16),
        NewsWidget(),
        ]
      ),
    );
  }
}

class NewsWidget extends StatefulWidget {
  final int? id;
  const NewsWidget({Key? key, this.id}) : super(key: key);

  @override
  _NewsWidgetState createState() => _NewsWidgetState();
}

class _NewsWidgetState extends State<NewsWidget> {
  late Future<List<Map<String, dynamic>>> newsDataFuture;
  late Future<List<String>> macrotemas;

  @override
  void initState() {
    super.initState();
    _initializeFutures();
  }

  void _initializeFutures() async {
    try {
      List<String> macrotemasList = await _fetchMacrotema();
      setState(() {
        newsDataFuture = _fetchNewsData(macrotemasList);
      });
    } catch (error) {
      print('Erro ao inicializar futuros: $error');
    }
  }

  Future<int> getUserId() async {
    // Supondo que você tem uma função para buscar o userId
    final prefs = await SharedPreferences.getInstance();
    return prefs.getInt('userId') ?? 1000;
  }

  Future<List<String>> _fetchMacrotema() async {
    int userId = await getUserId();
    print('UserId: $userId'); // Aqui você imprime o userId
    final String baseUrl = dotenv.env['BASE_URL'] ?? 'http://0.0.0.0';
    final response = await http.get(Uri.parse('$baseUrl/projetos/macrotemas/ceo/$userId'));
    if (response.statusCode == 200) {
      final data = jsonDecode(response.body);
      List<String> macrotemas = [];
      for (var macrotema in data['macrotemas']) {
        macrotemas.add(macrotema['nome']);
      }
      print('Macrotemas aqui: ');
      print(macrotemas);
      macrotemas = macrotemas.toSet().toList();
      return macrotemas;
    } else {
      throw Exception('Failed to load macrotemas');
    }
  }

  Future<List<Map<String, dynamic>>> _fetchNewsData(List<String> macrotemasList) async {
    int userId = await getUserId();
    print('UserId: $userId');
    List<Map<String, dynamic>> resultList = [];
    for (String macrotema in macrotemasList) {
      final String baseUrl = dotenv.env['BASE_URL'] ?? 'http://0.0.0.0';
      final response = await http.get(Uri.parse('$baseUrl/noticias/$macrotema'));
      if (response.statusCode == 200) {
        final data = json.decode(response.body);
        if (data['data'] != null && data['data'] is List) {
          resultList.addAll(List<Map<String, dynamic>>.from(data['data']));
        } else {
          throw Exception('A resposta não contém uma lista válida de artigos');
        }
      } else {
        throw Exception('Falha ao carregar dados: ${response.statusCode}');
      }
    }
    return resultList;
  }

  @override
  Widget build(BuildContext context) {
    return FutureBuilder<List<Map<String, dynamic>>>(
      future: newsDataFuture,
      builder: (context, snapshot) {
        if (snapshot.connectionState == ConnectionState.waiting) {
          return const Center(child: CircularProgressIndicator());
        } else if (snapshot.hasError) {
          return Center(child: Text('Erro: ${snapshot.error}'));
        } else if (!snapshot.hasData || snapshot.data!.isEmpty) {
          return const Center(child: Text('Nenhuma notícia disponível'));
        } else {
          final newsList = snapshot.data!;
          return SizedBox(
            height: MediaQuery.of(context).size.height,
            child: ListView.builder(
              itemCount: newsList.length,
              itemBuilder: (context, index) {
                final newsItem = newsList[index];
                final portal = newsItem['source']['name'] ?? '';
                final news = newsItem['description'] ?? '';
                final link = newsItem['url'] ?? '';
                final image = newsItem['urlToImage'] ?? '';
                return NewsCard(
                  portal: portal,
                  news: news,
                  link: link,
                  image: image,
                );
              },
            ),
          );
        }
      },
    );
  }
}
