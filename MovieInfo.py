class MovieInfo:
    movie_id = -1
    def __init__(self,moviename,movieagerating,movieduration,gvexclusivetag,movieHorror,movieDrama,movieComedy,movieScience,movieRomance,movieAnimation,movieCrimeFilm,movieThriller,movieAdventure,movieEmotional,movieMystery,movieAction):
        self.__staff_id = 1               #^movietitle,movieimage
        MovieInfo.movie_id += 1
        self.__movie_id = MovieInfo.movie_id
#        self.__movietitle = movietitle
#        self.__movieimage = movieimage
        self.__moviename = moviename
        self.__movieagerating = movieagerating
        self.__movieduration = movieduration
        self.__gvexclusivetag = gvexclusivetag
        #self.__moviegenres = ["Horror","Drama","Comedy","Science","Romance","Animation","Crime Film","Thriller","Adventure","Emotional","Mystery","Action"]
        self.__movieHorror = movieHorror
        self.__movieDrama = movieDrama
        self.__movieComedy = movieComedy
        self.__movieScience = movieScience
        self.__movieRomance = movieRomance
        self.__movieAnimation = movieAnimation
        self.__movieCrimeFilm = movieCrimeFilm
        self.__movieThriller = movieThriller
        self.__movieAdventure = movieAdventure
        self.__movieEmotional = movieEmotional
        self.__movieMystery = movieMystery
        self.__movieAction = movieAction

    def set_movietitle(self,movietitle):
        self.__movietitle = movietitle
    def set_moviename(self,moviename):
        self.__moviename = moviename
    def set_movieagerating(self,movieagerating):
        self.__movieagerating = movieagerating
    def set_movieduration(self,movieduration):
        self.__movieduration = movieduration
    def set_gvexclusivetag(self,gvexclusivetag):
        self.__gvexclusivetag = gvexclusivetag
    def set_movieimage(self,movieimage):
        self.__movieimage = movieimage
    def set_movieHorror(self,movieHorror):
        self.__movieHorror = movieHorror
    def set_movieDrama(self,movieDrama):
        self.__movieDrama = movieDrama
    def set_movieComedy(self,movieComedy):
        self.__movieComedy = movieComedy

    def set_movieScience(self,movieScience):
        self.__movieScience = movieScience
    def set_movieRomance(self,movieRomance):
        self.__movieRomance = movieRomance
    def set_movieAnimation(self,movieAnimation):
        self.__movieAnimation = movieAnimation

    def set_movieCrimeFilm(self,movieCrimeFilm):
        self.__movieCrimeFilm = movieCrimeFilm
    def set_movieThriller(self,movieThriller):
        self.__movieThriller = movieThriller
    def set_movieAdventure(self,movieAdventure):
        self.__movieAdventure = movieAdventure

    def set_movieEmotional(self,movieEmotional):
        self.__movieEmotional = movieEmotional
    def set_movieMystery(self,movieMystery):
        self.__movieMystery = movieMystery
    def set_movieAction(self,movieAction):
        self.__movieAction = movieAction

    def get_staff_id(self):
        return self.__staff_id
    def get_movie_id(self):
        return self.__movie_id
    def get_movietitle(self):
        return self.__movietitle
    def get_moviename(self):
        return self.__moviename
    def get_movieagerating(self):
        return self.__movieagerating
    def get_movieduration(self):
        return self.__movieduration
    def get_gvexclusivetag(self):
        return self.__gvexclusivetag
    def get_movieimage(self):
        return self.__movieimage
    def get_movieHorror(self):
        return self.__movieHorror
    def get_movieDrama(self):
        return self.__movieDrama
    def get_movieComedy(self):
        return self.__movieComedy

    def get_movieScience(self):
        return self.__movieScience
    def get_movieRomance(self):
        return self.__movieRomance
    def get_movieAnimation(self):
        return self.__movieAnimation

    def get_movieCrimeFilm(self):
        return self.__movieCrimeFilm
    def get_movieThriller(self):
        return self.__movieThriller
    def get_movieAdventure(self):
        return self.__movieAdventure

    def get_movieEmotional(self):
        return self.__movieEmotional
    def get_movieMystery(self):
        return self.__movieMystery
    def get_movieAction(self):
        return self.__movieAction
