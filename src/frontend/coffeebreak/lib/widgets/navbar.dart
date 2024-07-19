import 'package:coffeebreak/custom/themes.dart';
import 'package:coffeebreak/models/theme_model.dart';
import 'package:coffeebreak/utils/utils.dart';
import 'package:flutter/material.dart';
import 'package:coffeebreak/screens/home.dart';
import 'package:coffeebreak/screens/profile/index.dart';
import 'package:coffeebreak/screens/search.dart';
import 'package:provider/provider.dart';

/// Este widget representa uma barra de navegação inferior com três itens:
/// Home, Search e Profile. A navegação entre as telas é gerenciada pelo estado do widget.
///
/// Propriedades:
/// - `_selectedIndex` (int): Índice do item atualmente selecionado na barra de navegação.
///
/// Comportamento:
/// - Ao clicar em um item da barra de navegação, o índice selecionado é atualizado e a navegação para a tela correspondente ocorre.
/// - A navegação é gerenciada usando `Navigator.pushReplacement` para garantir que apenas uma instância de cada tela seja criada.
///
/// Métodos:
/// - `_onItemTapped(int index)`: Atualiza o índice selecionado e realiza a navegação para a tela correspondente.
/// - `_getPage(String routeName)`: Retorna o widget da tela correspondente ao nome da rota.
class BottomNavigationBarExample extends StatefulWidget {
  const BottomNavigationBarExample({super.key});

  @override
  State<BottomNavigationBarExample> createState() =>
      _BottomNavigationBarExampleState();
}

class _BottomNavigationBarExampleState
    extends State<BottomNavigationBarExample> {
  int _selectedIndex = 0;

  void _onItemTapped(int index) async {
    final userId = await getUserId();

    setState(() {
      _selectedIndex = index;
    });

    var routeName = '/';
    switch (index) {
      case 0:
        routeName = '/home';
        break;
      case 1:
        routeName = '/search';
        break;
      case 2:
        routeName = '/profile';
        break;
    }

    Navigator.of(context).pushReplacement(
      PageRouteBuilder(
        pageBuilder: (_, __, ___) => _getPage(routeName, userId),
        transitionDuration: Duration(seconds: 0),
      ),
    );
  }

  Widget _getPage(String routeName, int userId) {
    switch (routeName) {
      case '/home':
        return Home();
      case '/search':
        return Search();
      case '/profile':
        return Profile(
          id: userId,
        );
      default:
        return Home();
    }
  }

  @override
  Widget build(BuildContext context) {
    final theme = Provider.of<TemaModel>(context).theme;

    return Semantics(
      label: 'Barra de navegação',
      child: BottomNavigationBar(
        items: const <BottomNavigationBarItem>[
          BottomNavigationBarItem(
            icon: Icon(Icons.home),
            label: '',
          ),
          BottomNavigationBarItem(
            icon: Icon(Icons.search),
            label: '',
          ),
          BottomNavigationBarItem(
            icon: Icon(Icons.person),
            label: '',
          ),
        ],
        currentIndex: _selectedIndex,
        selectedItemColor: theme.icon,
        backgroundColor: theme.primaryBackground,
        elevation: 0,
        onTap: _onItemTapped,
        iconSize: 40, // Tamanho aumentado dos ícones
      ),
    );
  }
}
