import 'package:flutter/material.dart';
import 'package:sinimini_app/main.dart';

// A simple model class for a Film.
class Film {
  final String name;
  final String director;
  final List<String> genres;
  final String duration; // Duration in minutes (as a string or int)

  Film({
    required this.name,
    required this.director,
    required this.genres,
    required this.duration,
  });
}

class SearchScreen extends StatefulWidget {
  const SearchScreen({Key? key}) : super(key: key);

  @override
  _SearchScreenState createState() => _SearchScreenState();
}

class _SearchScreenState extends State<SearchScreen> {
  // Simulated database data (replace with real database call).
  List<Film> allFilms = [
    Film(
      name: "Avengers: Endgame",
      director: "Anthony Russo, Joe Russo",
      genres: ["Action", "Sci-Fi"],
      duration: "181",
    ),
    Film(
      name: "Inception",
      director: "Christopher Nolan",
      genres: ["Action", "Thriller", "Sci-Fi"],
      duration: "148",
    ),
    Film(
      name: "The Godfather",
      director: "Francis Ford Coppola",
      genres: ["Crime", "Drama"],
      duration: "175",
    ),
    Film(
      name: "Titanic",
      director: "James Cameron",
      genres: ["Drama", "Romance"],
      duration: "195",
    ),
    // Add more films as needed.
  ];

  List<Film> filteredFilms = [];
  String searchQuery = "";

  @override
  void initState() {
    super.initState();
    // Sort films alphabetically by name.
    allFilms.sort((a, b) => a.name.compareTo(b.name));
    filteredFilms = List.from(allFilms);
  }

  void _filterFilms(String query) {
    setState(() {
      searchQuery = query;
      if (query.isEmpty) {
        filteredFilms = List.from(allFilms);
      } else {
        filteredFilms = allFilms.where((film) {
          return film.name.toLowerCase().contains(query.toLowerCase());
        }).toList();
      }
    });
  }

  // Handle options from the three dots menu.
  void _handleMenuOption(Film film, String option) {
    if (option == 'watch_later') {
      // Replace with your database operation.
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(content: Text('${film.name} added to Watch Later')),
      );
    } else if (option == 'other_list') {
      // Replace with your database operation.
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(content: Text('${film.name} added to Other List')),
      );
    }
  }

  // Build each film item.
  Widget _buildFilmItem(Film film) {
    return Card(
      color: Colors.white, 
      elevation: 10,
      shadowColor: const Color.fromARGB(129, 217, 187, 249),
      margin: const EdgeInsets.symmetric(vertical: 8, horizontal: 16),
      child: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Row(
          children: [
            // Film details.
            Expanded(
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text(
                    film.name,
                    style: const TextStyle(
                        fontSize: 18, fontWeight: FontWeight.bold),
                  ),
                  const SizedBox(height: 4),
                  Text("Director: ${film.director}"),
                  const SizedBox(height: 4),
                  Text("Genres: ${film.genres.join(', ')}"),
                  const SizedBox(height: 4),
                  Text("Duration: ${film.duration} min"),
                ],
              ),
            ),
            // 3-dots menu button.
            PopupMenuButton<String>(
              onSelected: (option) => _handleMenuOption(film, option),
              itemBuilder: (BuildContext context) => <PopupMenuEntry<String>>[
                const PopupMenuItem<String>(
                  value: 'watch_later',
                  child: Text('Add to Watch Later'),
                ),
                const PopupMenuItem<String>(
                  value: 'other_list',
                  child: Text('Add to Other List'),
                ),
              ],
            ),
          ],
        ),
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      // Use a simple AppBar with a plain white background.
      backgroundColor: Color.fromRGBO(240, 240, 240, 1),
      body: 
      Container(
        child:Column(
        
        children: [
          // Plain search textbox at the top.
          Padding(
            padding: const EdgeInsets.all(15.0),
            child: TextField(
              onChanged: _filterFilms,
              decoration: InputDecoration(
                hintText: 'Search films...',
                prefixIcon: const Icon(Icons.search),
                filled: true,
                fillColor: Colors.white,
                border: OutlineInputBorder(
                  borderRadius: BorderRadius.circular(8),
                  borderSide: BorderSide.none,
                ),
              ),
            ),
          ),
          // Film list.
          Expanded(
            child: ListView.builder(
              itemCount: filteredFilms.length,
              itemBuilder: (context, index) {
                final film = filteredFilms[index];
                return _buildFilmItem(film);
              },
            ),
          ),
        ],
      ),)
      
    );
  }
}
