class Restaurant:
    _all = []

    def __init__(self, name):
        self._name = name
        self._reviews = []
        self._all.append(self)

    def name(self):
        return self._name

    @classmethod
    def all(cls):
        return cls._all

    def reviews(self):
        return self._reviews

    def customers(self):
        return list(set([review.customer() for review in self._reviews]))

    def average_star_rating(self):
        total_ratings = sum([review.rating() for review in self._reviews])
        num_reviews = len(self._reviews)
        if num_reviews == 0:
            return 0
        return total_ratings / num_reviews

    def __str__(self):
        return self._name
