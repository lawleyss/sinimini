import 'package:flutter/material.dart';
import 'package:sinimini_app/main.dart'; // Ensure MyApp.accentColor and MyApp.primaryColor are defined here.

class AuthScreen extends StatefulWidget {
  const AuthScreen({super.key});

  @override
  _AuthScreenState createState() => _AuthScreenState();
}

class _AuthScreenState extends State<AuthScreen> {
  // Toggle between log in (true) and register (false)
  bool _isLoginMode = true;
  final _profileController = TextEditingController();
  final _passwordController = TextEditingController();

  // Border radius value for buttons.
  final double _buttonBorderRadius = 15.0;

  void _submit() {
    final profileName = _profileController.text.trim();
    final password = _passwordController.text.trim();
    if (profileName.isNotEmpty && password.isNotEmpty) {
      // In a real app, perform validation/authentication here.
      Navigator.of(context).pop(profileName); // Return the profile name.
    } else {
      ScaffoldMessenger.of(context).showSnackBar(
        const SnackBar(content: Text("Please fill in both fields.")),
      );
    }
  }

  @override
  void dispose() {
    _profileController.dispose();
    _passwordController.dispose();
    super.dispose();
  }

  // Button helper based on your provided principle.
  Widget buildButton(String text, Color color, VoidCallback onPressed,
      {Color textColor = Colors.white, bool bold = false}) {
    return SizedBox(
      width: double.infinity,
      height: 70,
      child: ElevatedButton(
        onPressed: onPressed,
        style: ElevatedButton.styleFrom(
          backgroundColor: color,
          shape: RoundedRectangleBorder(
            borderRadius: BorderRadius.circular(_buttonBorderRadius),
          ),
        ),
        child: Text(
          text,
          style: TextStyle(
            color: textColor,
            fontWeight: bold ? FontWeight.bold : FontWeight.normal,
          ),
        ),
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: const Color.fromRGBO(240, 240, 240, 1),
      appBar: AppBar(
        title: Text(_isLoginMode ? "Log In" : "Register"),
        automaticallyImplyLeading: false,
      ),
      body: Center(
        child: Container(
          padding: const EdgeInsets.all(15),
          margin: const EdgeInsets.all(15),
          decoration: BoxDecoration(
            color: Colors.white,
            borderRadius: BorderRadius.circular(15),
          ),
          child: Column(
            mainAxisSize: MainAxisSize.min,
            children: [
              // Profile Name TextField.
              TextField(
                controller: _profileController,
                decoration: const InputDecoration(
                  labelText: "Profile Name",
                  border: OutlineInputBorder(),
                ),
              ),
              const SizedBox(height: 10),
              // Password TextField.
              TextField(
                controller: _passwordController,
                decoration: const InputDecoration(
                  labelText: "Password",
                  border: OutlineInputBorder(),
                ),
                obscureText: true,
              ),
              const SizedBox(height: 20),
              // Submit button using MyApp.accentColor.
              buildButton(
                _isLoginMode ? "Log In" : "Register",
                MyApp.accentColor,
                _submit,
                textColor: Colors.white,
                bold: true,
              ),
              const SizedBox(height: 10),
              // Toggle mode button using MyApp.primaryColor with black text.
              buildButton(
                _isLoginMode
                    ? "Don't have an account? Register"
                    : "Already have an account? Log In",
                MyApp.primaryColor,
                () {
                  setState(() {
                    _isLoginMode = !_isLoginMode;
                  });
                },
                textColor: Colors.black,
                bold: false,
              ),
            ],
          ),
        ),
      ),
    );
  }
}
