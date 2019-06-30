from flask_restplus import Namespace, Resource
from movies.resources.containers import DbMoviesModule, MyMoviesModule
import settings




namespace = Namespace(name="movies", description='The details of the movie')
namespace_db = Namespace(name="movies from db", description='The details of the movie')


@namespace.route("/")
@namespace.response(200, 'success')
@namespace.response(401, 'unauthorized')
@namespace.response(500, 'internal server error')
class MoviesGetter(Resource):
    @namespace.doc('movies', description='To get the movies list by director')
    def get(self):
        try:
            lister = MyMoviesModule.lister()

            #### Manual  Dependecy Injection ###############################################################
            # csv_finder = CsvMovieFinder(movies_model=MoviesModel,
            #                             csv_file_path="c:\\Users\\kauma\\Documents\\Learning\\movies"
            #                                          "\\movies\\resources\\movies.csv", delimiter=",")
            # lister = MovieLister(movie_finder=csv_finder)
            result = lister.get_all_movies()
            if result:
                return {'movies': result}, 200
            else:
                return {'error': 'no content'}, 408
        except Exception as err:
                return {'error': str(err)}, 500

@namespace.route('/<string:director>')
@namespace.response(200, 'success')
@namespace.response(401, 'unauthorized')
@namespace.response(500, 'internal server error')
class MoviesGetter(Resource):

    @namespace.doc('movies', description='To get the movies list by director')
    def get(self, director):
        try:
            if not director:
                return {'error': 'empty input'}, 400
            lister = MyMoviesModule.lister()
            result = lister.get_movies_director(director)
            if result:
                return {'movies': result}, 200
            else:
                return {'error': 'director name not exists'}, 408
        except Exception as err:
                return {'error': str(err)}, 500


@namespace.route('/<int:year>')
@namespace.response(200, 'success')
@namespace.response(401, 'unauthorized')
@namespace.response(500, 'internal server error')
class MoviesGetter(Resource):

    @namespace.doc('movies', description='To get the movies list by director')
    def get(self, year):
        try:
            if not year:
                return {'error': 'empty input'}, 400
            lister = MyMoviesModule.lister()
            result = lister.get_movies_released_in_year(int(year))
            print(result)
            if result:
                return {'movies': result}, 200
            else:
                return {'error': 'No movies released in the given year'}, 408
        except Exception as err:
                return {'error': str(err)}, 500


@namespace_db.route("/")
@namespace_db.response(200, 'success')
@namespace_db.response(401, 'unauthorized')
@namespace_db.response(500, 'internal server error')
class MoviesDbGetter(Resource):
    @namespace_db.doc('movies', description='To get the movies list by director')
    def get(self):
        try:
            print('testing')
            lister = DbMoviesModule.lister()
            #print(dir(lister))
            result = lister.get_all_movies()
            print(dir(result))
            if result:
                return {'movies': result}, 200
            else:
                return {'error': 'no content'}, 408
        except Exception as err:
            return {'error': str(err)}, 500

@namespace_db.route('/<string:director>')
@namespace_db.response(200, 'success')
@namespace_db.response(401, 'unauthorized')
@namespace_db.response(500, 'internal server error')
class MoviesDbGetter(Resource):

    @namespace_db.doc('movies', description='To get the movies list by director')
    def get(self, director):
        try:
            if not director:
                return {'error': 'empty input'}, 400
            lister = DbMoviesModule.lister()
            dir(lister)
            result = lister.get_movies_director(director)
            if result:
                return {'movies': result}, 200
            else:
                return {'error': 'director name not exists'}, 408
        except Exception as err:
                return {'error': str(err)}, 500


@namespace_db.route('/<int:year>')
@namespace_db.response(200, 'success')
@namespace_db.response(401, 'unauthorized')
@namespace_db.response(500, 'internal server error')
class MoviesDbGetter(Resource):

    @namespace_db.doc('movies', description='To get the movies list by director')
    def get(self, year):
        try:
            if not year:
                return {'error': 'empty input'}, 400
            lister = DbMoviesModule.lister()
            result = lister.get_movies_released_in_year(int(year))
            print(result)
            if result:
                return {'movies': result}, 200
            else:
                return {'error': 'No movies released in the given year'}, 408
        except Exception as err:
                return {'error': str(err)}, 500

#   Normal way of writting API layer
# @namespace.route("/")
# @namespace.response(200, 'success')
# @namespace.response(401, 'unauthorized')
# @namespace.response(500, 'internal server error')
# class MoviesGetter(Resource):
#     @namespace.doc('movies', description='To get the movies list by director')
#     def get(self):
#         try:
#             result = MoviesService.get_all_movies()
#             if result:
#                 return {'movies': result}, 200
#             else:
#                 return {'error': 'no content'}, 408
#         except Exception as err:
#                 return {'error': str(err)}, 500
# @namespace.route('/<string:director>')
# @namespace.response(200, 'success')
# @namespace.response(401, 'unauthorized')
# @namespace.response(500, 'internal server error')
# class MoviesGetter(Resource):
#
#     @namespace.doc('movies', description='To get the movies list by director')
#     def get(self, director):
#         try:
#             if not director:
#                 return {'error': 'empty input'}, 400
#             result = MoviesService.get_movies_director(director)
#             if result:
#                 return {'movies': result}, 200
#             else:
#                 return {'error': 'director name not exists'}, 408
#         except Exception as err:
#                 return {'error': str(err)}, 500
#

# @namespace.route('/<int:year>')
# @namespace.response(200, 'success')
# @namespace.response(401, 'unauthorized')
# @namespace.response(500, 'internal server error')
# class MoviesGetter(Resource):
#
#     @namespace.doc('movies', description='To get the movies list by director')
#     def get(self, year):
#         try:
#             if not year:
#                 return {'error': 'empty input'}, 400
#             result = MoviesService.get_movies_released_in_year(int(year))
#             if result:
#                 return {'movies': result}, 200
#             else:
#                 return {'error': 'No movies released in the given year'}, 408
#         except Exception as err:
#                 return {'error': str(err)}, 500
