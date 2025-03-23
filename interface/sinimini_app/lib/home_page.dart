import 'package:flutter/material.dart';
import 'package:sinimini_app/create_screen.dart'; // Ensure this file exports CreateSelectionWidget
import 'registration_screen.dart';
import 'search_screen.dart'; // Import your SearchScreen widget

class HomeScreen extends StatefulWidget {
  const HomeScreen({super.key});

  @override
  _HomeScreenState createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  // GlobalKey for the nested navigator in CreateSelectionWidget.
  final GlobalKey<NavigatorState> _createNavigatorKey = GlobalKey<NavigatorState>();

  // Screen indexes: 0 - Search, 1 - Create, 2 - Profile.
  int _selectedIndex = 0;

  // User registration state.
  bool _isLoggedIn = false;
  String _profileName = "";

  late final List<Widget> _bodyWidgets;

  @override
  void initState() {
    super.initState();
    _bodyWidgets = [
      // Change the first screen to the SearchScreen.
      const SearchScreen(),
      // Pass the GlobalKey to CreateSelectionWidget.
      CreateSelectionWidget(navigatorKey: _createNavigatorKey),
      const Center(child: Text("Profile Screen Content")),
    ];

    // On first launch, if not registered, show registration screen.
    WidgetsBinding.instance.addPostFrameCallback((_) {
      if (!_isLoggedIn) {
        _showRegistrationScreen();
      }
    });
  }

  void _showRegistrationScreen() async {
    final result = await Navigator.push(
      context,
      MaterialPageRoute(builder: (context) => AuthScreen()),
    );
    if (result != null && result is String) {
      setState(() {
        _profileName = result;
        _isLoggedIn = true;
      });
    }
  }

  void _showUserProfileDialog() {
    showDialog(
      context: context,
      builder: (context) {
        return AlertDialog(
          title: const Text("Profile"),
          content: Text("Logged in as: $_profileName"),
          actions: [
            TextButton(
              onPressed: () {
                // Log out action.
                setState(() {
                  _isLoggedIn = false;
                  _profileName = "";
                });
                Navigator.of(context).pop();
                // Optionally, force re-registration:
                _showRegistrationScreen();
              },
              child: const Text("Log Out"),
            ),
            TextButton(
              onPressed: () {
                Navigator.of(context).pop();
              },
              child: const Text("Close"),
            )
          ],
        );
      },
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: const Color.fromRGBO(240, 240, 240, 1),
      appBar: AppBar(
        // Show a back button if not on the Search screen.
        leading: _selectedIndex != 0
            ? IconButton(
                icon: const Icon(Icons.arrow_back),
                onPressed: () {
                  if (_selectedIndex == 1 &&
                      _createNavigatorKey.currentState != null &&
                      _createNavigatorKey.currentState!.canPop()) {
                    // Pop nested route if possible.
                    _createNavigatorKey.currentState!.pop();
                  } else {
                    // Otherwise, return to the Search screen.
                    setState(() {
                      _selectedIndex = 0;
                    });
                  }
                },
              )
            : null,
        title: const Text('sinimini'),
        centerTitle: true,
        backgroundColor: Colors.white,
        actions: [
          IconButton(
            icon: const Icon(Icons.person),
            onPressed: () {
              if (_isLoggedIn) {
                _showUserProfileDialog();
              } else {
                _showRegistrationScreen();
              }
            },
          ),
        ],
      ),
      body: IndexedStack(
        
        
        index: _selectedIndex,
        children: _bodyWidgets,
      ),
      bottomNavigationBar: BottomAppBar(
        color: const Color.fromRGBO(234, 140, 85, 1),
        shape: const CircularNotchedRectangle(),
        notchMargin: 10,
        child: Row(
          mainAxisAlignment: MainAxisAlignment.spaceAround,
          children: [
            // When pressing the search button, the SearchScreen is displayed.
            // If needed, you can also clear its internal search query here.
            IconButton(
              icon: const Icon(Icons.search),
              onPressed: () {
                setState(() {
                  _selectedIndex = 0;
                });
              },
            ),
            IconButton(
              icon: const Icon(Icons.add),
              onPressed: () {
                setState(() {
                  _selectedIndex = 1;
                });
              },
            ),
            IconButton(
              icon: const Icon(Icons.rate_review),
              onPressed: () {
                setState(() {
                  _selectedIndex = 2;
                });
              },
            ),
          ],
        ),
      ),
    );
  }
}
