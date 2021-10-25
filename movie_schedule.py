movies = {"Dune": "15:00",
          "Gaijin": "11:00",
          "The Hobbit": "09:00"}

print("The following movies are showing:")
for movie in movies:
	print(movie)
movie = input("Which movie would you like the viewing time for?\n")

time = movies.get(movie)
if time == None:
    print("That movie is not currently playing")
else:
    print(movie, " is playing at ", time)

