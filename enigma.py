class Rotor:
    wiring = ""
    def __init__(self, wiring):
        self.wiring = wiring
        
    def abc_index(self, c):
        index = ord(c.upper()) - ord('A')
        print(f"index of {c} is {index}")
        return index

    def map_r_to_l(self, c):
        return self.wiring[self.abc_index(c)]
    
    def map_l_to_r(self, c):
        return chr(self.wiring_index(c) + ord("A"))
    
    def wiring_index(self, c):
        return self.wiring.find(c.upper())
