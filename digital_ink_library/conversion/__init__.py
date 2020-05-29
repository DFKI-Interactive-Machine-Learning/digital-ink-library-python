from abc import ABC, abstractmethod


class BaseDataConversion(ABC):

    @abstractmethod
    def from_sketch(self, sketches):
        """Converts a digital ink sketch to another format."""
        raise NotImplementedError()

    @abstractmethod
    def to_sketch(self, ext_sketches):
        """Converts an external sketch format to a digital ink sketch object."""
        raise NotImplementedError()
