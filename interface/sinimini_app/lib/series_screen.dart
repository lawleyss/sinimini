import 'package:flutter/material.dart';
import 'genre_selector.dart';
class SeriesFormScreen extends StatefulWidget {
  const SeriesFormScreen({super.key});

  @override
  _SeriesFormScreenState createState() => _SeriesFormScreenState();
}

class _SeriesFormScreenState extends State<SeriesFormScreen> {
  final TextEditingController titleController = TextEditingController();
  final TextEditingController directorController = TextEditingController();
  final TextEditingController durationController = TextEditingController();
  final double Borders = 15;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: const Color.fromRGBO(240, 240, 240, 100),
      
      body: Padding(
        padding: const EdgeInsets.all(20.0),
        child: Container(
          decoration: BoxDecoration(
            color: Colors.white,
            borderRadius: BorderRadius.circular(15),
          ),
          child: Padding(
            padding: const EdgeInsets.all(20),
            child: Column(
              children: [
                buildTextField(titleController, 'Title'),
                const SizedBox(height: 15),
                buildTextField(directorController, 'Director'),
                const SizedBox(height: 15),
                const GenreSelector(),
                const SizedBox(height: 15),
                buildTextField(durationController, 'Duration (min)', isNumeric: true),
                SizedBox(height: Borders),
                buildButton('CREATE', const Color.fromRGBO(217, 217, 217, 1), () {}),
                SizedBox(height: Borders),
                buildButton('CREATE & RATE', const Color.fromRGBO(217, 187, 249, 1), () {}, textColor: Colors.black, bold: true),
              ],
            ),
          ),
        ),
      ),
    );
  }

  Widget buildTextField(TextEditingController controller, String label, {bool isNumeric = false}) {
    return Container(
      decoration: BoxDecoration(
        color: const Color.fromRGBO(240, 240, 240, 100),
        borderRadius: BorderRadius.circular(Borders),
      ),
      child: Padding(
        padding: const EdgeInsets.all(15),
        child: TextField(
          controller: controller,
          keyboardType: isNumeric ? TextInputType.number : TextInputType.text,
          decoration: InputDecoration(labelText: label),
        ),
      ),
    );
  }

  Widget buildButton(String text, Color color, VoidCallback onPressed, {Color textColor = Colors.white, bool bold = false}) {
    return SizedBox(
      width: double.infinity,
      height: 70,
      child: ElevatedButton(
        style: ElevatedButton.styleFrom(
          shape: RoundedRectangleBorder(
            borderRadius: BorderRadius.circular(Borders),
          ),
          backgroundColor: color,
        ),
        onPressed: onPressed,
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
}
