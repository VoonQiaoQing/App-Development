#roomtitle = "Rooms Pricings"
#small_roominfo = "Small Room - Up to 2 PAX \ $20"
#med_roominfo = "Medium Room - Up to 4 PAX \ $32"
#large_roominfo = "Large Room - Up to 6 PAX \ $42"
#roomimage = "none atm"
#gvexclusiveprice = "FOR GV EXCLUSIVE / Small Room - Up to 2 PAX \ $28 / Medium Room - Up to 4 PAX \ $40 / Large Room - Up to 6 PAX \ $52"

class RoomInfo:
    def __init__(self,roomtitle,small_roominfo,small_roomimage1,small_roomimage2,med_roominfo,med_roomimage,large_roominfo,large_roomimage1,large_roomimage2,gvexclusiveinfo):
        self.__staff_id = 0
        self.__roomtitle = roomtitle
        self.__small_roominfo = small_roominfo
        self.__med_roominfo = med_roominfo
        self.__large_roominfo = large_roominfo
        self.__small_roomimage1 = small_roomimage1
        self.__small_roomimage2 = small_roomimage2
        self.__med_roomimage = med_roomimage
        self.__large_roomimage1 = large_roomimage1
        self.__large_roomimage2 = large_roomimage2
        self.__gvexclusiveinfo = gvexclusiveinfo

    def set_staff_id(self,staff_id):
        self.__staff_id = staff_id
    def set_roomtitle(self,roomtitle):
        self.__roomtitle = roomtitle
    def set_small_roominfo(self,small_roominfo):
        self.__small_roominfo = small_roominfo
    def set_med_roominfo(self,med_roominfo):
        self.__med_roominfo = med_roominfo
    def set_large_roominfo(self,large_roominfo):
        self.__large_roominfo = large_roominfo
    def set_small_roomimage1(self,small_roomimage1):
        self.__small_roomimage1 = small_roomimage1
    def set_small_roomimage2(self,small_roomimage2):
        self.__small_roomimage2 = small_roomimage2
    def set_med_roomimage(self,med_roomimage):
        self.__med_roomimage = med_roomimage
    def set_large_roomimage1(self,large_roomimage1):
        self.__large_roomimage1 = large_roomimage1
    def set_large_roomimage2(self,large_roomimage2):
        self.__large_roomimage2 = large_roomimage2
    def set_gvexclusiveinfo(self,gvexclusiveinfo):
        self.__gvexclusiveinfo = gvexclusiveinfo

    def get_staff_id(self):
        return self.__staff_id
    def get_roomtitle(self):
        return self.__roomtitle
    def get_small_roominfo(self):
        return self.__small_roominfo
    def get_med_roominfo(self):
        return self.__med_roominfo
    def get_large_roominfo(self):
        return self.__large_roominfo
    def get_small_roomimage1(self):
        return self.__small_roomimage1
    def get_small_roomimage2(self):
        return self.__small_roomimage2
    def get_med_roomimage(self):
        return self.__med_roomimage
    def get_large_roomimage1(self):
        return self.__large_roomimage1
    def get_large_roomimage2(self):
        return self.__large_roomimage2
    def get_gvexclusiveinfo(self):
        return self.__gvexclusiveinfo

#object = MoviesInfo(roomtitle,small_roominfo,med_roominfo,large_roominfo,roomimage,gvexclusiveprice)
#new = object.get_roomtitle()
#print(new)
