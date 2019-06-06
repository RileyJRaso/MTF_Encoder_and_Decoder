#!/usr/bin/python3

import os
import sys

MAGIC_NUMBER_1 = chr(0xBA) + chr(0x5E) + chr(0xBA) + chr(0x11)
MAGIC_NUMBER_2 = chr(0xBA) + chr(0x5E) + chr(0xBA) + chr(0x12)

Word_List = []

def encode(input_name):
	#creates name for output file
	(base_name, _, _) = input_name.rpartition(".")
	output_name = base_name + "." + "mtf"

	#handling input/output files
	Input_file = open(input_name, encoding = "latin-1", mode = "r",  newline="")
	Output_file = open(output_name, encoding = "latin-1", mode = "w+",  newline="")

	#writing file coding to output file
	Output_file.write(MAGIC_NUMBER_2)

	#varables for use in word processing
	Number_Of_Words = 0
	Boolean_NewLine = 0

	for line in Input_file:
		for word in line.split(" "):
			#handling new lines before word processing
			if word[0] == '\n':
				Output_file.write('\n')
				break
			if word[-1] == '\n':
				word = word[:len(word) - 1]
				Boolean_NewLine = 1

			#checks if the word is currently in our list
			Index_Of_Word = Check_If_In_List(word)

			#handles new words
			if Index_Of_Word == -1:
				Number_Of_Words = Number_Of_Words + 1
				Word_Code = Word_Coding(Number_Of_Words)
				Word_List.insert(0, word)
				Output_file.write(Word_Code)
				Output_file.write(word)
			#Handles words we already know
			if Index_Of_Word >= 0:
				Word_Code = Word_Coding(Index_Of_Word + 1)
				Move_Word_To_Front_Of_List(Index_Of_Word)
				Output_file.write(Word_Code)
			#prints newline if it was attached at the end of a word
			if Boolean_NewLine == 1:
				Output_file.write('\n')
				Boolean_NewLine = 0

	Output_file.close()
	Input_file.close()
	exit(0)

def decode(input_name):
	#output filename creation
	(base_name, _, _) = input_name.rpartition(".")
	output_name = base_name + "." + "txt"

	#file handling
	Input_file = open(input_name, encoding = "latin-1", mode = "r", newline="")
	Output_file = open(output_name, encoding = "latin-1", mode = "w+", newline="")

	#error handling
	File_Code = Input_file.read(4)
	if File_Code != MAGIC_NUMBER_1 and File_Code != MAGIC_NUMBER_2:
		print("invaid file type")
		Input_file.close()
		Output_file.close()
		exit(1)

	#variables to be used in word processing
	Previously_Was_New_Line = 1
	Number_of_Unique_Words = 0
	ch = Input_file.read(1)

	#word Processing
	while ch != '':
		if ord(ch) == 10:
			Output_file.write('\n')
			Previously_Was_New_Line = 1
			ch = Input_file.read(1)

		#handling word codes
		if ch != '' and ord(ch) > 128 and ord(ch) != 10:
			Word_index = Index_Decode(ch,Input_file)
		#handling known words
		if Word_index <= Number_of_Unique_Words and ord(ch) != 10:
			Move_Word_To_Front_Of_List(Word_index - 1)
			# if the next word is not the first word on a line you need to add a space, this next if does that
			if Previously_Was_New_Line == 0:
				Output_file.write(' ')
			Output_file.write(Word_List[0])
			Previously_Was_New_Line = 0
			ch = Input_file.read(1)
		#handling new words
		if Word_index > Number_of_Unique_Words and ord(ch) != 10:
			Number_of_Unique_Words = Number_of_Unique_Words + 1
			ch = Input_file.read(1)
			word = ''
			while ord(ch) < 128 and ch != '' and ord(ch) != 10:
				word = word + ch
				ch = Input_file.read(1)
			if Previously_Was_New_Line == 0:
				Output_file.write(' ')
			Output_file.write(word)
			Previously_Was_New_Line = 0
			Word_List.insert(0, word)
		#handling new lines after a new word
		if ch != '' and ord(ch) == 10:
			Output_file.write('\n')
			Previously_Was_New_Line = 1
			ch = Input_file.read(1)

	Output_file.close()
	Input_file.close()
	exit(0)

def Check_If_In_List(Current_Word):
	#checks our list for the word
	#returns -1 if not in list
	#returns Index if in list
	global Word_List
	try:
		Word_Index = Word_List.index(Current_Word)
		return Word_Index
	except ValueError:
		return -1

def Word_Coding(Number_Of_Words):
	Code_String = '0'
	#dealing with words under 121
	if Number_Of_Words < 121:
		Code_String = chr(Number_Of_Words + 128)
	#dealing with words over 120
	elif Number_Of_Words < 376:
		Code_String = chr(121 + 128) + chr(Number_Of_Words - 121)
	#dealing with codes over 375
	else:
		Code_String = chr(122 + 128) + chr((Number_Of_Words - 376) // 256) + chr((Number_Of_Words - 376) % 256)
	return Code_String

def Move_Word_To_Front_Of_List(Index_Of_Word):
	#moves word to front of the list
	global Word_List

	Temp_Hold_Word = Word_List[Index_Of_Word]
	i = Index_Of_Word
	while i > 0:
		Word_List[i] = Word_List[i-1]
		i = i - 1
	Word_List[0] = Temp_Hold_Word
	return

def Index_Decode(First_Code,Input_file):
	First_Code = ord(First_Code) - 128
	Index = 0
	#looks at first code and figures out word code from the three cases
	if First_Code < 121:
		#words under 121
		Index = First_Code
	elif First_Code == 121:
		#words over 120 and under 376
		Index = 121
		Second_Code = Input_file.read(1)
		Second_Code = ord(Second_Code)
		Index = Index + Second_Code
	elif First_Code == 122:
		#words over 375
		Index = 376
		Second_Code = Input_file.read(1)
		Second_Code = ord(Second_Code) * 256
		Thrid_Code = Input_file.read(1)
		Thrid_Code = ord(Thrid_Code)
		Index = Index + Second_Code + Thrid_Code
	return Index

def Add_To_Word_List(Word):
	#Function used in Testing
	Word_List.insert(0, Word)
	return
