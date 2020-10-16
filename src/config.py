import os
import pickle

STAGE = os.getenv('STAGE')

class ConfigBase:
    def __init__(self):
        self.STAGE = STAGE
        with open('./data/config.pkl', 'rb') as file:
            config = pickle.load(file)
            self.QUERY_FEATURES = config['query_features']
            self.PROPERTY_FEATURES = config['property_features']
            self.CATEGORICAL_FEATURES = config['categorical_features']
            self.MAP_CATEGORY_CODE = config['map_category_code']
        self.RANKING_MODEL_FILE_PATH = './data/model.txt'

class ConfigTest(ConfigBase):
    def __init__(self):
        super().__init__()
        self.NUM_RECOMMENDATIONS = 10

class ConfigDev(ConfigBase):
    pass

class ConfigProd(ConfigBase):
    pass

config = {
    'test': ConfigTest,
    'dev': ConfigDev,
    'prod': ConfigProd
}

config = config[STAGE]()