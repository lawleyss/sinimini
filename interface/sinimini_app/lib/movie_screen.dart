import 'package:flutter/material.dart';
import 'genre_selector.dart';

class MovieFormScreen extends StatefulWidget {
  const MovieFormScreen({super.key});

  @override
  _MovieFormScreenState createState() => _MovieFormScreenState();
}

class _MovieFormScreenState extends State<MovieFormScreen> {
  final TextEditingController titleController = TextEditingController();
  final TextEditingController directorController = TextEditingController();
  final TextEditingController durationController = TextEditingController();
  final double Borders = 15;

  // GlobalKey to access GenreSelector's state.
  final GlobalKey<GenreSelectorState> _genreSelectorKey =
      GlobalKey<GenreSelectorState>();

  // Simulated function to send data to database.
  void _sendDataToDatabase({
    required String title,
    required String director,
    required String duration,
    required List<String> genres,
    double? rating,
  }) {
    // Replace this with your actual database code.
    print("Sending to DB:");
    print("Title: $title");
    print("Director: $director");
    print("Duration: $duration");
    print("Genres: $genres");
    if (rating != null) {
      print("Rating: $rating");
    }
    ScaffoldMessenger.of(context).showSnackBar(
      SnackBar(
        content: Text(rating == null
            ? "Movie created!"
            : "Movie created and rated!"),
      ),
    );
  }

  // Called when the user presses "CREATE"
  void _handleCreate() {
    final title = titleController.text;
    final director = directorController.text;
    final duration = durationController.text;
    final genres = _genreSelectorKey.currentState?.selectedGenres ?? [];
    _sendDataToDatabase(
      title: title,
      director: director,
      duration: duration,
      genres: genres,
    );
  }

  // Called when the user presses "CREATE & RATE"
  void _handleCreateAndRate() {
    showDialog<double>(
      context: context,
      builder: (context) {
        final ratingController = TextEditingController();
        return AlertDialog(
          title: const Text("Rate the movie"),
          content: TextField(
            controller: ratingController,
            keyboardType:
                const TextInputType.numberWithOptions(decimal: true),
            decoration: const InputDecoration(hintText: "Enter rating (0-10)"),
          ),
          actions: [
            TextButton(
              onPressed: () {
                final rating = double.tryParse(ratingController.text);
                if (rating != null && rating >= 0 && rating <= 10) {
                  // Round to one decimal.
                  final roundedRating = (rating * 10).round() / 10;
                  Navigator.of(context).pop(roundedRating);
                } else {
                  ScaffoldMessenger.of(context).showSnackBar(
                    const SnackBar(
                      content: Text(
                          "Invalid rating. Please enter a number between 0 and 10."),
                    ),
                  );
                }
              },
              child: const Text("Submit"),
            ),
          ],
        );
      },
    ).then((rating) {
      if (rating != null) {
        final title = titleController.text;
        final director = directorController.text;
        final duration = durationController.text;
        final genres = _genreSelectorKey.currentState?.selectedGenres ?? [];
        _sendDataToDatabase(
          title: title,
          director: director,
          duration: duration,
          genres: genres,
          rating: rating,
        );
      }
    });
  }

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
                // Assign the GlobalKey to GenreSelector.
                GenreSelector(key: _genreSelectorKey),
                const SizedBox(height: 15),
                buildTextField(durationController, 'Duration (min)',
                    isNumeric: true),
                SizedBox(height: Borders),
                buildButton('CREATE',
                    const Color.fromRGBO(217, 217, 217, 1), _handleCreate),
                SizedBox(height: Borders),
                buildButton('CREATE & RATE',
                    const Color.fromRGBO(217, 187, 249, 1), _handleCreateAndRate,
                    textColor: Colors.black, bold: true),
              ],
            ),
          ),
        ),
      ),
    );
  }

  Widget buildTextField(TextEditingController controller, String label,
      {bool isNumeric = false}) {
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

  Widget buildButton(String text, Color color, VoidCallback onPressed,
      {Color textColor = Colors.white, bool bold = false}) {
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