class FrameAdvCalculator:

    threshold = 3

    def __init__(self, startup, active, recovery):
        self.startup = startup
        self.active = active
        self.recovery = recovery
    
    def isAdvantageous(self):
        if self.recovery <= self.threshold:
            return True
        return False

    def __str__(self):
       return "This Class Calculates Frame Advantage as any move with a recovery <= " + str(self.threshold)