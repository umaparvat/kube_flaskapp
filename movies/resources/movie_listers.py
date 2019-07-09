

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

    def get_movies_by_year_director(self, year, director):
        """
        display the list of movies directed by the directory for the given year
        :param year: the movie was released on which year
        :param director: the movies's director
        :return: the list of movies
        """
        movies = self._movie_finder.find_all()
        movies_list = list()
        for movie in movies:
            if int(movie.rstrip().split(',')[1]) == int(year) and \
                    movie.rstrip().split(',')[2].lower() == director.lower():
                movies_list.append(movie.split(',')[0])
        return movies_list

