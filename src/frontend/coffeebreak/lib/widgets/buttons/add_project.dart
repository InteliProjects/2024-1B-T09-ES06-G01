import 'package:coffeebreak/models/theme_model.dart';
import 'package:coffeebreak/custom/text_styles.dart';
import 'package:flutter/material.dart';
import 'package:flutter_svg/flutter_svg.dart';
import 'package:provider/provider.dart';

/// Este widget representa um botão para adicionar um novo projeto.
///
/// Estrutura:
/// - Um ícone de adição seguido pelo texto "Adicionar projeto".
///
/// Comportamento:
/// - Ao ser tocado, o usuário é direcionado para a tela de criação de projeto.
class AddProject extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    final theme = Provider.of<TemaModel>(context).theme;

    return GestureDetector(
      onTap: () => Navigator.of(context).pushNamed(
        "/create-project",
      ),
      child: Semantics(
        label: 'Botão para adicionar projeto', 
        child: Row(
        children: [
          SvgPicture.asset(
            'assets/icons/add.svg',
            height: 23,
            width: 23,
            colorFilter: ColorFilter.mode(
              theme.primaryText,
              BlendMode.srcIn,
            ),
          ),
          SizedBox(width: 13),
          Text('Adicionar projeto',
              style: CoffebreakTextStyle.project.copyWith(
                color: theme.primaryText,
              )),
        ],
      ),
      )
    );
  }
}
