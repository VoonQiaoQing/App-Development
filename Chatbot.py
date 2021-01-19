class Chatbot:
    def __init__(self,keywords,answers,suggestions):
        self.__keywords=keywords
        self.__answers=answers
        self.__suggestions=suggestions

    def set_keywords(self,keywords):
        self.__keywords=keywords
    def get_keywords(self):
        return self.__keywords
    def set_answers(self,answers):
        self.__answers=answers
    def get_answers(self):
        return self.__answers
    def set_suggestions(self,suggestions):
        self.__suggestions=suggestions
    def get_suggestons(self):
        return self.__suggestions