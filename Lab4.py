# Method 2 - Using dictionary 
 sentence = "512155461454" 
 char_dict = {} 
 for char in sentence: 
 if char in char_dict: 
 char_dict[char] = char_dict[char] + 1 
 else: 
 char_dict[char] = 1 
 print("Frequency of each digit: ", char_dict) 
 print('-'*50) 
 print(char_dict.keys()) 
 print('-'*50) 
 print(char_dict.values()) 
 print('-'*50) 
 print(char_dict.items())
