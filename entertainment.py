import media
import webbrowser
import fresh_tomatoes
Conjuring_2 = media.Movie("Conjuring 2","2:10hrs",
                          "The film begins with paranormal investigators Ed and Lorraine Warren documenting the Amityville murders at the Amityville house in 1976, to determine if a demonic presence was truly responsible for Ronald DeFeo Jr. mass murdering his family on November 13, 1974. During a seance, Lorraine is drawn into a vision where she relives the murders and discovers a demonic nun figure, before seeing Ed being fatally impaled. After a struggle, Ed is able to break her out of the vision.",
                       "http://www.voltagebd.com/wp-content/uploads/2016/01/The-Conjuring-2-The-Enfield-Poltergeist-2016.jpg",
                          "https://www.youtube.com/watch?v=KyA9AtUOqRM")
Kabali = media.Movie("Kabali","Kabali runs a school for the kids, which got affected in the gangster fights, 'Kalaiyarasan' acts as the teacher Tamilkumarn. Attakathi Dinesh is the son of another gangster gets impressed by Kabali and he joins in Kabali's group.","2:40hrs",
                     "http://www.telugupopular.com/wp-content/uploads/2015/09/kabali-tamil-poster.jpg", "https://www.youtube.com/watch?v=9mdJV5-eias")
Zootopia = media.Movie("Zootopia","2:30hrs",
                       "A little bunny named Judy Hops who grew up on a farm had to leave her family to persue her dreams as the first bunny cop in Zootopia. She ran into a con artist fox named Nick Wilde. They have to work together after an incident between the two of them to save Zootopia.",
                       "https://upload.wikimedia.org/wikipedia/en/e/ea/Zootopia.jpg",
                       "https://www.youtube.com/watch?v=bY73vFGhSVk")
Paisa = media.Movie("Paisa","2:20hrs",
                    " It deals with the power of money and how the whole world revolves around it",
                    "https://upload.wikimedia.org/wikipedia/en/f/f3/Paisa_poster.jpg", "https://www.youtube.com/watch?v=yeT5XEcSFxo")
Sarrinodu = media.Movie("Sarrinodu","2:15hrs",
                        "Dhanush (Aadhi) is the son of a Chief Minister. He kills a farmer for refusing to give up his lands. Gana (Allu Arjun) is an ex-military youth who beats up crooked people those whom cannot be punished by the law due to faults in the legal system. He is raised by his paternal uncle Sripati (Srikanth). He is berated by his father Umapati (Jayaprakash) for leaving the military and not having an aim in life. He is sent to meet his prospective bride Mahalakshmi (Rakul Preet Singh) to a neighboring village one day,daughter of his father's friend and also a sincere IAS Officer besides politician(Sai Kumar). But he meets a beautiful girl, Hansitha Reddy (Catherine Tresa), who is revealed to be the local MLA and falls in love with her. He makes up and tells his father a story of how he met Jaanu aka Mahalakshmi, the girl he was to meet and how she denied him as he gets into fights.",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/f/f4/Sarrainodu-Telugu_poster.jpg/220px-Sarrainodu-Telugu_poster.jpg",
                        "https://www.youtube.com/watch?v=YGzdsXbwOtI")
Civilwar = media.Movie("Captain America:Civil War","2:00hrs",
                       "Political pressure mounts to install a system of accountability when the actions of the Avengers lead to collateral damage. The new status quo deeply divides members of the team. Captain America (Chris Evans) believes superheroes should remain free to defend humanity without government interference. Iron Man (Robert Downey Jr.) sharply disagrees and supports oversight. As the debate escalates into an all-out feud, Black Widow (Scarlett Johansson) and Hawkeye (Jeremy Renner) must pick a side.","https://upload.wikimedia.org/wikipedia/en/thumb/5/53/Captain_America_Civil_War_poster.jpg/220px-Captain_America_Civil_War_poster.jpg","https://www.youtube.com/watch?v=uVdV-lxRPFo")

movies = [Conjuring_2, Kabali, Zootopia, Paisa, Sarrinodu, Civilwar]
fresh_tomatoes.open_movies_page(movies)
##def show(self):
    #print(self.title)
    #print(self.duration)
    #print(self.storyline)

    #play(self)
##def play(self):
    #webbrowser.open(self.poster_image_url)
    #webbrowser.open(self.trailer_youtube_url)

##show(Paisa)
