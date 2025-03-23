import 'package:flutter/material.dart';
import 'package:sinimini_app/main.dart';
import 'movie_screen.dart';
import 'series_screen.dart';

class CreateSelectionWidget extends StatefulWidget {
  final GlobalKey<NavigatorState> navigatorKey;

  const CreateSelectionWidget({Key? key, required this.navigatorKey})
      : super(key: key);

  @override
  _CreateSelectionWidgetState createState() => _CreateSelectionWidgetState();
}

class _CreateSelectionWidgetState extends State<CreateSelectionWidget> {
  @override
  Widget build(BuildContext context) {
    return Navigator(
      key: widget.navigatorKey,
      initialRoute: 'createHome',
      onGenerateRoute: (RouteSettings settings) {
        WidgetBuilder builder;
        switch (settings.name) {
          case 'createHome':
            builder = (BuildContext _) => CreateSelectionHome();
            break;
          case 'movie':
            builder = (BuildContext _) => const MovieFormScreen();
            break;
          case 'series':
            builder = (BuildContext _) => const SeriesFormScreen();
            break;
          default:
            throw Exception('Invalid route: ${settings.name}');
        }
        return MaterialPageRoute(builder: builder, settings: settings);
      },
    );
  }
}

class CreateSelectionHome extends StatefulWidget {
  const CreateSelectionHome({super.key});

  @override
  _CreateSelectionHomeState createState() => _CreateSelectionHomeState();
}

class _CreateSelectionHomeState extends State<CreateSelectionHome> {
  String selectedOption = "Film";

  void navigateToForm() {
    if (selectedOption == "Film") {
      Navigator.of(context).pushNamed('movie');
    } else if (selectedOption == "Series") {
      Navigator.of(context).pushNamed('series');
    }
    // Handle "List" if needed.
  }

  Widget buildOption(String title, Color color, bool isSelected) {
    return GestureDetector(
      onTap: () {
        setState(() {
          selectedOption = title;
        });
      },
      child: Container(
        width: double.infinity,
        height: 60,
        padding: const EdgeInsets.symmetric(vertical: 12),
        margin: const EdgeInsets.symmetric(vertical: 5),
        decoration: BoxDecoration(
          color: isSelected ? color : Colors.grey[300],
          borderRadius: BorderRadius.circular(10),
        ),
        child: Center(
          child: Text(
            title,
            style: TextStyle(
              fontWeight: FontWeight.bold,
              color: isSelected ? Colors.white : Colors.black54,
            ),
          ),
        ),
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    return Center(
      child: Container(
        padding: const EdgeInsets.symmetric(horizontal: 15.0),
        child: Container(
          padding: const EdgeInsets.all(20),
          decoration: BoxDecoration(
            color: Colors.white,
            borderRadius: BorderRadius.circular(15),
            boxShadow: const [BoxShadow(color: Colors.black12, blurRadius: 10)],
          ),
          child: Column(
            mainAxisSize: MainAxisSize.min,
            children: [
              const Text("CREATE", style: TextStyle(fontWeight: FontWeight.bold)),
              const SizedBox(height: 10),
              buildOption("Film", MyApp.accentColor, selectedOption == "Film"),
              buildOption("Series", MyApp.accentColor, selectedOption == "Series"),
              buildOption("List", MyApp.accentColor, selectedOption == "List"),
              const SizedBox(height: 15),
              ElevatedButton(
                onPressed: navigateToForm,
                style: ElevatedButton.styleFrom(
                  backgroundColor: MyApp.primaryColor,
                  shape: RoundedRectangleBorder(
                    borderRadius: BorderRadius.circular(15),
                  ),
                ),
                child: Container(
                  width: double.infinity,
                  padding: const EdgeInsets.symmetric(vertical: 15),
                  child: const Center(
                    child: Text(
                      "START",
                      style: TextStyle(fontWeight: FontWeight.bold, color: Colors.black),
                    ),
                  ),
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
