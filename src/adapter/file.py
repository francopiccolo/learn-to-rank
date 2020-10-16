import lightgbm as lgb

class File:
    def __init__(self, file_path):
        self.file_path = file_path

class RankingModelFile(File):
    def __init__(self, path):
        super().__init__(path)

    @property
    def model(self):
        return lgb.Booster(model_file=self.file_path)