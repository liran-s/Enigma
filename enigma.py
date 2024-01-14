class Rotor:
    wiring = ""
    abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def __init__(self, wiring):
        self.wiring = wiring
                
    def abc_index(self, c):
        return self.abc.find(c.upper())
        # index = ord(c.upper()) - ord('A')
        # print(f"index of {c} is {index}")
        # return index

    def map_r_to_l(self, c):
        return self.wiring[self.abc_index(c)]
    
    def map_l_to_r(self, c):
        return chr(self.wiring_index(c) + ord("A"))
    
    def wiring_index(self, c):
        return self.wiring.find(c.upper())

class Reflector(Rotor):
    def test_map_refl(self, c):
        return self.map_r_to_l(c)