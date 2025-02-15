# Problem: Design Underground System - https://leetcode.com/problems/design-underground-system/

class UndergroundSystem:

    def __init__(self):
        self.check_ins = {}
        self.records = {}
        
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        if id not in self.check_ins:
            self.check_ins[id] = [stationName, t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        if id in self.check_ins:
            fromTo = self.records.get((self.check_ins[id][0], stationName), [0, 0])
            self.records[(self.check_ins[id][0], stationName)] = [fromTo[0] + (t - self.check_ins[id][1]), fromTo[1] + 1]
            del self.check_ins[id]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        if (startStation, endStation) not in self.records:
            return 0
        value = self.records[(startStation, endStation)]
        return value[0] / value[1]

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)