import Ghibli
import Tomato
spirited_away = Ghibli.Movie("Spirited Away",
                             "In this animated feature, 10-year-old Chihiro and her parents stumble upon a seemingly abandoned amusement park. "+
                             "After her mother and father are turned into giant pigs, Chihiro meets the mysterious Haku, who explains "
                             +"that the park is a resort for supernatural beings who need a break from their time spent in the earthly realm, "+
                             "and that she must work there to free herself and her parents.",
                             "https://upload.wikimedia.org/wikipedia/en/3/30/Spirited_Away_poster.JPG",
                             "https://www.youtube.com/watch?v=ByXuk9QqQkk"                     
                             )
howls_moving_castle = Ghibli.Movie("Howl's Moving Castle",
                                   "A young girl is forced to toil in her parents' hat shop and her only joy is in her occasional meetings with a handsome stranger, Howl the wizard. When a witch sees her happiness, she curses her to become old in a jealous rage. Ashamed and afraid, she flees to Howl's magic moving castle. Will Howl see her for who she really is?",
                                   "https://upload.wikimedia.org/wikipedia/en/a/a0/Howls-moving-castleposter.jpg",
                                   "https://www.youtube.com/watch?v=iwROgK94zcM"
                                   )
castle_in_the_sky = Ghibli.Movie("Castle in the sky",
                                 "Two orphans, one with a levitation stone, search for lost treasure and the key to their past in a legendary floating city.",
                                 "https://upload.wikimedia.org/wikipedia/en/4/40/Castle_in_the_Sky_%28Movie_Poster%29.jpg",
                                 "https://www.youtube.com/watch?v=McM0_YHDm5A")
neighbour_totoro = Ghibli.Movie("My neighbour Totoro",
                                "Two sisters encounter a mythical forest sprite and its woodland companions when they move to rural Japan.",
                                "https://upload.wikimedia.org/wikipedia/en/0/02/My_Neighbor_Totoro_-_Tonari_no_Totoro_%28Movie_Poster%29.jpg",
                                "https://www.youtube.com/watch?v=TuLX50_5UAI")
mononoke_hime = Ghibli.Movie("Princess Mononoke",
                             "A prince becomes involved in the struggle between a forest princess and the encroachment of mechanization.",
                             "https://upload.wikimedia.org/wikipedia/en/2/24/Princess_Mononoke_Japanese_Poster_%28Movie%29.jpg",
                             "https://www.youtube.com/watch?v=4OiMOHRDs14")
kiki_delivery = Ghibli.Movie("Kiki's delivery service",
                             "Kiki's Delivery Service is a 1989 Japanese animated fantasy film produced by Studio Ghibli. It was written, produced and directed by Hayao Miyazaki as an adaptation of the 1985 novel of the same name by Eiko Kadono.",
                             "https://upload.wikimedia.org/wikipedia/en/0/07/Kiki%27s_Delivery_Service_%28Movie%29.jpg",
                             "https://www.youtube.com/watch?v=4bG17OYs-GA")
movies = [spirited_away, howls_moving_castle, castle_in_the_sky, neighbour_totoro, mononoke_hime, kiki_delivery]
Tomato.open_movies_page(movies)
