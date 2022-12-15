from kivi_paperi_sakset import KiviPaperiSakset


class Peli:
    def __init__(self) -> None:
        self.kps = KiviPaperiSakset()

    def pelaa(self):
        while True:
            print("Valitse pelataanko"
                "\n (a) Ihmistä vastaan"
                "\n (b) Tekoälyä vastaan"
                "\n (c) Parannettua tekoälyä vastaan"
                "\nMuilla valinnoilla lopetetaan"
                )

            vastaus = input()
            peli = self.kps.luo_peli(vastaus)
            if peli:
                peli.pelaa()
            else:
                break

if __name__ == "__main__":
    # main()
    peli = Peli()
    peli.pelaa()
