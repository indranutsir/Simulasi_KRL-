class Controls:

    def __init__(self):
        self.throttle = 0
        self.brake = 0
        
        #arah
        # -1 reverse
        # 0 neutral
        # 1 forward
        self.direction = 0
        
    def throttle_up(self):
        self.throttle = min(5, self.throttle + 1)

    def throttle_down(self):
        self.throttle = max(0, self.throttle - 1)

    def brake_up(self):
        self.brake = min(4, self.brake + 1)

    def brake_down(self):
        self.brake = max(0, self.brake - 1)
        
    def set_forward(self):
        self.direction = 1
    
    def set_reverse(self):
        self.direction = -1
    
    def set_neutral(self):
        self.direction = 0