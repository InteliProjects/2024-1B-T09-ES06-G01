import 'package:coffeebreak/models/theme_model.dart';
import 'package:coffeebreak/custom/text_styles.dart';
import 'package:coffeebreak/widgets/buttons/back.dart';
import 'package:coffeebreak/widgets/header.dart';
import 'package:coffeebreak/widgets/navbar.dart';
import 'package:provider/provider.dart';
import 'package:flutter/material.dart';
import 'package:flutter_svg/flutter_svg.dart';

class Layout extends StatelessWidget {
  final Widget child;
  final String? page;
  final Widget? editScreen;
  final dynamic backScreen;

  const Layout({
    Key? key,
    required this.child,
    this.page,
    this.editScreen,
    this.backScreen,
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    final theme = Provider.of<TemaModel>(context).theme;

    return Scaffold(
      backgroundColor: theme.primaryBackground,
      body: SingleChildScrollView(
        child: Column(
          children: [
            SizedBox(height: 42),
            Header(),
            Padding(
              padding: EdgeInsets.symmetric(vertical: 12, horizontal: 16),
              child: Column(
                children: [
                  if (page != null) ...[
                    SizedBox(height: 11),
                    Row(
                      children: [
                        BackButtonWidget(backScreen: backScreen),
                        SizedBox(width: 20),
                        Expanded(
                          child: Row(
                            mainAxisAlignment: MainAxisAlignment.spaceBetween,
                            children: [
                              Flexible(
                                child: Text(
                                  page!,
                                  style: CoffebreakTextStyle.title.copyWith(color: theme.primaryText),
                                  softWrap: true,
                                  overflow: TextOverflow.visible,
                                ),
                              ),
                              if (editScreen != null)
                                GestureDetector(
                                  onTap: () {
                                    Navigator.push(
                                      context,
                                      MaterialPageRoute(
                                        builder: (context) => editScreen!,
                                      ),
                                    );
                                  },
                                  child: SvgPicture.asset(
                                    'assets/icons/pencil.svg',
                                    height: 18,
                                    width: 18,
                                    colorFilter: const ColorFilter.mode(
                                      Color.fromARGB(255, 0, 0, 0),
                                      BlendMode.srcIn,
                                    ),
                                  ),
                                ),
                            ],
                          ),
                        ),
                      ],
                    ),
                    SizedBox(height: 23),
                  ],
                  child,
                ],
              ),
            ),
          ],
        ),
      ),
      bottomNavigationBar: const BottomNavigationBarExample(),
    );
  }
}
