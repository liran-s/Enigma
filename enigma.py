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
    
class Plugboard():
    plugged = []        
    
    def __init__(self, plugged):
        self.plugged = plugged

        if len(plugged) > 10:
            raise Exception("Error")

    def map_plug(self, c):
        for plug in self.plugged:
            if c == plug[0]:
                # print(f'Return plugged {plug[1]}')
                return plug[1]
            elif c == plug[1]:
                # print(f'Return plugged {plug[0]}')
                return plug[0]
        
        
        return c
