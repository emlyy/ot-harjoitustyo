import unittest
from maksukortti import Maksukortti
from kassapaate import Kassapaate

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(350)
        self.kassapaate = Kassapaate()

    def test_kassapaatteen_raha_maara_ja_myytyjen_maara_oikea(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa,100000)
        self.assertEqual(self.kassapaate.edulliset,0)
        self.assertEqual(self.kassapaate.maukkaat,0)
    
    def test_käteisosto_toimii_kun_riittää_edulliseen(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(250),10)
        self.assertEqual(self.kassapaate.kassassa_rahaa,100240)
        self.assertEqual(self.kassapaate.edulliset,1)

    def test_käteisosto_toimii_kun_riittää_maukkaaseen(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(450),50)
        self.assertEqual(self.kassapaate.kassassa_rahaa,100400)
        self.assertEqual(self.kassapaate.maukkaat,1)

    def test_käteisosto_kun_ei_riitä_edulliseen(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(230),230)
        self.assertEqual(self.kassapaate.kassassa_rahaa,100000)
        self.assertEqual(self.kassapaate.edulliset,0)

    def test_käteisosto_kun_ei_riitä_maukkaaseen(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(230),230)
        self.assertEqual(self.kassapaate.kassassa_rahaa,100000)
        self.assertEqual(self.kassapaate.maukkaat,0)

    def test_korttimaksu_toimii_kun_tarpeeksi_rahaa_edulliseen(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti),True)
        self.assertEqual(self.kassapaate.edulliset,1)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 1.10 euroa")
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_korttimaksu_toimii_kun_tarpeeksi_rahaa_maukkaaseen(self):
        kortti = Maksukortti(400)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(kortti),True)
        self.assertEqual(self.kassapaate.maukkaat,1)
        self.assertEqual(str(kortti), "Kortilla on rahaa 0.00 euroa")
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_korttimaksu_ei_toimi_kun_ei_tarpeeksi_rahaa_maukkaaseen(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti),False)
        self.assertEqual(self.kassapaate.maukkaat,0)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 3.50 euroa")
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_korttimaksu_ei_toimi_kun_ei_tarpeeksi_rahaa_edulliseen(self):
        kortti = Maksukortti(200)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(kortti),False)
        self.assertEqual(self.kassapaate.edulliset,0)
        self.assertEqual(str(kortti), "Kortilla on rahaa 2.00 euroa")
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kortille_lataus_toimii(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti,350)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 7.00 euroa")
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100350)
    
    def test_kortille_lataus_ei_toimi_negatiivisella(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti,-350)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 3.50 euroa")
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)