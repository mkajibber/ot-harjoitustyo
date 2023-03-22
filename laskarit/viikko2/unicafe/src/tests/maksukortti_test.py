import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
	def setUp(self):
		self.maksukortti = Maksukortti(1000)


	def test_luotu_kortti_on_olemassa(self):
		self.assertNotEqual(self.maksukortti, None)
        
        
	def test_kortin_saldo_alussa_oikein(self):
		self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")
		
	
	def test_kortin_lataaminen_kasvattaa_saldoa_oikein(self):
		self.maksukortti.lataa_rahaa(1000)
		self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 20.00 euroa")
		
		
#	def test_negatiivisen_summan_lataaminen_ei_muuta_saldoa(self):
#		self.maksukortti.lataa_rahaa(-500)
#		self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")
		
		
	def test_rahan_ottaminen_toimii_oikein_kun_saldo_riittaa(self):
		self.maksukortti.ota_rahaa(500)
		self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 5.00 euroa")
		
		
	def test_rahan_ottaminen_toimii_oikein_kun_saldo_ei_riittava(self):
		self.maksukortti.ota_rahaa(1200)
		self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")
		
		
	def test_rahan_ottaminen_palauttaa_totuusarvon_true(self):
		self.assertEqual(self.maksukortti.ota_rahaa(500), True)
		
		
	def test_rahan_ottaminen_palauttaa_totuusarvon_false(self):
		self.assertEqual(self.maksukortti.ota_rahaa(1200), False)
		
		
		
	
		
		
		
	
        
        
        
