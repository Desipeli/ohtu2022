import unittest
from ostoskori import Ostoskori
from tuote import Tuote

class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()

    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(self.kori.tavaroita_korissa(), 0)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_tavara(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)

        self.assertEqual(self.kori.tavaroita_korissa(), 1)

    def test_yhden_tuotteen_lisaamisen_jalkeen_ostoskorin_hinta_on_tuotteen_hinta(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)

        self.assertEqual(self.kori.hinta(), 3)

    def test_kahden_tuotteen_lisaamisen_jalkeen_ostoskorissa_on_2_tavaraa(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        leipa = Tuote("Leipä", 2)
        self.kori.lisaa_tuote(leipa)

        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_ostoskorin_hinta_on_tuotteiden_hintojen_summa(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        leipa = Tuote("Leipä", 2)
        self.kori.lisaa_tuote(leipa)

        self.assertEqual(self.kori.hinta(), 5)

    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_korissa_2_tavaraa(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)

        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    def test_yhden_tuotteen_lisaamisen_jalkeen_ostoskori_sisaltaa_1_ostoksen(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)

        self.assertEqual(len(self.kori.ostokset()), 1)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio_jolla_oikea_tuotteen_nimi_ja_maara(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)

        ostos = self.kori.ostokset()[0]
        self.assertEqual(ostos.tuotteen_nimi(), "Maito")
        self.assertEqual(ostos.lukumaara(), 1)

    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_ostoskorissa_2_ostosta(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        leipa = Tuote("Leipä", 2)
        self.kori.lisaa_tuote(leipa)

        ostokset = self.kori.ostokset()
        self.assertEqual(len(ostokset), 2)

    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_ostoskorissa_yksi_ostos(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)
        ostokset = self.kori.ostokset()

        self.assertEqual(len(ostokset), 1)

    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_korissa_ostos_samalla_nimella_lkm_2(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)
        ostokset = self.kori.ostokset()

        self.assertEqual(ostokset[0].tuotteen_nimi(), "Maito")
        self.assertEqual(ostokset[0].lukumaara(), 2)

    def test_korissa_2_samaa_tuotetta_joista_toinen_poistetaan_jaa_ostos_lkm_1(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)
        self.kori.poista_tuote(maito)
        ostokset = self.kori.ostokset()

        self.assertEqual(ostokset[0].lukumaara(), 1)

    def test_jos_koriin_lisatty_tuote_poistetaan_on_kori_tyhja(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.poista_tuote(maito)
        ostokset = self.kori.ostokset()

        self.assertEqual(len(ostokset), 0)

    def test_metodi_tyhjenna_tyhjentaa_korin(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        leipa = Tuote("Leipä", 2)
        self.kori.lisaa_tuote(leipa)
        self.kori.lisaa_tuote(leipa)
        self.kori.tyhjenna()
        ostokset = self.kori.ostokset()

        self.assertEqual(len(ostokset), 0)