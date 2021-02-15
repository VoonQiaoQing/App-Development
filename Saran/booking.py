class Booking:
    def __init__(self, Date, Time, location):
        self.__Date = Date
        self.__Time = Time
        self.__location = location
        # self.__roomtype = roomtype



    def set_Date(self, Date):
        self.__Date = Date
    def set_Time(self, Time):
        self.__Time = Time
    def set_location(self, location):
        self.__location = location
    def get_Date(self):
        return self.__Date
    def get_Time(self):
        return self.__Time
    def get_location(self):
        return self.__location
class Roomtype:
    def __init__(self,num,ref,roomtype,moviname,Date,Time,location):
        self.__num = num
        self.__ref = ref
        self.__roomtype = roomtype
        self.__moviename = moviname
        self.__Date = Date
        self.__Time = Time
        self.__location = location

    def get_num(self):
         return self.__num
    def get_ref(self):
        return self.__ref
    def get_roomtype(self):
         return self.__roomtype
    def get_moviename(self):
        return self.__moviename
    def set_ref(self,ref):
        self.__ref = ref
    def set_moviename(self, moviename):
        self.__moviename = moviename
    def set_roomtype(self, roomtype):
         self.__roomtype = roomtype
    def set_num(self, num):
        self.__numm = num
    def set_Date(self, Date):
        self.__Date = Date
    def set_Time(self, Time):
        self.__Time = Time
    def set_location(self, location):
        self.__location = location
    def get_Date(self):
        return self.__Date
    def get_Time(self):
        return self.__Time

    def get_location(self):
        return self.__location
class Booked:
    def __init__(self, customerid,ref,moviename, Date, Time, location,roomtype):
        self.__customerid = customerid
        self.__ref = ref
        self.__moviename = moviename
        self.__Date = Date
        self.__Time = Time
        self.__location = location
        self.__roomtype = roomtype
    def get_ref(self):
        return self.__ref
    def set_ref(self,ref):
        self.__ref =ref
    def set_customerid(self, customerid):
        self.__customerid = customerid
    def set_moviename(self, moviename):
        self.__moviename = moviename
    def set_Date(self, Date):
        self.__Date = Date
    def set_Time(self, Time):
        self.__Time = Time
    def set_location(self, location):
        self.__location = location
    def set_roomtype(self, roomtype):
        self.__roomtype = roomtype
    def get_customerid(self):
        return self.__customerid
    def get_moviename(self):
        return self.__moviename
    def get_Date(self):
        return self.__Date
    def get_Time(self):
        return self.__Time
    def get_location(self):
        return self.__location
    def get_roomtype(self):
        return self.__roomtype
class Left:
     def __init__(self,small_left,medium_left,big_left):
         self.__small_left = small_left
         self.__medium_left = medium_left
         self.__big_left = big_left

     def set_small_left(self,small_left):
        self.__small_left = small_left
     def medium_left(self, medium_left):
        self.__medium_left = medium_left
     def set_big_left(self, big_left):
        self.__big_left = big_left
     def get_small_left(self):
        return self.__small_left
     def get_medium_left(self):
        return self.__medium_left
     def get_big_left(self):
        return self.__big_left
class Code:
     def __init__(self,Id,small_code,medium_code,big_code,small_discount,medium_discount,big_discount):
         self.__small_code = small_code
         self.__medium_code = medium_code
         self.__big_code = big_code
         self.__small_discount = small_discount
         self.__medium_discount = medium_discount
         self.__big_discount = big_discount
         self.__Id =Id
     def set_Id(self,Id):
        self.__Id = Id
     def set_small_code(self,small_code):
        self.__small_code = small_code
     def medium_code(self, medium_code):
        self.__medium_code = medium_code
     def set_big_code(self, big_code):
        self.__big_code = big_code
     def set_small_discount(self,small_discount):
        self.__small_discount = small_discount
     def medium_discount(self, medium_discount):
        self.__medium_discount = medium_discount
     def set_big_discount(self, big_discount):
        self.__big_discount = big_discount

     def get_small_discount(self):
        return self.__small_discount
     def get_medium_discount(self):
        return self.__medium_discount
     def get_big_discount(self):
        return self.__big_discount
     def get_Id(self):
        return self.__Id
     def get_small_code(self):
        return self.__small_code
     def get_medium_code(self):
        return self.__medium_code
     def get_big_code(self):
        return self.__big_code
class Promocode:
    def __init__(self,Id,promocode,roomtype):
        self.__Id =Id
        self.__promocode = promocode
        self.__roomtype = roomtype

    def set_Id(self,Id):
        self.__Id = Id
    def set_roomtype(self,roomtype):
        self.__roomtype = roomtype
    def set_promocode(self,promocode):
        self.__promocode = promocode
    def get_Id(self):
        return self.__Id
    def get_promocode(self):
        return self.__promocode
    def get_roomtype(self):
        return self.__roomtype
