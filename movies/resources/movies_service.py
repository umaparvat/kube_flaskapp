# from movies.core.exceptions import MoviesError
# import os
###################################3
# normal all codes in one function
#  Here file read and parsing the result both are in same function
#####################################
# class MoviesService:
#
#     @staticmethod
#     def get_all_movies():
#         try:
#             file_path = os.path.join(os.path.dirname(__file__), 'movies.csv')
#             with open(file_path, 'r') as fr:
#                 listmovies = fr.readlines()
#             if listmovies:
#                 return listmovies
#             else:
#                 return []
#         except IOError as ier:
#             print('error')
#             raise Exception('IO Exception occurred')
#
#
#     @staticmethod
#     def get_movies_by_director(director_name):
#         """get the movies by director_name"""
#         try:
#             file_path = os.path.join(os.path.dirname(__file__), 'movies.csv')
#             with open(file_path, 'r') as fr:
#                 listmovies = fr.readlines()
#             for index, movie_detail in enumerate(listmovies):
#                 movie_name, year, director_name = movie_detail.rstrip().split(',')
#                 if director_name.lower() == director_name.lower():
#                     listmovies.pop(index)
#             if listmovies:
#                 return listmovies
#             else:
#                 return []
#         except IOError as ier:
#             print('error')
#             raise Exception('IO Exception occurred')
#
#     @staticmethod
#     def get_movies_by_year(year):
#         """ Get the movies which are released in that year"""
#         try:
#             file_path = os.path.join(os.path.dirname(__file__), 'movies.csv')
#             with open(file_path, 'r') as fr:
#                 listmovies = fr.readlines()
#             for index, movie_detail in enumerate(listmovies):
#                 movie_name, year, director_name = movie_detail.rstrip().split(',')
#                 if int(year) == year:
#                     listmovies.pop(index)
#             if listmovies:
#                 return listmovies
#             else:
#                 return []
#         except IOError as ier:
#             raise Exception('IO Exception occurred')


###################################################
# Dependency Injection with __init__ way
##################################################
class MovieFinder(object):
    def __init__(self, model_name):
        self._model = model_name

    def find_all(self):
        raise NotImplementedError


class CsvMovieFinder(MovieFinder):

    def __init__(self, movies_model, csv_file_path, delimiter):
        self._csv_file_path = csv_file_path
        self._delimiter = delimiter
        super().__init__(movies_model)

    def find_all(self):
        with open(self._csv_file_path, 'r') as csv_file:
            result = csv_file.readlines()
        return result

class SQliteMovieFinder(MovieFinder):
    def __init__(self, database, movies_model):
        self._database = database
        super().__init__(movies_model)

    def find_all(self):
        """Return all found movies.
        :rtype: list[movies.models.Movie]
        :return: List of movie instances.
        """
        with self._database:
            rows = self._database.execute('SELECT name, year, director '
                                          'FROM movies')
            print(rows)
            st = [",".join(list(map(str, row))) for row in rows]
            print(st[0])
            # print(st)
            return st





# if __name__ == "__main__":
#     x = MoviesService.get_movies_by_director('FrancisLawrence')
#     print(x)