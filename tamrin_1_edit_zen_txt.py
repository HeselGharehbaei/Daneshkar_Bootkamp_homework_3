import re


with open("Zen.txt", 'r', encoding = 'utf-8') as zen:  
    zen_txt = zen.read()

    
numerical_word_number_dictionery = {
'one': 1, 'two': 2, 'three': 3, 
'four': 4, 'five': 5, 'six': 6, 
'seven': 7, 'eight': 8, 'nine': 9, 
'ten': 10, 'eleven': 11, 'twelve': 12, 
'thirteen': 13, 'fourteen': 14, 
'fifteen': 15, 'sixteen': 16,
'seventeen': 17, 'eighteen': 18,
'nineteen': 19, 'twenty': 20
} 

#Use aregular expression to find all numerical word in the Zen.txt file
numerical_word_patern_for_serching = re.compile(
r'\b(' + '|'.join(numerical_word_number_dictionery.keys()) + r')\b'
)
#Replace numerical word finded in the Zen.txt file with matched numerical value in numerical_word_number_dictionery
edit_zen_txt = numerical_word_patern_for_serching.sub(
lambda match: str(numerical_word_number_dictionery[match.group()]), zen_txt
)


with open("edit_zen.txt", 'w', encoding = 'utf-8') as edit_zen:
    edit_zen.write(edit_zen_txt)