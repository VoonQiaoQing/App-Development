class HomeImage:
    def __init__(self,homeimage,homepolicy,homepolicyimage):
        self.__homeid = "homeid"
        self.__homepolicy = homepolicy
        self.__homeimage = homeimage
        self.__homepolicyimage = homepolicyimage

    def set_homeid(self,homeid):
        self.__homeid = homeid
    def set_homeimage(self,homeimage):
        self.__homeimage = homeimage
    def set_homepolicy(self,homepolicy):
        self.__homepolicy = homepolicy
    def set_homepolicyimage(self,homepolicyimage):
        self.__homepolicyimage = homepolicyimage

    def get_homeid(self):
        return self.__homeid
    def get_homeimage(self):
        return self.__homeimage
    def get_homepolicyimage(self):
        return self.__homepolicyimage
    def get_homepolicy(self):
        return self.__homepolicy
