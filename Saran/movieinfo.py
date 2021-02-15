class MovieInfo:
    def __init__(self, movieimage,moviename,movieagerating,movieduration):

                 #^movietitle,movieimage
        self.__movieimage = movieimage
        self.__moviename = moviename
        self.__movieagerating = movieagerating
        self.__movieduration = movieduration
    # def set_movieid(self, movieid):
    #     self.__movieid = movieid
    def set_movieimage(self,movieimage):
        self.__movieimage = movieimage
    def set_moviename(self,moviename):
        self.__moviename = moviename
    def set_movieagerating(self,movieagerating):
        self.__movieagerating = movieagerating
    def set_movieduration(self,movieduration):
        self.__movieduration = movieduration

    # def get_movieid(self):
    #     return self.__movieid
    def get_movieimage(self):
        return self.__movieimage
    def get_moviename(self):
        return self.__moviename
    def get_movieagerating(self):
        return self.__movieagerating
    def get_movieduration(self):
        return self.__movieduration

