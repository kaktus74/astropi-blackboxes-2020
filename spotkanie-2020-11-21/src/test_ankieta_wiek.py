import unittest
import ankieta_wiek as aw


class AnkietaWiekTest(unittest.TestCase):
    
    def test_czy_liczba(self):
        self.assertEqual(aw.czy_liczba(None), False)
        self.assertEqual(aw.czy_liczba(''), False)
        self.assertEqual(aw.czy_liczba('ala'), False)
        self.assertEqual(aw.czy_liczba('-1'), True)
        self.assertEqual(aw.czy_liczba('0'), True)
        self.assertEqual(aw.czy_liczba('777'), True)
        self.assertEqual(aw.czy_liczba('77.7'), False) #wtf? 

    #TODO-1: napisz test dla funkcji czy_wiek
        
    #TODO-2: napisz test dla funkcji srednia, uwzglednij warunki brzegowe dla tab: None, [];
    #jeśli test wykryje błąd w funkcji, popraw go i przetestuj ponownie    

if __name__ == '__main__':
    unittest.main()
