import unittest
from statistics import Statistics
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        self.statistics = Statistics(PlayerReaderStub())
    
    def test_etsi_olemassa_oleva_pelaaja(self):
        pelaaja = self.statistics.search("Kurri")
        self.assertEqual(pelaaja.name, "Kurri")
        self.assertEqual(pelaaja.team, "EDM")
        self.assertEqual(pelaaja.points, 37+53)
    
    def test_etsi_pelaaja_jota_ei_ole(self):
        pelaaja = self.statistics.search("Möttönen")
        self.assertEqual(pelaaja, None)
    
    def test_etsi_joukkoeen_pelaajat(self):
        pelaajat = self.statistics.team("EDM")
        nimet = [x.name for x in pelaajat]
        EDM = [
            "Semenko",
            "Kurri",
            "Gretzky"
        ]
        self.assertListEqual(nimet, EDM)
    
    def test_top_2(self):
        parhaat = self.statistics.top(1)
        parhaiden_nimet = [x.name for x in parhaat]
        vertailu = ["Gretzky", "Lemieux"]
        self.assertListEqual(parhaiden_nimet, vertailu)
        