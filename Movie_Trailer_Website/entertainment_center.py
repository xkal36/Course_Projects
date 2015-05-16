import fresh_tomatoes
import media

# Here we instantiate all our Movie objects that get passed
# into the open_movie_page function below that dispalys them 
# and their associated attributes

goodfellas = media.Movie("Goodfellas", 
	"The story of Irish-Italian American, Henry Hill, and how he lives day-to-day life as a member of the Mafia.",
	"http://upload.wikimedia.org/wikipedia/en/thumb/7/7b/Goodfellas.jpg/220px-Goodfellas.jpg",
	"https://www.youtube.com/watch?v=qo5jJpHtI1Y",
	8.7)

interstellar = media.Movie("Interstellar",
	"A team of explorers travel through a wormhole in an attempt to ensure humanity's survival.",
	"http://upload.wikimedia.org/wikipedia/en/thumb/b/bc/Interstellar_film_poster.jpg/220px-Interstellar_film_poster.jpg",
	"https://www.youtube.com/watch?v=zSWdZVtXT7E",
	8.7)


gravity = media.Movie("Gravity",
	"A medical engineer and an astronaut work together to survive after a catastrophe destroys their shuttle and leaves them adrift in orbit.",
	"http://upload.wikimedia.org/wikipedia/en/thumb/f/f6/Gravity_Poster.jpg/220px-Gravity_Poster.jpg",
	"https://www.youtube.com/watch?v=OiTiKOy59o4",
	7.9)

shawshank = media.Movie("The Shawshank Redemption",
	"Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.",
	"http://upload.wikimedia.org/wikipedia/en/thumb/8/81/ShawshankRedemptionMoviePoster.jpg/220px-ShawshankRedemptionMoviePoster.jpg",
	"https://www.youtube.com/watch?v=6hB3S9bIaco",
	9.2)


mystic_river = media.Movie("Mystic River",
	"With a childhood tragedy that overshadowed their lives, three men are reunited by circumstance when one has a family tragedy.",
	"http://upload.wikimedia.org/wikipedia/en/thumb/9/93/Mystic_River_poster.jpg/220px-Mystic_River_poster.jpg",
	"https://www.youtube.com/watch?v=nmiA24jwlbM",
	8.0)

cuckoos = media.Movie("One Flew Over the Cuckoo's Nest",
	"Upon admittance to a mental institution, a brash rebel rallies the patients to take on the oppressive head nurse.",
	"http://upload.wikimedia.org/wikipedia/en/thumb/2/26/One_Flew_Over_the_Cuckoo%27s_Nest_poster.jpg/220px-One_Flew_Over_the_Cuckoo%27s_Nest_poster.jpg",
	"https://www.youtube.com/watch?v=2WSyJgydTsA",
	8.7)

movies = [goodfellas, interstellar, gravity, shawshank, mystic_river, cuckoos]
fresh_tomatoes.open_movies_page(movies)