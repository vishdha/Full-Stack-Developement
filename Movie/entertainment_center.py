import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that came into real life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")
#print(toy_story.storyline)

central_intelligence = media.Movie("Central Intelligence",
                     "CBI",
                     "https://upload.wikimedia.org/wikipedia/commons/4/4a/Central_intelligence.jpg",
                     "https://www.youtube.com/watch?v=0FKctBraQj0")

 
inception  = media.Movie("Inception",
                     "A mind game",
                     "http://t2.gstatic.com/images?q=tbn:ANd9GcRo9vfJCM6dzPkZHIHBVCtlJnAnew9Ai26kEdrli0-tfmatmciD",
                     "https://www.youtube.com/watch?v=66TuSJo4dZM")

walk_to_remember = media.Movie("Walk To Remember",
                     "The Beautifull Love Story",
                     "https://upload.wikimedia.org/wikipedia/en/d/dc/A_Walk_to_Remember_Poster.jpg",
                     "https://www.youtube.com/watch?v=V96uhfQ0x9A")

social_network = media.Movie("Social Network",
                     "Story based on Mark Zukerburg founder of facebook",
                     "http://t2.gstatic.com/images?q=tbn:ANd9GcTj268E01VcjLW3fNrO2z10WpXs7WMeciAB9wYSOA2DI-le_NQH",
                     "https://www.youtube.com/watch?v=2RB3edZyeYw")


internship = media.Movie("The Internship",
                     "not an average interhsip",
                     "https://upload.wikimedia.org/wikipedia/en/e/ed/The-internship-poster.jpg",
                     "https://www.youtube.com/watch?v=cdnoqCViqUo")




#central_intelligence.show_trailer()

movies = [toy_story,central_intelligence, inception, walk_to_remember,social_network,internship]
fresh_tomatoes.open_movies_page(movies)
