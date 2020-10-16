import pandas as pd

from config import config

class Property:
    def __init__(
            self, id, city_id, property_type, distance_to_center, dorm_price=None, private_price=None,
            security_score=None, location_score=None, staff_score=None, fun_score=None,
            cleanliness_score=None, value_for_money_score=None, facilities_score=None
            ):
        self.id = id
        self.city_id = city_id
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
            self, city_id, device_type, language, nr_guests):
        self.city_id = city_id
        self.device_type = device_type
        self.language = language
        self.nr_guests = nr_guests

class RankingModel:
    def __init__(self, model,
                 query_features=config.QUERY_FEATURES,
                 property_features=config.PROPERTY_FEATURES,
                 categorical_features=config.CATEGORICAL_FEATURES,
                 map_category_code=config.MAP_CATEGORY_CODE):
        self.model = model
        self.query_features = query_features
        self.property_features = property_features
        self.categorical_features = categorical_features
        self.map_category_code = map_category_code

    def rank(self, query, properties_repo):
        property_ids, properties = properties_repo.get(query.city_id, self.property_features)
        X = pd.DataFrame(properties, columns=self.property_features)
        for feature in self.query_features:
            X[feature] = getattr(query, feature)
        X = X[self.query_features + self.property_features]
        for feature in self.categorical_features:
            X[feature] = X[feature].replace(self.map_category_code[feature])
        scores = self.model.predict(X)
        return list(zip(property_ids, scores))

class Recommendations:
    def __init__(self, num_recommendations=config.NUM_RECOMMENDATIONS):
        self.num_recommendations = num_recommendations

    def recommend(self, properties_ranking):
        pass
