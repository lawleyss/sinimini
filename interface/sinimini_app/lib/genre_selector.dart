import 'package:flutter/material.dart';
class GenreSelector extends StatefulWidget {
  @override
  const GenreSelector({Key? key}) : super(key: key);
  @override
  GenreSelectorState createState() => GenreSelectorState();
}

class GenreSelectorState extends State<GenreSelector> {
  
  final List<String> availableGenres = [
    "Action", "Comedy", "Drama", "Horror", "Romance", "Sci-Fi", "Thriller"
  ];
  final List<String> selectedGenres = [];

  @override
  Widget build(BuildContext context) {
    return Container
    
    ( width: double.infinity,
    padding: const EdgeInsets.all(15),
      decoration: BoxDecoration(color: const Color.fromRGBO(240, 240, 240, 100),
        borderRadius: BorderRadius.circular(15),),
      child: Column(
      
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        const Text("Genres", style: TextStyle(fontSize: 16, fontWeight: FontWeight.bold)),
        Column(
          children: selectedGenres.map((genre) {
            return Container(
              margin: const EdgeInsets.symmetric(vertical: 4),
              padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 8),
              decoration: BoxDecoration(
                color: Colors.grey[300],
                borderRadius: BorderRadius.circular(8),
              ),
              child: Row(
                mainAxisAlignment: MainAxisAlignment.spaceBetween,
                children: [
                  Text(genre),
                  IconButton(
                    icon: const Icon(Icons.close),
                    onPressed: () {
                      setState(() {
                        selectedGenres.remove(genre);
                      });
                    },
                  )
                ],
              ),
            );
          }).toList(),
        ),
        if (selectedGenres.length < 3)
          DropdownButton<String>(
            hint: const Text("Add more"),
            value: null,
            onChanged: (String? newValue) {
              if (newValue != null && !selectedGenres.contains(newValue)) {
                setState(() {
                  selectedGenres.add(newValue);
                });
              }
            },
            items: availableGenres
                .where((genre) => !selectedGenres.contains(genre))
                .map<DropdownMenuItem<String>>((String genre) {
              return DropdownMenuItem<String>(
                value: genre,
                child: Text(genre),
              );
            }).toList(),
          ),
      ],
    ),);
    
  }
}
