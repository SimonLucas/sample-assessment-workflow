from provided.stats_interface import StatsInterface


class StatsList(StatsInterface):
    def __init__(self):
        self.data = []

    def add(self, x: float) -> None:
        self.data.append(x)

    def get_mean(self) -> float:
        return sum(self.data) / len(self.data)

    def get_variance(self) -> float:
        return 0.0

    def get_n(self) -> int:
        return len(self.data)
