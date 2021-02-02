class User:
    count_id = 0

    def __init__(self, rating, review):
        User.count_id += 1
        self.__user_id = User.count_id
        self.__rating = rating
        self.__review = review

    def set_user_id(self, user_id):
        self.__user_id = user_id

    def set_rating(self, rating):
        self.__rating = rating

    def set_review(self, review):
        self.__review = review

    def get_user_id(self):
        return self.__user_id

    def get_rating(self):
        return self.__rating

    def get_review(self):
        return self.__review
