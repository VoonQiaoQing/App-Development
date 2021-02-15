class HomeDescription:
    def __init__(self,homedescription):
        self.__homeid = "homeid"
        self.__homedescription = homedescription

    def set_homeid(self,homeid):
        self.__homeid = homeid
    def set_homedescription(self,homedescription):
        self.__homedescription = homedescription

    def get_homeid(self):
        return self.__homeid
    def get_homedescription(self):
        return self.__homedescription
