import fresh_tomatoes
import movies


toy_story = movies.Movie("Toy Story",
                         "A Story of toys coming to life",
                         "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcSzy3MH1Pr0xN0RKULlCFq-3NAxuoF7zoZQLIEKVSI4r-kNrR3M",
                         "https://www.youtube.com/watch?v=wmiIUN-7qhE")
#toy_story.show_trailer()

tenet = movies.Movie("TENET",
                     "A secret agent embarks on a dangerous, time-bending mission to prevent the start of World War III",
                     "https://www.google.com/url?sa=i&url=https%3A%2F%2Fencrypted-tbn1.gstatic.com%2Fimages%3Fq%3Dtbn%3AANd9GcT-sg5sL8FnOVMC_Au85ohUWgmo6pvOkKoLo0yzzYoGI674tfDr&psig=AOvVaw0afeE3kVxmFBs2kS47Wz5P&ust=1603223462690000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCND50vq2wewCFQAAAAAdAAAAABAD",
                     "https://www.youtube.com/watch?v=AZGcmvrTX9M")

#tenet.show_trailer()

Dolittle = movies.Movie("Dolittle",
                        "Dr. John Dolittle lives in solitude behind the high walls of his lush manor in 19th-century England. His only companionship comes from an array of exotic animals that he speaks to on a daily basis. But when young Queen Victoria becomes gravely ill, the eccentric doctor and his furry friends embark on an epic adventure to a mythical island to find the cure.",
                        "https://m.media-amazon.com/images/M/MV5BODQ2MzVmZDctMDRkMi00ODBlLThjZWUtYTVmYjA0YmU4NDZhXkEyXkFqcGdeQXVyMTA0OTQ1OTA0._V1_SY1000_CR0,0,806,1000_AL_.jpg",
                        "https://www.youtube.com/watch?v=zjm6rDgKNMY")

Ironman1 = movies.Movie("IRONMAN",
                        "After being held captive in an Afghan cave, billionaire engineer Tony Stark creates a unique weaponized suit of armor to fight evil.",
                        "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcRVCyceg2xqUQ8zye4k2r1D8dUQFXm7sZMuqymAnCmoIASoYlxC",
                        "https://www.youtube.com/watch?v=8ugaeA-nMTc")

Ironman2 = movies.Movie("IRONMAN 2",
                        "With the world now aware that he is Iron Man, billionaire inventor Tony Stark (Robert Downey Jr.) faces pressure from all sides to share his technology with the military. He is reluctant to divulge the secrets of his armored suit, fearing the information will fall into the wrong hands. With Pepper Potts (Gwyneth Paltrow) and Rhodey Rhodes (Don Cheadle) by his side, Tony must forge new alliances and confront a powerful new enemy.",
                        "https://static.wikia.nocookie.net/ironman/images/d/df/P3546118_v_v8_af.jpg/revision/latest/top-crop/width/360/height/450?cb=20191202171556",
                        "https://www.youtube.com/watch?v=BoohRoVA9WQ")


Ironman3 = movies.Movie("IRONMAN 3",
                        "Tony Stark (Robert Downey Jr.), now, is more dependent on the suits that give him his Iron Man persona -- so much so that every aspect of his life is affected, including his relationship with Pepper (Gwyneth Paltrow). After a malevolent enemy known as the Mandarin (Ben Kingsley) reduces his personal world to rubble, Tony must rely solely on instinct and ingenuity to avenge his losses and protect the people he loves",
                        "https://wallpaperstock.net/iron-man-3-official-wallpaper_wallpapers_36153_640x960.jpg",
                        "https://www.youtube.com/watch?v=Ke1Y3P9D0Bc")
#Ironman3.show_trailer()

Bahubali1 = movies.Movie("Baahubali:The Beginning",
                        "In the kingdom of Mahishmati, while pursuing his love, Shivudu learns about the conflict ridden past of his family and his legacy. He must now prepare himself to face his newfound arch-enemy.",
                        "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcS1MpZ-4QpkpoB0MubBnFsAJ06bGTM4bdJgyg2C68JNWE1nzuET",
                        "https://www.youtube.com/watch?v=3NQRhE772b0")


Bahubali2 = movies.Movie("Baahubali 2: The Conclusion",
                        "When Bhallaladeva conspires against his brother to become the king of Mahishmati, he has him killed by Katappa and imprisons his wife. Years later, his brother's son returns to avenge his father's death.",
                        "https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcRlhsFudAiEvNDiNPu_Sx7zkRsOCun061F62b4Cdy9VX6Tin20G",
                        "https://www.youtube.com/watch?v=G62HrubdD6o")



names = [toy_story,tenet,Ironman1,Ironman2,Ironman3,Bahubali1,Bahubali2]
fresh_tomatoes.open_movies_page(names)
