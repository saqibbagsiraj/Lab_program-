testFile = open('C:\\Users\\Student\\Desktop\\test.txt', 'r') testContent = testFile.read() 
 word_list = 
 testContent.split() 
 char_dict = {} # Empty dictionary for char in word_list: 
 if char in char_dict: 
   char_dict [char] = char_dict [char] + 1 
  else: 
     char_dict [char] = 1 
 sorted_dict sorted (char_dict.items (), key = lambda item: item [1], reverse = 
 first10pairs list (sorted_dict) [:10] 
 print (first10pairs)
