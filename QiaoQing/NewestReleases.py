class NewestReleases:
    def __init__(self,release_image1,release_name1,
                 release_image2,release_name2,
                 release_image3,release_name3,
                 release_image4,release_name4):

        self.__homeid = "homeid"
        self.__release_image1 = release_image1
        self.__release_name1 = release_name1
        self.__release_image2 = release_image2
        self.__release_name2 = release_name2
        self.__release_image3 = release_image3
        self.__release_name3 = release_name3
        self.__release_image4 = release_image4
        self.__release_name4 = release_name4

    def set_homeid(self,homeid):
        self.__homeid = homeid
    def set_release_image1(self,release_image1):
        self.__release_image1 = release_image1
    def set_release_image2(self,release_image2):
        self.__release_image2 = release_image2
    def set_release_image3(self,release_image3):
        self.__release_image3 = release_image3
    def set_release_image4(self,release_image4):
        self.__release_image4 = release_image4

    def get_homeid(self):
        return self.__homeid
    def set_release_name1(self,release_name1):
        self.__release_name1 = release_name1
    def set_release_name2(self,release_name2):
        self.__release_name2 = release_name2
    def set_release_name3(self,release_name3):
        self.__release_name3 = release_name3
    def set_release_name4(self,release_name4):
        self.__release_name4 = release_name4

    def get_release_image1(self):
        return self.__release_image1
    def get_release_image2(self):
        return self.__release_image2
    def get_release_image3(self):
        return self.__release_image3
    def get_release_image4(self):
        return self.__release_image4

    def get_release_name1(self):
        return self.__release_name1
    def get_release_name2(self):
        return self.__release_name2
    def get_release_name3(self):
        return self.__release_name3
    def get_release_name4(self):
        return self.__release_name4
