class Faq:
    def __init__(self,questions,rankings,description):
        self.__questions=questions
        self.__ranking=rankings
        self.__description=description

    def set_questions(self,questions):
        self.__questions=questions
    def get_questions(self):
        return self.__questions
    def set_ranking(self,rankings):
        self.__ranking=rankings
    def get_ranking(self):
        return self.__rankings
    def set_description(self,description):
        self.__description=description
    def get_decription(self):
        return self.__description



