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

	def test_Check_If_In_List_Correct_First_Position(self):
		#arrange
		Encode_And_Decode.Add_To_Word_List("Hello")
		Encode_And_Decode.Add_To_Word_List("Day")

		#act
		List_Index = Encode_And_Decode.Check_If_In_List("Day")

		#assert
		self.assertEqual(List_Index, 0)

	def test_Check_If_In_List_Correct_Middle_Position(self):
		#arrange
		Encode_And_Decode.Add_To_Word_List("Hello")
		Encode_And_Decode.Add_To_Word_List("Day")
		Encode_And_Decode.Add_To_Word_List("Job")
		Encode_And_Decode.Add_To_Word_List("Birthday")

		#act
		List_Index = Encode_And_Decode.Check_If_In_List("Day")

		#assert
		self.assertEqual(List_Index, 2)

	def test_Check_If_In_List_Correct_Last_Position(self):
		#arrange
		Encode_And_Decode.Add_To_Word_List("Hello")
		Encode_And_Decode.Add_To_Word_List("Day")
		Encode_And_Decode.Add_To_Word_List("Job")
		Encode_And_Decode.Add_To_Word_List("Birthday")

		#act
		List_Index = Encode_And_Decode.Check_If_In_List("Hello")

		#assert
		self.assertEqual(List_Index, 3)

	def test_Check_If_In_List_Not_In_List(self):
		#arrange
		Encode_And_Decode.Add_To_Word_List("Hello")
		Encode_And_Decode.Add_To_Word_List("Day")
		Encode_And_Decode.Add_To_Word_List("Job")
		Encode_And_Decode.Add_To_Word_List("Birthday")

		#act
		List_Index = Encode_And_Decode.Check_If_In_List("Name")

		#assert
		self.assertEqual(List_Index, -1)


if __name__ == '__main__':
	unittest.main()
