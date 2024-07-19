import 'package:flutter/material.dart';
import 'package:coffeebreak/models/theme_model.dart';
import 'package:provider/provider.dart';
import 'package:coffeebreak/custom/text_styles.dart';

/// Este widget exibe uma barra de navegação com abas para explorar e notícias.
///
/// Comportamento:
/// - Navega entre duas telas: "Explorar" e "Notícias".
/// - Mantém o estado da aba selecionada.
/// - Aplica uma indicação visual na aba selecionada.
class Tabbar extends StatefulWidget {
  final String initialTab;

  const Tabbar({Key? key, required this.initialTab}) : super(key: key);

  @override
  State<Tabbar> createState() => _TabbarState();
}

class _TabbarState extends State<Tabbar> {
  late int _selectedIndex;

  @override
  void initState() {
    super.initState();
    // Define a aba inicial com base no valor de initialTab
    _selectedIndex = widget.initialTab == 'Explorar' ? 0 : 1;
  }

  void _onItemTapped(int index) {
    setState(() {
      _selectedIndex = index;
    });
    switch (index) {
      case 0:
        Navigator.of(context).pushReplacementNamed('/home'); // Navega para a Home
        break;
      case 1:
        Navigator.of(context).pushReplacementNamed('/news'); // Navega para Notícias
        break;
    }
  }

  @override
  Widget build(BuildContext context) {
    return Semantics(
      label: 'Barra de navegação para explorar e notícias',
      child: DefaultTabController(
        length: 2,
        initialIndex: _selectedIndex,
        child: LayoutBuilder(
          builder: (BuildContext context, BoxConstraints constraints) {
            final theme = Provider.of<TemaModel>(context).theme;

            double indicatorWidth = constraints.maxWidth / 2;
            return Column(
              children: [
                Container(
                  child: TabBar(
                    tabs: [
                      Tab(text: "Explorar"),
                      Tab(text: "Notícias"),
                    ],
                    labelColor: theme.primaryText,
                    onTap: _onItemTapped,
                    unselectedLabelColor: theme.primaryText,
                    labelStyle: CoffebreakTextStyle.activeAuxiliary,
                    unselectedLabelStyle: CoffebreakTextStyle.button,
                    indicator: UnderlineTabIndicator(
                      borderSide: BorderSide(color: Color(0xFF2F8B82), width: 3),
                      insets: EdgeInsets.symmetric(horizontal: indicatorWidth / 2),
                    ),
                  ),
                ),
              ],
            );
          },
        ),
      ),
    );
  }
}
