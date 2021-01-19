class User:
    count_id = 0

    def __init__(self,Question,Reason,Availability,NumberOfPeople,remarks):
        User.count_id +=1
        self.__user_id = User.count_id
        self.__Question= Question
        self.__Reason= Reason
        self.__Availability= Availability
        self.__NumberOfPeople= NumberOfPeople
        self.__remarks= remarks

    def set_user_id(self,user_id):
        self.__user_id=user_id
    def set_Question(self,Question):
        self.__Question=Question
    def set_Reason(self,Reason):
        self.__Reason=Reason
    def set_Availability(self,Availability):
        self.__Availability=Availability
    def set_NumberOfPeople(self,NumberOfPeople):
        self.__NumberOfPeople=NumberOfPeople
    def set_remarks(self,remarks):
        self.__remarks=remarks

    def get_user_id(self):
        return self.__user_id
    def get_Question(self):
        return self.__Question
    def get_Reason(self):
        return self.__Reason
    def get_Availability(self):
        return self.__Availability
    def get_NumberOfPeople(self):
        return self.__NumberOfPeople
    def get_remarks(self):
        return self.__remarks
