import dependency_injector.providers as providers
from movies.resources.movies_service import MovieFinder, SQliteMovieFinder, CsvMovieFinder
from  movies.resources.movie_listers import MovieLister
from movies.models import movies as MoviesModel
import dependency_injector.containers as containers
import sqlite3
import settings

# class Configs(containers.DeclarativeContainer):
#     config = providers.Configuration('config')
#     # other configs


# class Clients(containers.DeclarativeContainer):
#     email_client = providers.Singleton(EmailClient, Configs.config)
#     # other clients


class MovieModuleContainer(containers.DeclarativeContainer):
    # movie_model = providers.Factory(MovieModel)
    movie_finder_abs = providers.AbstractFactory(MovieFinder, model_name=MoviesModel)
    lister = providers.Factory(MovieLister, movie_finder=movie_finder_abs)



@containers.override(MovieModuleContainer)
class MyMoviesModule(MovieModuleContainer):
    """IoC container for overriding movies module component providers."""
    # overriding the abstract class.
    movie_finder_abs = providers.Factory(CsvMovieFinder,
                               csv_file_path="c:\\Users\\kauma\\Documents\\Learning\\movies"
                                             "\\movies\\resources\\movies.csv",
                               delimiter=',',
                               movies_model=MoviesModel
                               )




class ResourcesModule(containers.DeclarativeContainer):
    """IoC container of application resource providers."""

    database = providers.Singleton(sqlite3.connect, settings.MOVIES_DB_PATH, check_same_thread=False)


@containers.copy(MovieModuleContainer)
class DbMoviesModule(MovieModuleContainer):
    """IoC container for overriding movies module component providers."""

    movie_finder_abs = providers.Factory(SQliteMovieFinder,
                               database=ResourcesModule.database,
                               movies_model=MoviesModel)



