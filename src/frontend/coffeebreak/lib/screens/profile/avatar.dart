import 'package:coffeebreak/screens/profile/edit.dart';
import 'package:coffeebreak/utils/utils.dart';
import 'package:flutter/material.dart';
import 'package:coffeebreak/models/theme_model.dart';
import 'package:coffeebreak/layouts/layout.dart';
import 'package:provider/provider.dart';
import 'package:coffeebreak/widgets/buttons/button.dart';
import 'package:coffeebreak/widgets/avatar/avatar_card.dart';
import 'package:coffeebreak/widgets/profile_card/profile_card_edit.dart';

class EditAvatar extends StatefulWidget {
  final String avatarLink;
  EditAvatar({Key? key, required this.avatarLink}) : super(key: key);

  @override
  _EditAvatarState createState() => _EditAvatarState();
}

class _EditAvatarState extends State<EditAvatar> {
  late String _image;

  @override
  void initState() {
    super.initState();
    _image = widget.avatarLink;
  }

  @override
  Widget build(BuildContext context) {
    final theme = Provider.of<TemaModel>(context).theme;

    Future _fetch() async {
      final userId = await getUserId();
      return userId;
    }

    List<String> avatars = [
      'https://api.dicebear.com/8.x/miniavs/svg?seed=Peanut',
      'https://api.dicebear.com/8.x/miniavs/svg?seed=Annie',
      'https://api.dicebear.com/8.x/miniavs/svg?seed=Coco',
      'https://api.dicebear.com/8.x/miniavs/svg?seed=Rocky',
      'https://api.dicebear.com/8.x/miniavs/svg?seed=Oreo',
      'https://api.dicebear.com/8.x/miniavs/svg?seed=Cali',
      'https://api.dicebear.com/8.x/miniavs/svg?seed=Lily',
    ];

    return FutureBuilder(
      future: _fetch(),
      builder: (context, snapshot) {
        if (snapshot.connectionState == ConnectionState.waiting) {
          return Center(child: CircularProgressIndicator());
        } else if (snapshot.hasError) {
          return Center(
              child: Text(
                  'Erro ao carregar informações do usuário: ${snapshot.error}'));
        } else {
          final userId = snapshot.data!;
          return Layout(
            page: 'Editar avatar',
            child: Column(
              mainAxisSize: MainAxisSize.min,
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                ProfileCardEdit(
                  avatarLink: _image,
                  canEdit: false,
                ),
                SizedBox(height: 15),
                GridView.builder(
                  shrinkWrap: true,
                  physics: NeverScrollableScrollPhysics(),
                  gridDelegate: SliverGridDelegateWithMaxCrossAxisExtent(
                    maxCrossAxisExtent: MediaQuery.of(context).size.width / 5,
                    mainAxisExtent: MediaQuery.of(context).size.width / 5,
                    crossAxisSpacing: 15,
                    mainAxisSpacing: 15,
                  ),
                  itemCount: avatars.length,
                  itemBuilder: (context, index) {
                    return AvatarCard(
                      image: avatars[index],
                      onTap: (selectedImage) {
                        setState(() {
                          _image = selectedImage;
                        });
                      },
                    );
                  },
                ),
                SizedBox(height: 15),
                CustomButton(
                  alt: 'Botão de confirmar o avatar',
                  text: 'Usar avatar',
                  textColor: Colors.white,
                  onPressed: () async => {
                    await putFetch(url: 'ceos/${userId}', body: {"foto": _image}),
                    Navigator.push(
                      context,
                      MaterialPageRoute(
                        builder: (context) => EditProfile(),
                      ),
                    ),
                  },
                  gradient: theme.secondaryButton,
                )
              ],
            ),
          );
        }
      },
    );
  }
}
