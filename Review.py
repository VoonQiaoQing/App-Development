# moviename, username, rating, review
# moviename, take from saran
# username = take from saran
# rating = customer insert data
# review = customer insert data

# createmovie.html, editmovies.py, movieinfo.py
# __init__.py

class Review:
    def __init__(self, movie_name, username, rating, review):
        self.__movie_name = movie_name
        self.__username = username
        self.__rating = rating
        self.__review = review

    def set_movie_name(self, movie_name):
        self.__movie_name = movie_name

    def set_username(self, username):
        self.__username = username

    def set_rating(self, rating):
        self.__rating = rating

    def set_review(self, review):
        self.__review = review

    def get_movie_name(self):
        return self.__movie_name

    def get_username(self):
        return self.__username

    def get_rating(self):
        return self.__username

    def get_review(self):
        return self.__review

