class Add_location:
    location_Id = 0

    def __init__(self, location1, location2, location3, location4, location5):
        Add_location.location_Id += 1
        self.__location_Id = Add_location.location_Id
        self.__location1 = location1
        self.__location2 = location2
        self.__location3 = location3
        self.__location4 = location4
        self.__location5 = location5

    def set_location_Id(self, location_Id):
        self.__location_Id = location_Id

    def set_location1(self, location1):
        self.__location1 = location1

    def get_location_Id(self):
        return self.__location_Id

    def get_location1(self):
        return self.__location1

    def set_location2(self, location2):
        self.__location2 = location2

    def set_location3(self, location3):
        self.__location3 = location3

    def set_location4(self, location4):
        self.__location4 = location4

    def set_location5(self, location5):
        self.__location5 = location5


    def get_location2(self):
        return self.__location2

    def get_location3(self):
        return self.__location3

    def get_location4(self):
        return self.__location4

    def get_location5(self):
        return self.__location5


class Add_time:
    time_id = 0

    def __init__(self, time1, time2, time3, time4, time5):
        Add_time.time_id += 1
        self.__time_id = Add_time.time_id
        self.__time1 = time1
        self.__time2 = time2
        self.__time3 = time3
        self.__time4 = time4
        self.__time5 = time5

    def set_time_id(self, time_id):
        self.__time_id = time_id
    def set_time1(self, time1):
        self.__time1 = time1
    def set_time2(self, time2):
        self.__time2 = time2
    def set_time3(self, time3):
        self.__time3 = time3
    def set_time4(self, time4):
        self.__time4 = time4
    def set_time5(self, time5):
        self.__time5 = time5

    def get_time_id(self):
        return self.__time_id
    def get_time1(self):
        return self.__time1
    def get_time2(self):
        return self.__time2
    def get_time3(self):
        return self.__time3
    def get_time4(self):
        return self.__time4
    def get_time5(self):
        return self.__time5

class Admin_date:

    def __init__(self,date1,date2,date3,date4,date5):
        Admin_date.admin_date_Id = 1
        self.__admin_date_Id = Admin_date.admin_date_Id
        self.__date1 = date1
        self.__date2 = date2
        self.__date3 = date3
        self.__date4 = date4
        self.__date5 = date5

    def set_admin_date_Id(self, admin_date_Id):
        self.__admin_date_Id = admin_date_Id

    def set_date1(self, date1):
        self.__date1 = date1
    def set_date2(self, date2):
        self.__date2 = date2
    def set_date3(self, date3):
        self.__date3 = date3
    def set_date4(self, date4):
        self.__date4 = date4
    def set_date5(self, date5):
        self.__date5 = date5

    def get_admin_date_Id(self):
        return self.__admin_date_Id

    def get_date1(self):
        return self.__date1
    def get_date2(self):
        return self.__date2
    def get_date3(self):
        return self.__date3
    def get_date4(self):
        return self.__date4
    def get_date5(self):
        return self.__date5



    # def set_location2(self, location2):
    #     self.__location2 = location2
    #
    # def set_location3(self, location3):
    #     self.__location3 = location3
    #
    # def set_location4(self, location4):
    #     self.__location4 = location4
    #
    # def set_location5(self, location5):
    #     self.__location5 = location5


    # def get_location2(self):
    #     return self.__location2
    #
    # def get_location3(self):
    #     return self.__location3
    #
    # def get_location4(self):
    #     return self.__location4
    #
    # def get_location5(self):
    #     return self.__location5
