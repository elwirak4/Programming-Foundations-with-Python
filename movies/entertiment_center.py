import fresh_tomatoes
import media


toy_story = media.Movie("Toy Story", "A story of a boy and his toys that come to life",
                        "https://en.wikipedia.org/wiki/Toy_Story#/media/File:Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=tN1A2mVnrOM")
#print(toy_story.storyline)

avatar = media.Movie("Avatar", "A marine on an alien planet",
                      "https://en.wikipedia.org/wiki/Avatar_(2009_film)#/media/File:Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=uZNHIU3uHT4")
print(avatar.storyline)
#avatar.show_trailer()

un_homme_et_une_femme = media.Movie("Un homme et une femme",
                                    "A story about love",
                                    "https://en.wikipedia.org/wiki/A_Man_and_a_Woman#/media/File:Un_homme_et_une_femme_1966_poster.jpg",
                                    "https://www.youtube.com/watch?v=ALQIWIzPE3Q")
#print(un_homme_et_une_femme.storyline)
#un_homme_et_une_femme.show_trailer()


movies = [toy_story, avatar, un_homme_et_une_femme]
fresh_tomatoes.open_movies_page(movies)
