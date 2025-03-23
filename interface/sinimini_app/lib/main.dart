import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:sinimini_app/home_page.dart';
void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});
  static const Color accentColor = Color.fromRGBO(234, 140, 85, 1);
  static const Color backgroundColor = Color.fromRGBO(217, 217, 217, 1);
  static const Color primaryColor = Color.fromRGBO(217, 187, 249, 1);


  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      theme: ThemeData(
        textTheme: GoogleFonts.montserratTextTheme(),
        
      ),
      debugShowCheckedModeBanner: false,
      home: const HomeScreen(),
    );
  }
}




