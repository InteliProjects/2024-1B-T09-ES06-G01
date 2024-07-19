import 'package:coffeebreak/models/theme_model.dart';
import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
// Corrija o caminho conforme necessário

/// Este widget representa o cabeçalho da aplicação, incluindo um logotipo e um ícone de notificação.
/// Ele é construído utilizando um `Row` dentro de um `Container` com padding e decoração.
///
/// Propriedades:
/// - `theme` (TemaModel): Define as cores e estilos utilizados no cabeçalho, obtido a partir do `Provider`.
///
/// Estrutura:
/// - O logotipo é exibido à esquerda e ajusta conforme o tema claro ou escuro.
/// - O ícone de notificação é exibido à direita, com cor e tamanho personalizados.
/// - O contêiner tem uma linha na parte inferior para separar o cabeçalho do conteúdo.
///
/// Comportamento:
/// - Ao pressionar o ícone de notificação, o usuário é redirecionado para a tela de notificações.
class Header extends StatelessWidget {
  const Header({super.key});

  @override
  Widget build(BuildContext context) {
    final theme = Provider.of<TemaModel>(context).theme;

    return Semantics(
      label: 'Cabeçalho',
      child: Container(
        padding: const EdgeInsets.symmetric(horizontal: 20, vertical: 10),
        decoration: BoxDecoration(
            color: theme.primaryBackground,
            border: Border(
                bottom: BorderSide(
                    color: theme.outline, width: 2) // Linha na parte inferior
                )),
        child: Row(
          mainAxisAlignment: MainAxisAlignment.spaceBetween,
          children: [
            Image.asset(
              Theme.of(context).brightness == Brightness.light
                  ? theme.darkLogo
                  : theme.lightLogo,
              height: 40, // Ajuste conforme necessário
            ),
            IconButton(
              icon: const Icon(Icons.notifications),
              color: theme.icon,
              onPressed: () => Navigator.of(context).pushNamed("/notification"),
              iconSize: 30, // Aumentar o tamanho do ícone
            ),
          ],
        ),
      ),
    );
  }
}
