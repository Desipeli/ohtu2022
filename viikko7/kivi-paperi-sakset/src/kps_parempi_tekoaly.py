from tekoaly_parannettu import TekoalyParannettu
from kivi_paperi_sakset import KiviPaperiSakset


class KPSParempiTekoaly(KiviPaperiSakset):
    def __init__(self) -> None:
        self.tekoaly = TekoalyParannettu(10)

    def _toisen_siirto(self, ensimmaisen_siirto: str) -> str:
        siirto = self.tekoaly.anna_siirto()
        self.tekoaly.aseta_siirto(ensimmaisen_siirto)
        return siirto