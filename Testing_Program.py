import unittest
import Encode_And_Decode

class TestEncode_And_Decode(unittest.TestCase):

	def test_AddtoList(self):
		#arrange
		Encode_And_Decode.Add_To_Word_List("Hello")
		Encode_And_Decode.Add_To_Word_List("Day")

		#act
		Global_List = Encode_And_Decode.Word_List

		#assert
		self.assertEqual(Global_List, ["Day", "Hello"])

if __name__ == '__main__':
	unittest.main() 

