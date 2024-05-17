class RecoverySystem:
    def __init__(self):
        self.situations = {}
    def add_situation(self, location, situation):
        if location not in self.situations:
            self.situations[location] = []
        self.situations[location].append(situation)
    def get_the_situation(self, location):
        return self.situations.get(location, [])

recovery = RecoverySystem()
recovery.add_situation("Location A", "Flood")
recovery.add_situation("Location B", "Earthquake")
print(recovery.get_the_situation("Location A"))  
print(recovery.get_the_situation("Location B"))  
