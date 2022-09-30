from imdb import Cinemagoer

ia = Cinemagoer()

top = ia.get_top250_movies()
bottom = ia.get_bottom100_movies()
print("Top 250 Movies in order are:")
for i in range(250):
    print(top[i])

print("Bottom 100 Movies in order are:")
for i in range(100):
    print(bottom[i])
