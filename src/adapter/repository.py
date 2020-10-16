import abc
from domain import model
from typing import List

class AbstractRepository(abc.ABC):

    @abc.abstractmethod
    def add(self, property: model.Property):
        raise NotImplementedError

    @abc.abstractmethod
    def get(self, city_id) -> List[model.Property]:
        raise NotImplementedError

class FakeRepository(AbstractRepository):
    def __init__(self, properties=None):
        if properties is None:
            self.properties = []
        else:
            self.properties = properties

    def add(self, property):
        self.properties.append(property)

    def get(self, city_id, features):
        property_ids = []
        data = []
        for property in self.properties:
            if property.city_id == city_id:
                property_ids.append(property.id)
                data.append([getattr(property, feature) for feature in features])
        return property_ids, data