import 'package:flutter/material.dart';
import 'package:coffeebreak/models/theme_model.dart';
import 'package:coffeebreak/layouts/layout.dart';
import 'package:provider/provider.dart';

class Help extends StatelessWidget {
  const Help({Key? key});

  @override
  Widget build(BuildContext context) {
    final theme = Provider.of<TemaModel>(context).theme;

    return Layout(
      page: 'Help',
      child: Text('Help'),
    );
  }
}
