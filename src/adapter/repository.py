import abc
from domain import model
from typing import List

class AbstractRepository(abc.ABC):

    @abc.abstractmethod
    def add(self, property: model.Property):
        raise NotImplementedError

    @abc.abstractmethod
    def get(self, country_id, city_id) -> List[model.Property]:
        raise NotImplementedError

class FakeRepository(AbstractRepository):
    def __init__(self, properties):
        self.properties = properties

    def add(self, property):
        pass

    def get(self, country_id, city_id):
        return [property for property in self.properties
                if property.country_id == country_id and property.city_id == city_id]