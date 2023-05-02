class ParkingSystem:

    spaces = [0] * 3

    def __init__(self, big: int, medium: int, small: int):
        self.spaces[0] = big
        self.spaces[1] = medium
        self.spaces[2] = small
        

    def addCar(self, carType: int) -> bool: # big: 1, medium: 2, small: 3
        if (self.spaces[carType - 1] > 0): # space 남음
            self.spaces[carType - 1] -= 1
            return True
        else:
            return False


        


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)