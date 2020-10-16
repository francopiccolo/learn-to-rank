import pytest
import pandas as pd
import numpy as np

from config import config
from domain.model import RankingModel, Property, Query
from adapter.file import RankingModelFile
from adapter.repository import FakeRepository

np.random.seed(0)

@pytest.fixture
def ranking_model():
    ranking_model_file = RankingModelFile(config.RANKING_MODEL_FILE_PATH)
    return RankingModel(ranking_model_file.model)

@pytest.fixture
def properties_repo():
    properties_repo = FakeRepository()
    df_properties = pd.read_pickle('./test/data/properties.pkl')
    for i, p in df_properties.iterrows():
        properties_repo.add(
            Property(
                p['property_id'], p['city_id'], p['property_type'], p['distance_to_center'],
                np.random.random()*100, np.random.random()*100, p['security_score'],
                p['location_score'], p['staff_score'], p['fun_score'],
                p['cleanliness_score'], p['value_for_money_score'],
                p['facilities_score']
            )
        )
    return properties_repo

@pytest.fixture
def query():
    city_id = 709
    device_type = 'mobile'
    language = 'english'
    nr_guests = 2
    return Query(city_id, device_type, language, nr_guests)

def test_ranking_model(ranking_model, properties_repo, query):
    ranking = ranking_model.rank(query, properties_repo)
    print(ranking[:10])
    # [(12097.0, -0.19654849286021842), (4371.0, -0.10378978542140786), (8695.0, -0.025944057407561557),
    #  (9363.0, 0.02036439879173103), (19250.0, -0.11052489430637884), (5872.0, -0.1243382270436339),
    #  (18122.0, 0.023465678218124293), (7239.0, -0.07883322832368722), (14380.0, -0.08460605781348653),
    #  (11013.0, -0.07358991313721155)]
    assert isinstance(ranking, list)
