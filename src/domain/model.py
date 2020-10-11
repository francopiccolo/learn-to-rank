class Property:
    def __init__(
            self, id, property_type, distance_to_center, dorm_price=None, private_price=None,
            security_score=None, location_score=None, staff_score=None, fun_score=None,
            cleanliness_score=None, value_for_money_score=None, facilities_score=None
            ):
        self.id = id
        self.property_type = property_type
        self.distance_to_center = distance_to_center
        self.dorm_price = dorm_price
        self.private_price = private_price
        self.security_score = security_score
        self.location_score = location_score
        self.staff_score = staff_score
        self.fun_score = fun_score
        self.cleanliness_score = cleanliness_score
        self.value_for_money_score = value_for_money_score
        self.facilities_score = facilities_score

class Query:
    def __init__(
            self, country_id, city_id, device_type, language, nr_guests):
        self.country_id = country_id
        self.city_id = city_id
        self.device_type = device_type
        self.language = language
        self.nr_guests = nr_guests

class RankingModel:
    def __init__(self, model, query_features, property_features):
        self.model = model
        self.query_features = query_features
        self.property_features = property_features

    def rank(self, query, properties):
        ranked_properties = 0
        return ranked_properties

class Recommendations:
    def __init__(self, nr_recommendations):
        self.nr_recommendations = nr_recommendations

    def recommend(self, ranked_properties):
        pass