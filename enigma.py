class Rotor:
    wiring = ""
    abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def __init__(self, wiring):
        self.wiring = wiring
        self.offset = 0
                
    def step(self):
        self.offset += 1
        if self.offset % 26 == 0:
            self.offset = 0
            return 1

        return 0        

    def get_step(self):
        return self.offset

    def abc_index(self, c):
        return self.abc.find(c.upper())
        # index = ord(c.upper()) - ord('A')
        # print(f"index of {c} is {index}")
        # return index

    def map_r_to_l(self, c):
        index = (self.abc_index(c) + self.offset) % 26
        return self.wiring[self.abc_index(c)]
    
    def map_l_to_r(self, c):
        index = (self.wiring_index(c) + self.offset) % 26
        return chr(index + ord("A"))
    
    def wiring_index(self, c):
        return self.wiring.find(c.upper())

class Reflector(Rotor):
    def test_map_refl(self, c):
        return self.map_r_to_l(c)
    
class Plugboard():
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

class Enigma():
    def __init__(self, rotor_a, rotor_b,rotor_c, reflector, plugboard):
        self.rotor_a = Rotor(rotor_a)
        self.rotor_b = Rotor(rotor_b)
        self.rotor_c = Rotor(rotor_c)
        self.reflector = Reflector(reflector)
        self.plugboard = Plugboard(plugboard)
        self.offset_a = 0
        self.offset_b = 0
        self.offset_c = 0

    def step(self):
        if (self.rotor_a.step() > 0):
            if (self.rotor_b.step()):
                self.rotor_c.step()
                        
        # print(f'Step {self.rotor_a.get_step()}, {self.rotor_b.get_step()}, {self.rotor_c.get_step()}')

    def cipher_char(self, c):
        self.step()
        c = self.plugboard.map_plug(c)
        c = self.rotor_a.map_r_to_l(c)
        c = self.rotor_b.map_r_to_l(c)
        c = self.rotor_c.map_r_to_l(c)
        c = self.reflector.test_map_refl(c)
        c = self.rotor_c.map_l_to_r(c)
        c = self.rotor_b.map_l_to_r(c)
        c = self.rotor_c.map_l_to_r(c)
        c = self.plugboard.map_plug(c)

        return c
