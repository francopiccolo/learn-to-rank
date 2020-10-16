from config import config
from domain.model import Query, RankingModel, Recommendations
from adapter.file import RankingModelFile

ranking_model_file = RankingModelFile(config.RANKING_MODEL_FILE_PATH)
ranking_model = RankingModel(ranking_model_file.model)

def make_recommendations(
        country_id, city_id, device_type,
        language, nr_guests, properties_repository,
        ranking_model=ranking_model):
    query = Query(country_id, city_id, device_type, language, nr_guests)
    properties = properties_repository.get(country_id, city_id)
    ranked_properties = ranking_model.rank(query, properties)
    return Recommendations(ranked_properties)





