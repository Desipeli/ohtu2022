from tuomari import Tuomari


class KiviPaperiSakset:
    def pelaa(self):
        print("Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s")
        tuomari = Tuomari()

        ekan_siirto = self._ensimmaisen_siirto()
        tokan_siirto = self._toisen_siirto(ekan_siirto)

        while self._onko_ok_siirto(ekan_siirto) and self._onko_ok_siirto(tokan_siirto):
            tuomari.kirjaa_siirto(ekan_siirto, tokan_siirto)
            print(tuomari)

            ekan_siirto = self._ensimmaisen_siirto()
            tokan_siirto = self._toisen_siirto(ekan_siirto)

            print(f"Toinen pelaaja valitsi: {tokan_siirto}")

        print("Kiitos!")
        print(tuomari)

    def _ensimmaisen_siirto(self) -> str:
        return input("Ensimmäisen pelaajan siirto: ")

    def _toisen_siirto(self, ensimmaisen_siirto: str) -> str:
        return "k"

    def _onko_ok_siirto(self, siirto: str) -> bool:
        return siirto == "k" or siirto == "p" or siirto == "s"

    def luo_peli(self, tyyppi: str) -> object:
        from tehdas import luo_peli
        return luo_peli(tyyppi)