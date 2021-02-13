#scales dictionary
#try numbers for the keys, and make the values "scale name: " + [note list]
#or just use scales[#] for each key
scales = {
	"C Ionian (Major Scale)(I)": ['C', 'D', 'E', 'F', 'G', 'A', 'B'],
	"C Dorian (II)": ['', '', '', '', '', '', ''],
	"C Phrygian (III)": ['', '', '', '', '', '', ''],
	"C Lydian (IV)": ['', '', '', '', '', '', ''],
	"C Mixolydian (V)": ['', '', '', '', '', '', ''],
	"C Aeolian (Minor Scale) (VI)": ['', '', '', '', '', '', ''],
	"C Locrian (VII)": ['', '', '', '', '', '', ''],

	"C# Ionian (Major Scale)(I)": ['', '', '', '', '', '', ''],
	"C# Dorian (II)": ['', '', '', '', '', '', ''],
	"C# Phrygian (III)": ['', '', '', '', '', '', ''],
	"C# Lydian (IV)": ['', '', '', '', '', '', ''],
	"C# Mixolydian (V)": ['', '', '', '', '', '', ''],
	"C# Aeolian (Minor Scale) (VI)": ['', '', '', '', '', '', ''],
	"C# Locrian (VII)": ['', '', '', '', '', '', ''],

	"D Ionian (Major Scale)(I)": ['', '', '', '', '', '', ''],
	"D Dorian (II)": ['D', 'E', 'F', 'G', 'A', 'B', 'C'],
	"D Phrygian (III)": ['', '', '', '', '', '', ''],
	"D Lydian (IV)": ['', '', '', '', '', '', ''],
	"D Mixolydian (V)": ['', '', '', '', '', '', ''],
	"D Aeolian (Minor Scale) (VI)": ['', '', '', '', '', '', ''],
	"D Locrian (VII)": ['', '', '', '', '', '', ''],

	"D# Ionian (Major Scale)(I)": ['', '', '', '', '', '', ''],
	"D# Dorian (II)": ['', '', '', '', '', '', ''],
	"D# Phrygian (III)": ['', '', '', '', '', '', ''],
	"D# Lydian (IV)": ['', '', '', '', '', '', ''],
	"D# Mixolydian (V)": ['', '', '', '', '', '', ''],
	"D# Aeolian (Minor Scale) (VI)": ['', '', '', '', '', '', ''],
	"D# Locrian (VII)": ['', '', '', '', '', '', ''],

	"E Ionian (Major Scale)(I)": ['', '', '', '', '', '', ''],
	"E Dorian (II)": ['', '', '', '', '', '', ''],
	"E Phrygian (III)": ['E', 'F', 'G', 'A', 'B', 'C', 'D'],
	"E Lydian (IV)": ['', '', '', '', '', '', ''],
	"E Mixolydian (V)": ['', '', '', '', '', '', ''],
	"E Aeolian (Minor Scale) (VI)": ['', '', '', '', '', '', ''],
	"E Locrian (VII)": ['', '', '', '', '', '', ''],

	"F Ionian (Major Scale)(I)": ['', '', '', '', '', '', ''],
	"F Dorian (II)": ['', '', '', '', '', '', ''],
	"F Phrygian (III)": ['', '', '', '', '', '', ''],
	"F Lydian (IV)": ['F', 'G', 'A', 'B', 'C', 'D', 'E'],
	"F Mixolydian (V)": ['', '', '', '', '', '', ''],
	"F Aeolian (Minor Scale) (VI)": ['', '', '', '', '', '', ''],
	"F Locrian (VII)": ['', '', '', '', '', '', ''],

	"F# Ionian (Major Scale)(I)": ['', '', '', '', '', '', ''],
	"F# Dorian (II)": ['', '', '', '', '', '', ''],
	"F# Phrygian (III)": ['', '', '', '', '', '', ''],
	"F# Lydian (IV)": ['', '', '', '', '', '', ''],
	"F# Mixolydian (V)": ['', '', '', '', '', '', ''],
	"F# Aeolian (Minor Scale) (VI)": ['', '', '', '', '', '', ''],
	"F# Locrian (VII)": ['', '', '', '', '', '', ''],

	"G Ionian (Major Scale)(I)": ['', '', '', '', '', '', ''],
	"G Dorian (II)": ['', '', '', '', '', '', ''],
	"G Phrygian (III)": ['', '', '', '', '', '', ''],
	"G Lydian (IV)": ['', '', '', '', '', '', ''],
	"G Mixolydian (V)": ['G', 'A', 'B', 'C', 'D', 'E', 'F'],
	"G Aeolian (Minor Scale) (VI)": ['', '', '', '', '', '', ''],
	"G Locrian (VII)": ['', '', '', '', '', '', ''],

	"G# Ionian (Major Scale)(I)": "[]",
	"G# Dorian (II)": ['', '', '', '', '', '', ''],
	"G# Phrygian (III)": ['', '', '', '', '', '', ''],
	"G# Lydian (IV)": ['', '', '', '', '', '', ''],
	"G# Mixolydian (V)": ['', '', '', '', '', '', ''],
	"G# Aeolian (Minor Scale) (VI)": ['', '', '', '', '', '', ''],
	"G# Locrian (VII)": ['', '', '', '', '', '', ''],

	"A Ionian (Major Scale)(I)": ['', '', '', '', '', '', ''],
	"A Dorian (II)": ['', '', '', '', '', '', ''],
	"A Phrygian (III)": ['', '', '', '', '', '', ''],
	"A Lydian (IV)": ['', '', '', '', '', '', ''],
	"A Mixolydian (V)": ['', '', '', '', '', '', ''],
	"A Aeolian (Minor Scale) (VI)": ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
	"A Locrian (VII)": ['', '', '', '', '', '', ''],

	"A# Ionian (Major Scale)(I)": ['', '', '', '', '', '', ''],
	"A# Dorian (II)": ['', '', '', '', '', '', ''],
	"A# Phrygian (III)": ['', '', '', '', '', '', ''],
	"A# Lydian (IV)": ['', '', '', '', '', '', ''],
	"A# Mixolydian (V)": ['', '', '', '', '', '', ''],
	"A# Aeolian (Minor Scale) (VI)": ['', '', '', '', '', '', ''],
	"A# Locrian (VII)": ['', '', '', '', '', '', ''],


	"B Ionian (Major Scale)(I)": "[]",
	"B Dorian (II)": ['', '', '', '', '', '', ''],
	"B Phrygian (III)": ['', '', '', '', '', '', ''],
	"B Lydian (IV)": ['', '', '', '', '', '', ''],
	"B Mixolydian (V)": ['', '', '', '', '', '', ''],
	"B Aeolian (Minor Scale) (VI)": ['', '', '', '', '', '', ''],
	"B Locrian (VII)": ['B', 'C', 'D', 'E', 'F', 'G', 'A']
}


'''This part is intended to list the Scale options for the user, 
incase they already know what they want and just need a refresher'''
#The user can also type "menu" to have all the scale options listed
menu = scales.keys()



#if/then statements and inputs, or whatever I need to make a search bar
#I want there to be up to 7 inputs connected by and, with a break in them if nothing is input
#if input length is over 2 characters, only 1 input (for if the user inputs a specific scale)
ui = input()
if ui in scales[""]:
	print scales[0]
