from domain.model import Query, RankingModel

def make_recommendations(country_id, city_id, device_type,
                         language, nr_guests, properties_repository):
    properties = properties_repository.get(country_id, city_id)
    query = Query(country_id, city_id, device_type, language, nr_guests)
    return





