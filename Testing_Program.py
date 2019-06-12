import unittest
import Encode_And_Decode

class TestEncode_And_Decode(unittest.TestCase):

	#testing the Add_To_Word_List method
	def test_Add_To_Word_List(self):
		#arrange
		Encode_And_Decode.Add_To_Word_List("Hello")
		Encode_And_Decode.Add_To_Word_List("Day")

		#act
		Current_Global_List = Encode_And_Decode.Word_List

		#assert
		self.assertEqual(Current_Global_List, ["Day", "Hello"])

	def test_Clear_Word_List(self):
		#arrange
		Encode_And_Decode.Add_To_Word_List("Hello")
		Encode_And_Decode.Add_To_Word_List("Day")

		#act
		Encode_And_Decode.Clear_Word_List()
		Current_Global_List = Encode_And_Decode.Word_List

		#assert
		self.assertEqual(Current_Global_List, [])

	#method used to set up a word_list for testing
	#this is not a test but a useful method to use for testing
	def Setup_Method(self):
		#arrange
		#clear the list of previous elements
		Encode_And_Decode.Clear_Word_List()
		#add a few random elements to work with
		Encode_And_Decode.Add_To_Word_List("Hello")
		Encode_And_Decode.Add_To_Word_List("Day")
		Encode_And_Decode.Add_To_Word_List("Job")
		Encode_And_Decode.Add_To_Word_List("Birthday")

	#testing the Check_If_In_List method
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
		self.Setup_Method()

		#act
		List_Index = Encode_And_Decode.Check_If_In_List("Day")

		#assert
		self.assertEqual(List_Index, 2)

	def test_Check_If_In_List_Correct_Last_Position(self):
		#arrange
		self.Setup_Method()

		#act
		List_Index = Encode_And_Decode.Check_If_In_List("Hello")

		#assert
		self.assertEqual(List_Index, 3)

	def test_Check_If_In_List_Not_In_List(self):
		#arrange
		self.Setup_Method()

		#act
		List_Index = Encode_And_Decode.Check_If_In_List("Name")

		#assert
		self.assertEqual(List_Index, -1)

	#testing the Move_Word_To_Front_Of_List method
	def test_Move_Word_To_Front_Of_List_From_Front(self):
		#arrange
		self.Setup_Method()

		#act
		Encode_And_Decode.Move_Word_To_Front_Of_List(0)
		Current_Global_List = Encode_And_Decode.Word_List

		#assert
		self.assertEqual(Current_Global_List, ["Birthday", "Job", "Day", "Hello"])

	def test_Move_Word_To_Front_Of_List_From_Middle(self):
		#arrange
		self.Setup_Method()

		#act
		Encode_And_Decode.Move_Word_To_Front_Of_List(2)
		Current_Global_List = Encode_And_Decode.Word_List

		#assert
		self.assertEqual(Current_Global_List, ["Day", "Birthday", "Job", "Hello"])

	def test_Move_Word_To_Front_Of_List_From_End(self):
		#arrange
		self.Setup_Method()

		#act
		Encode_And_Decode.Move_Word_To_Front_Of_List(3)
		Current_Global_List = Encode_And_Decode.Word_List

		#assert
		self.assertEqual(Current_Global_List, ["Hello", "Birthday", "Job", "Day"])

	#this test exposes a flaw in Move_Word_To_Front_Of_List (can not handle negative indexes)
	#def test_Move_Word_To_Front_Of_List_With_Negative(self):
	#	#arrange
	#	self.Setup_Method()
	#
	#	#act
	#	Encode_And_Decode.Move_Word_To_Front_Of_List(-1)
	#	Current_Global_List = Encode_And_Decode.Word_List
	#
	#	#assert
	#	self.assertEqual(Current_Global_List, ["Hello", "Birthday", "Job", "Day"])

	def test_Word_Coding_Under_121(self):
		#arrange
		Word_Index = 2

		#act
		Word_Code = Encode_And_Decode.Word_Coding(Word_Index)

		#assert
		self.assertEqual(Word_Code, chr(130))

	def test_Word_Coding_Between_121_and_374(self):
		#arrange
		Word_Index = 245

		#act
		Word_Code = Encode_And_Decode.Word_Coding(Word_Index)

		#assert
		self.assertEqual(Word_Code, chr(121 + 128) + chr(245 - 121))

	def test_Word_Coding_Over_375(self):
		#arrange
		Word_Index = 500

		#act
		Word_Code = Encode_And_Decode.Word_Coding(Word_Index)

		#assert
		self.assertEqual(Word_Code, chr(122 + 128) + chr((500 - 376) // 256) + chr((500 - 376) % 256))

if __name__ == '__main__':
	unittest.main()
