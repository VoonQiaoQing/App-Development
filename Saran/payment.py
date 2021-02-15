class Payment:

    def __init__(self,card_number1,name_on_card, expiry_month, cvv_number, expiry_year):

        self.__card_number1 = card_number1
        # self.__card_number2 = card_number2
        # self.__card_number3 = card_number3
        # self.__card_number4 = card_number4
        self.__name_on_card = name_on_card
        self.__expiry_month = expiry_month
        self.__cvv_number = cvv_number
        self.__expiry_year = expiry_year

    def set_card_number1(self,card_number1):
        self.__card_number1 = card_number1
    # def set_card_number2(self,card_number2):
    #     self.__card_number2 = card_number2
    # def set_card_number3(self,card_number3):
    #     self.__card_number3 = card_number3
    # def set_card_number4(self,card_number4):
    #     self.__card_number4 = card_number4
    def set_name_on_card(self, name_on_card):
        self.__name_on_card = name_on_card
    def set_expiry_month(self,expiry_month):
        self.__expiry_month = expiry_month
    def set_cvv_number(self, cvv_number):
        self.__cvv_number = cvv_number
    def set_expiry_year(self,expiry_year):
        self.__expiry_year = expiry_year
    # def set_promocode(self, promocode):
    #     self.__promocode = promocode

    def get_card_number1(self):
        return self.__card_number1
    # def get_card_number2(self):
    #     return self.__card_number2
    # def get_card_number3(self):
    #     return self.__card_number3
    # def get_card_number4(self):
    #     return self.__card_number4
    def get_name_on_card(self):
        return self.__name_on_card
    def get_expiry_month(self):
        return self.__expiry_month
    def get_cvv_number(self):
        return self.__cvv_number
    def get_expiry_year(self):
        return self.__expiry_year
    # def get_promocode(self):
    #     return self.__promocode


