import json
import statistics


if __name__ == "__main__":

    movies = json.loads(open("movies.json").read())
    ratings = json.loads(open("ratings.json").read())

    min_year = input("Min year => ")
    print(min_year)

    # get user input max year
    max_year = input("Max year => ")
    print(max_year)

    # get user input IMDB weightage
    imdb_weight = input("Weight for IMDB => ")
    print(imdb_weight)
    imdb_weight = float(imdb_weight)

    # get user input Twitter weightage
    twitter_weight = input("Weight for Twitter => ")
    print(twitter_weight)
    twitter_weight = float(twitter_weight)
    print()
    
    # get list of calc. rating, name of movie, movie year,
    # lowercase genre list from movies & ratings
    # dictionaries, for movies between min-max year
    # and have at least 3 ratings

    result  = [[
                ((imdb_weight*movies[x]['rating'] +\
                  twitter_weight*statistics.mean(ratings[x]))\
                 /(imdb_weight+twitter_weight)), movies[x]['name'], 
                movies[x]['movie_year'], 
                [j.casefold() for j in movies[x]['genre']]] for x in movies
                       if  movies[x]['movie_year'] >= int(min_year) and
                           movies[x]['movie_year'] <= int(max_year) and
                           x in ratings and
                           len(ratings[x]) >= 3]

    # sit in a while loop asking for genre, stop when told stop
    ask_genre = True
    while ask_genre:
        genre = input("What genre do you want to see? ")
        print(genre)
        genre = genre.lower()

        if genre.casefold() == "stop":
            ask_genre = False
            break

        gset = [y for y in result if genre in y[3]]
        
        if gset:
            best = sorted(gset,  reverse=True)[0]

            wrst = sorted(gset, reverse=False)[0]

            print()
            print('Best:')
            print('\tReleased in', str(best[2])+",", best[1], "has a rating of", "{:.2f}".format(best[0]) )
            print()
            print('Worst:')
            print('\tReleased in', str(wrst[2])+",", wrst[1], "has a rating of", "{:.2f}".format(wrst[0]) )
            print()
        else:
            print()
            print('No', genre.title(), 'movie found in', min_year, 'through', max_year)
            print()