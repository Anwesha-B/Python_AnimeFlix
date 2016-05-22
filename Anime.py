# -*- coding: utf-8 -*-
import Ghibli
import Tomato
import webbrowser
import re

spirited_away = Ghibli.Movie("Spirited Away",
                             "In this animated feature, 10-year-old Chihiro and her parents stumble upon a seemingly abandoned amusement park. "+
                             "After her mother and father are turned into giant pigs, Chihiro meets the mysterious Haku, who explains "
                             +"that the park is a resort for supernatural beings who need a break from their time spent in the earthly realm, "+
                             "and that she must work there to free herself and her parents.",
                             "https://upload.wikimedia.org/wikipedia/en/3/30/Spirited_Away_poster.JPG",
                             "Fantasy/Mystery",
                             "https://www.youtube.com/watch?v=ByXuk9QqQkk",
                             "2h 5m",
                             "Hayao Miayazaki",
                             "2001"
                             )
howls_moving_castle = Ghibli.Movie("Howl's Moving Castle",
                                   "A young girl is forced to toil in her parents' hat shop and her only joy is in her occasional meetings with a handsome stranger, Howl the wizard. When a witch sees her happiness, she curses her to become old in a jealous rage. Ashamed and afraid, she flees to Howl's magic moving castle. Will Howl see her for who she really is?",
                                   "https://upload.wikimedia.org/wikipedia/en/a/a0/Howls-moving-castleposter.jpg",
                                   "Fantasy/Drama",
                                   "https://www.youtube.com/watch?v=iwROgK94zcM",
                                   "1h 59m",
                                   "Hayao Miayazaki",
                                   "2004"
                                   )
castle_in_the_sky = Ghibli.Movie("Castle in the sky",
                                 "Two orphans, one with a levitation stone, search for lost treasure and the key to their past in a legendary floating city.",
                                 "https://upload.wikimedia.org/wikipedia/en/4/40/Castle_in_the_Sky_%28Movie_Poster%29.jpg",
                                "Fantasy/Action",
                                 "https://www.youtube.com/watch?v=McM0_YHDm5A",
                                 "2h 6m",
                                 "Hayao Miyazaki",
                                 "1986"
                                 )
neighbour_totoro = Ghibli.Movie("My neighbour Totoro",
                                "Two sisters encounter a mythical forest sprite and its woodland companions when they move to rural Japan.",
                                "https://upload.wikimedia.org/wikipedia/en/0/02/My_Neighbor_Totoro_-_Tonari_no_Totoro_%28Movie_Poster%29.jpg",
                                "Fantasy/Drama",
                                "https://www.youtube.com/watch?v=TuLX50_5UAI",
                                "1h 28m",
                                "Hayao Miyazaki",
                                "1988"
                                )
mononoke_hime = Ghibli.Movie("Princess Mononoke",
                             "A prince becomes involved in the struggle between a forest princess and the encroachment of mechanization.",
                             "https://upload.wikimedia.org/wikipedia/en/2/24/Princess_Mononoke_Japanese_Poster_%28Movie%29.jpg",
                             "Fantasy/Drama",
                             "https://www.youtube.com/watch?v=4OiMOHRDs14",
                             "2h 15m",
                             "Hayao Miyazaki",
                             "1997"
                             )
kiki_delivery = Ghibli.Movie("Kiki's delivery service",
                             "Kiki's Delivery Service is a 1989 Japanese animated fantasy film produced by Studio Ghibli. It was written, produced and directed by Hayao Miyazaki as an adaptation of the 1985 novel of the same name by Eiko Kadono.",
                             "https://upload.wikimedia.org/wikipedia/en/0/07/Kiki%27s_Delivery_Service_%28Movie%29.jpg",
                            "Fantasy/Drama",
                             "https://www.youtube.com/watch?v=4bG17OYs-GA",
                             "1h 4m",
                              "Hayao Miyazaki",
                             "1989")
cardcaptor_sakura = Ghibli.Anime("Cardcaptor Sakura",
                                 "Cardcaptor Sakura, abbreviated as CCS and also known as Cardcaptors, is a Japanese shōjo manga series written and illustrated by the manga group Clamp",
                                 "https://upload.wikimedia.org/wikipedia/en/5/50/Cardcaptor_Sakura_vol1_cover.jpg",
                                 "adventure, comedy, magic, romance",
                                 "https://www.youtube.com/watch?v=luM4oGFSpT8",
                                 "70",
                                 "Madhouse",
                                 "1998")
inuyasha = Ghibli.Anime("Inuyasha",
                        "The series follows Kagome Higurashi, a 15-year-old girl from Tokyo who is transported to the Sengoku period after falling into a well in her family shrine, where she meets the half-demon Inuyasha. When a monster from that era tries to take the magical Shikon Jewel embodied in Kagome, she accidentally shatters the Jewel into many pieces that are dispersed across Japan. Inuyasha and Kagome start traveling to recover it before the powerful demon Naraku finds all the shards",
                        "https://upload.wikimedia.org/wikipedia/en/2/2a/InuYasha1.jpg",
                        "Action, Romantic comedy, Sengoku-jidai geki, Supernatural",
                        "https://www.youtube.com/watch?v=0nTgKxeWMGQ",
                        "167",
                        "Sunrise",
                        "2000")
bleach = Ghibli.Anime("Bleach",
                      "Bleach follows the adventures of Ichigo Kurosaki after he obtains the powers of a Soul Reaper (死神 Shinigami?, literally, Death God) — a death personification similar to the Grim Reaper — from another Soul Reaper, Rukia Kuchiki. His newfound powers force him to take on the duties of defending humans from evil spirits and guiding departed souls to the afterlife",
                      "https://upload.wikimedia.org/wikipedia/en/5/5c/Bleach_01_-_The_Substitute.jpg",
                      "Action, Adventure, Fantasy, Comedy-drama, Supernatural",
                      "https://www.youtube.com/watch?v=oZ67d9XSjFs",
                      "366",
                      "Studio Pierrot",
                      "2006")
code_geass = Ghibli.Anime("Code Geass",
                          "The Holy Empire of Britannia conquered the country known as Japan and now call it Area 11. Its residents lost their rights to self-govern and are now called Elevens. The Empire uses powerfully destructive robotic weapons called Knightmares to ensure control, but someone is about to stand up against it. Lelouch, the black prince, has endless ambition and uses the power of the Geass to build a world based on his ideals. Suzaku Kururugi, the white knight, aspires to justice and strives to live an honest and fair life",
                          "https://upload.wikimedia.org/wikipedia/en/0/08/Code_Geass_DVD_Part3.png",
                          "Tragedy, Mecha, Science fantasy",
                          "https://www.youtube.com/watch?v=8ShufKkeKoQ",
                          "50",
                          "Sunrise",
                          "2006")
death_note = Ghibli.Anime("Death Note",
                          "Light Yagami is a genius high schooler who discovers the Death Note, a notebook that kills anyone whose name is written in it. After experimenting with the notebook, Light meets the Shinigami Ryuk, the notebook's original owner, who dropped the notebook to the human world out of boredom. Light tells Ryuk of his plan to rule over a new world free from criminals as a god, where only people he deems morally fit to live remain. Light eventually becomes known to the public as Kira (キラ?), which is derived from the Japanese pronunciation of the word Killer",
                          "https://upload.wikimedia.org/wikipedia/en/e/e2/SNote.jpg",
                          "Occult detective, psychological thriller",
                          "https://www.youtube.com/watch?v=Amag3NrjBc0",
                          "37",
                          "Madhouse",
                          "2007")
fma_brotherhood = Ghibli.Anime("Full Metal Alchemist Brotherhod",
                               "The Elric brothers' mother is dead and their father has long since abandoned them. Deciding to perform a forbidden human transmutation to bring their mother back, they end up losing their bodies. Now Edward must join the military in order to gain certain alchemical privileges, with his one goal being to restore his brother to his original state. But with war on the horizon it's only a matter of time before they are both forced to question their morals and ultimately decide the value of human life.",
                               "https://upload.wikimedia.org/wikipedia/en/9/9c/Fullmetal_Alchemist_Brotherhood.jpg",
                               "Adventure, Science fantasy",
                               "https://www.youtube.com/watch?v=BOm_PAI2goo",
                               "64",
                               "Bones",
                               "2009")
movies = [spirited_away, howls_moving_castle, castle_in_the_sky, neighbour_totoro, mononoke_hime, kiki_delivery]
animes = [cardcaptor_sakura, inuyasha, bleach, code_geass, death_note, fma_brotherhood]
videos = movies + animes
Tomato.open_movies_page(videos)
