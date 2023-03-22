import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
	def setUp(self):
		self.kassapaate = Kassapaate()
		self.maksukortti = Maksukortti(1000)
		
		
	def test_luotu_kassapaate_on_olemassa(self):
		self.assertNotEqual(self.kassapaate, None)
		
		
	def test_kassassa_rahamaara_alussa_oikein(self):
		self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
		
		
	def test_kassassa_myytyjen_lounaiden_maara_alussa_oikein(self):
		myytyjen_lukumaara = self.kassapaate.edulliset + self.kassapaate.maukkaat
		self.assertEqual(myytyjen_lukumaara, 0)
		
		
	def test_vaihtoraha_oikein_syodessa_edullisesti_kateisella(self):
		kateinen = 1000
		vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(kateinen)
		self.assertEqual(vaihtoraha, 760)
		
		
	def test_vaihtoraha_oikein_syodessa_maukkaasti_kateisella(self):
		kateinen = 1000
		vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(kateinen)
		self.assertEqual(vaihtoraha, 600)
		
		
	def test_kassan_rahamaara_kasvaa_oikein_syodessa_edullisesti_kateisella(self):
		kateinen = 1000
		self.kassapaate.syo_edullisesti_kateisella(kateinen)
		self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
		
		
	def test_kassan_rahamaara_kasvaa_oikein_syodessa_maukkaasti_kateisella(self):
		kateinen = 1000
		self.kassapaate.syo_maukkaasti_kateisella(kateinen)
		self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)
		
		
	def test_myytyjen_lounaiden_maara_kasvaa_oikein_syodessa_edullisesti_kateisella(self):
		kateinen = 1000
		self.kassapaate.syo_edullisesti_kateisella(kateinen)
		self.assertEqual(self.kassapaate.edulliset, 1)
		
		
	def test_myytyjen_lounaiden_maara_kasvaa_oikein_syodessa_maukkaasti_kateisella(self):
		kateinen = 1000
		self.kassapaate.syo_maukkaasti_kateisella(kateinen)
		self.assertEqual(self.kassapaate.maukkaat, 1)
		
		
	def test_kassassa_oleva_rahamaara_ei_muutu_kun_maksu_ei_ole_riittava_syodessa_edullisesti_kateisella(self):
		kateinen = 200
		self.kassapaate.syo_edullisesti_kateisella(kateinen)
		self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
		
		
	def test_kassassa_oleva_rahamaara_ei_muutu_kun_maksu_ei_ole_riittava_syodessa_maukkaasti_kateisella(self):
		kateinen = 350
		self.kassapaate.syo_maukkaasti_kateisella(kateinen)
		self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
		
		
	def test_koko_maksu_palautuu_vaihtorahana_kun_maksu_ei_riita_syodessa_edullisesti_kateisella(self):
		kateinen = 200
		vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(kateinen)
		self.assertEqual(vaihtoraha, 200)
		
		
	def test_koko_maksu_palautuu_vaihtorahana_kun_maksu_ei_riita_syodessa_maukkaasti_kateisella(self):
		kateinen = 350
		vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(kateinen)
		self.assertEqual(vaihtoraha, 350)
		
		
	def test_myytyjen_lounaiden_maarassa_ei_muutosta_kun_kateinen_raha_ei_riita(self):
		kateinen_edulliseen = 200
		kateinen_maukkaaseen = 350
		self.kassapaate.syo_edullisesti_kateisella(kateinen_edulliseen)
		self.kassapaate.syo_maukkaasti_kateisella(kateinen_maukkaaseen)
		self.assertEqual(self.kassapaate.edulliset + self.kassapaate.maukkaat, 0)
		
		
	def test_veloitetaan_oikea_summa_kun_kortilla_riittavasti_rahaa_syodessa_edullisesti_kortilla(self):
		self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
		self.assertEqual(self.maksukortti.saldo, 760)
		
		
	def test_veloitetaan_oikea_summa_kun_kortilla_riittavasti_rahaa_syodessa_maukkaasti_kortilla(self):
		self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
		self.assertEqual(self.maksukortti.saldo, 600)
		
		
	def test_palautuu_true_kun_kortilla_riittavasti_rahaa_syodessa_edullisesti_kortilla(self):
		palautusarvo = self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
		self.assertEqual(palautusarvo, True)
		
		
	def test_palautuu_true_kun_kortilla_riittavasti_rahaa_syodessa_maukkaasti_kortill(self):
		palautusarvo = self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
		self.assertEqual(palautusarvo, True)
		
		
	def test_myytyjen_lounaiden_maara_kasvaa_oikein_kun_kortilla_riittavasti_rahaa_syodessa_kortilla(self):
		self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
		self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
		self.assertEqual(self.kassapaate.edulliset + self.kassapaate.maukkaat, 2)
		
		
	def test_kortin_rahamaara_ei_muutu_kun_kortilla_ei_riittavasti_rahaa_syodessa_kortilla(self):
		maksukortti_edulliseen = Maksukortti(200)
		maksukortti_maukkaaseen = Maksukortti(350)
		self.kassapaate.syo_edullisesti_kortilla(maksukortti_edulliseen)
		self.kassapaate.syo_maukkaasti_kortilla(maksukortti_maukkaaseen)
		testausarvo = maksukortti_edulliseen.saldo + maksukortti_maukkaaseen.saldo
		odotusarvo = 550
		self.assertEqual(testausarvo, odotusarvo)
		
		
	def test_myytyjen_lukumaara_kassassa_ei_muutu_kun_kortilla_ei_riittavasti_rahaa_syodessa_kortilla(self):
		maksukortti_edulliseen = Maksukortti(200)
		maksukortti_maukkaaseen = Maksukortti(350)
		self.kassapaate.syo_edullisesti_kortilla(maksukortti_edulliseen)
		self.kassapaate.syo_maukkaasti_kortilla(maksukortti_maukkaaseen)
		testausarvo = self.kassapaate.edulliset + self.kassapaate.maukkaat
		odotusarvo = 0
		self.assertEqual(testausarvo, odotusarvo)
		
		
	def test_palautuu_false_kun_kortilla_ei_riittavasti_rahaa_syodessa_edullisesti_kortilla(self):
		maksukortti = Maksukortti(200)
		testausarvo = self.kassapaate.syo_edullisesti_kortilla(maksukortti)
		odotusarvo = False
		self.assertEqual(testausarvo, odotusarvo)
		
		
	def test_palautuu_false_kun_kortilla_ei_riittavasti_rahaa_syodessa_maukkaasti_kortilla(self):
		maksukortti = Maksukortti(350)
		testausarvo = self.kassapaate.syo_maukkaasti_kortilla(maksukortti)
		odotusarvo = False
		self.assertEqual(testausarvo, odotusarvo)
		
		
	def test_kassassa_oleva_rahamaara_ei_muutu_kortilla_syodessa_kun_kortilla_riittavasti_rahaa(self):
		self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
		self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
		self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
		
		
	def test_kortille_rahaa_ladattaessa_kortin_saldo_muuttuu_oikein(self):
		self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 1000)
		testausarvo = self.maksukortti.saldo
		odotusarvo = 2000
		self.assertEqual(testausarvo, odotusarvo)
		
		
	def test_kortille_rahaa_ladattaessa_rahamaara_kassassa_kasvaa_oikein(self):
		self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 1200)
		testausarvo = self.kassapaate.kassassa_rahaa
		odotusarvo = 101200
		self.assertEqual(testausarvo, odotusarvo)
		
		
	def test_kortille_ladattavan_summan_ollessa_negatiivinen_palautuu_none(self):
		testausarvo = self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -5)
		odotusarvo = None
		self.assertEqual(testausarvo, odotusarvo)
		
		
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
