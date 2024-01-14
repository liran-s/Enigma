import unittest
from enigma import Rotor, Reflector, Plugboard

class TestRotor(unittest.TestCase):
    wiring = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
    abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    def test_abc_index(self):
        rotor = Rotor(self.wiring)
        for i, c in enumerate(self.abc):
            self.assertEqual(rotor.abc_index(c), i, 'Wrong')

    def test_r_to_l(self):
        rotor = Rotor(self.wiring)
        for i, c in enumerate(self.wiring):
            self.assertEqual(rotor.map_r_to_l(self.abc[i]), c, f'Wrong')

    def test_l_to_r(self):
        rotor = Rotor(self.wiring)
        for i, c in enumerate(self.abc):
            self.assertEqual(rotor.map_l_to_r(self.wiring[i]), c, f'Wrong')

class TestReflector(unittest.TestCase):
    wiring = "YRUHQSLDPXNGOKMIEBFZCWVJAT"
    abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def test_map_refl(self):
        reflector = Reflector(self.wiring)
        for i, c in enumerate(self.wiring):
            self.assertEqual(reflector.map_r_to_l(reflector.map_r_to_l(c)), c, f'Wrong')

class TestPlugboard(unittest.TestCase):
    abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    def test_map_plug(self):

        plugboard = Plugboard([('A','Z'), ('X','Y'),('K','Q'), ('B','C'), ('D','E')])

        for i, c in enumerate(self.abc):
            self.assertEqual(plugboard.map_plug(plugboard.map_plug(c)), c, f'Wrong')

        
if __name__ == '__main__':
    unittest.main()