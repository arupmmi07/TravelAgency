from abc import ABC, abstractmethod

class Model(ABC):
    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def base_url(self):
        pass

    @abstractmethod
    def temperature(self):
        pass