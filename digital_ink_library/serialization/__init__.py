from abc import ABC, abstractmethod


class BaseDataSerialization(ABC):

    @abstractmethod
    def dump(self, obj, fp):
        raise NotImplementedError()

    @abstractmethod
    def dumps(self, obj):
        raise NotImplementedError()

    @abstractmethod
    def load(self, fp):
        raise NotImplementedError()

    @abstractmethod
    def loads(self, s):
        raise NotImplementedError()
