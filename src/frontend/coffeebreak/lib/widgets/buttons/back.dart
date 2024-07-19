import 'package:coffeebreak/models/theme_model.dart';
import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

/// Este widget representa um botão para voltar à página anterior.
///
/// Parâmetros:
/// - `backScreen` (Widget?, opcional): A tela para a qual voltar quando o botão é pressionado.
///
/// Comportamento:
/// - Ao ser tocado, o usuário é direcionado para a tela anterior.
class BackButtonWidget extends StatelessWidget {
  final backScreen;

  const BackButtonWidget({
    Key? key,
    this.backScreen,
  });

  @override
  Widget build(BuildContext context) {
    final theme = Provider.of<TemaModel>(context).theme;

    return Semantics(
      label: 'Botão para voltar à página anterior',
      child: IconButton(
        padding: EdgeInsets.zero,
        constraints: BoxConstraints(),
        icon: Container(
          width: 14,
          child: Icon(
            Icons.arrow_back_ios,
            size: 25,
            color: theme.primaryText,
          ),
        ),
        onPressed: () {
          if (backScreen != null)
            Navigator.push(
              context,
              MaterialPageRoute(
                builder: (context) => backScreen,
              ),
            );
          else
            Navigator.of(context).pop();
        },
      ),
    );
  }
}
