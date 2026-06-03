from sortedcontainers import SortedDict

class TimeMap:

    def __init__(self):
        self.map: dict[dict[int, str]] = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.map:
            self.map[key][timestamp] = value
        else:
            self.map[key] = SortedDict()
            self.map[key][timestamp] = value
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ""
        times = self.map[key]
        for time in reversed(times.keys()):
            if time <= timestamp:
                return self.map[key][time]
        return ""