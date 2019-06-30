

class MovieLister:

    def __init__(self, movie_finder):

        self._movie_finder = movie_finder

    def get_all_movies(self):
        return [movie for movie in self._movie_finder.find_all()]

    def get_movies_director(self, director_name):
        """ get movies based on director"""
        return [movie for movie in self._movie_finder.find_all()
                if movie.rstrip().split(',')[2].lower() == director_name.lower()]

    def get_movies_released_in_year(self, year):
        """ get the movies released for the given year """
        return [movie for movie in self._movie_finder.find_all()
                if int(movie.rstrip().split(',')[1]) == int(year)]
