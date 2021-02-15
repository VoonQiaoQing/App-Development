#roomtitle = "Rooms Pricings"
#small_roominfo = "Small Room - Up to 2 PAX \ $20"
#med_roominfo = "Medium Room - Up to 4 PAX \ $32"
#large_roominfo = "Large Room - Up to 6 PAX \ $42"
#roomimage = "none atm"
#gvexclusiveprice = "FOR GV EXCLUSIVE / Small Room - Up to 2 PAX \ $28 / Medium Room - Up to 4 PAX \ $40 / Large Room - Up to 6 PAX \ $52"

class RoomInfo:
    def __init__(self,roomtitle,small_roominfo,small_roomprice,
                 small_roomimage1,small_roomimage2,
                 med_roominfo,med_roomprice,med_roomimage,
                 large_roominfo,large_roomprice,
                 large_roomimage1,large_roomimage2,
                 gvexclusivesmall_roominfo,gvexclusivesmall_roomprice,
                 gvexclusivemed_roominfo,gvexclusivemed_roomprice,
                 gvexclusivelarge_roominfo,gvexclusivelargeroomprice):

        self.__staff_id = 0
        self.__roomid = "RoomInfo"
        self.__roomtitle = roomtitle
        self.__small_roominfo = small_roominfo
        self.__small_roomprice = small_roomprice
        self.__med_roominfo = med_roominfo
        self.__med_roomprice = med_roomprice
        self.__large_roominfo = large_roominfo
        self.__large_roomprice = large_roomprice
        self.__small_roomimage1 = small_roomimage1
        self.__small_roomimage2 = small_roomimage2
        self.__med_roomimage = med_roomimage
        self.__large_roomimage1 = large_roomimage1
        self.__large_roomimage2 = large_roomimage2

        self.__gvexclusivesmall_roominfo = gvexclusivesmall_roominfo
        self.__gvexclusivesmall_roomprice = gvexclusivesmall_roomprice
        self.__gvexclusivemed_roominfo = gvexclusivemed_roominfo
        self.__gvexclusivemed_roomprice = gvexclusivemed_roomprice
        self.__gvexclusivelarge_roominfo = gvexclusivelarge_roominfo
        self.__gvexclusivelargeroomprice = gvexclusivelargeroomprice


    def set_staff_id(self,staff_id):
        self.__staff_id = staff_id
    def set_roomid(self,roomid):
        self.__roomid = roomid
    def set_roomtitle(self,roomtitle):
        self.__roomtitle = roomtitle
    def set_small_roominfo(self,small_roominfo):
        self.__small_roominfo = small_roominfo
    def set_med_roominfo(self,med_roominfo):
        self.__med_roominfo = med_roominfo
    def set_large_roominfo(self,large_roominfo):
        self.__large_roominfo = large_roominfo
    def set_small_roomprice(self,small_roomprice):
        self.__small_roomprice = small_roomprice
    def set_med_roomprice(self,med_roomprice):
        self.__med_roomprice = med_roomprice
    def set_large_roomprice(self,large_roomprice):
        self.__large_roomprice = large_roomprice
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

    def set_gvexclusivesmall_roominfo(self,gvexclusivesmall_roominfo):
        self.__gvexclusivesmall_roominfo = gvexclusivesmall_roominfo
    def set_gvexclusivesmall_roomprice(self,gvexclusivesmall_roomprice):
        self.__gvexclusivesmall_roomprice = gvexclusivesmall_roomprice
    def set_gvexclusivemed_roominfo(self,gvexclusivemed_roominfo):
        self.__gvexclusivemed_roominfo = gvexclusivemed_roominfo
    def set_gvexclusivemed_roomprice(self,gvexclusivemed_roomprice):
        self.__gvexclusivemed_roomprice = gvexclusivemed_roomprice
    def set_gvexclusivelarge_roominfo(self,gvexclusivelarge_roominfo):
        self.__gvexclusivelarge_roominfo = gvexclusivelarge_roominfo
    def set_gvexclusivelargeroomprice(self,gvexclusivelargeroomprice):
        self.__gvexclusivelargeroomprice = gvexclusivelargeroomprice

    def get_staff_id(self):
        return self.__staff_id
    def get_roomid(self):
        return self.__roomid
    def get_roomtitle(self):
        return self.__roomtitle
    def get_small_roominfo(self):
        return self.__small_roominfo
    def get_med_roominfo(self):
        return self.__med_roominfo
    def get_large_roominfo(self):
        return self.__large_roominfo

    def get_small_roomprice(self):
        return self.__small_roomprice
    def get_med_roomprice(self):
        return self.__med_roomprice
    def get_large_roomprice(self):
        return self.__large_roomprice

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

    def get_gvexclusivesmall_roominfo(self):
        return self.__gvexclusivesmall_roominfo
    def get_gvexclusivesmall_roomprice(self):
        return self.__gvexclusivesmall_roomprice
    def get_gvexclusivemed_roominfo(self):
        return self.__gvexclusivemed_roominfo
    def get_gvexclusivemed_roomprice(self):
        return self.__gvexclusivemed_roomprice
    def get_gvexclusivelarge_roominfo(self):
        return self.__gvexclusivelarge_roominfo
    def get_gvexclusivelargeroomprice(self):
        return self.__gvexclusivelargeroomprice

#object = MoviesInfo(roomtitle,small_roominfo,med_roominfo,large_roominfo,roomimage,gvexclusiveprice)
#new = object.get_roomtitle()
#print(new)
