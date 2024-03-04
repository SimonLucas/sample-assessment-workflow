from abc import ABC, abstractmethod


class StatsInterface(ABC):
    """
    Interface for stat summary class that provides a running stat summary
    of a set of data: the number of data points, the mean, the variance,
    """

    @abstractmethod
    def add(self, x: float) -> None:
        pass

    @abstractmethod
    def get_mean(self) -> float:
        pass

    @abstractmethod
    def get_variance(self) -> float:
        pass

    @abstractmethod
    def get_n(self) -> int:
        pass
