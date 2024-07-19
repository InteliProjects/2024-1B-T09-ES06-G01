import 'package:flutter/material.dart';
import 'package:coffeebreak/layouts/layout.dart';
import 'package:coffeebreak/widgets/synergy.dart';
import 'package:coffeebreak/widgets/synergy_status.dart';
import 'package:coffeebreak/widgets/synergy_status.dart';

class NotificationScreen extends StatelessWidget {
  const NotificationScreen({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Layout(
      page: 'Notificação',
      child: Column(
        children: [
          Synergy(),
          SizedBox(height: 15),
          SynergyStatus(),
        ],
      ),
    );
  }
}
