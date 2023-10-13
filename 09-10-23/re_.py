# import re module
import re

#Defining regEx pattern
pattern = "amazing"

#Createing a regEx object
regex_object = re.compile(pattern)

#String
text = "This tutorial is amazing!"


#Searching for the pattern in the string
match_object = regex_object.search(text)


#Output
print("Match Object:",match_object)


# import re


# pattern = "hello"

# match = re.match(pattern,"hello world")

# print(match)#printing the match object
# print("Span:",match.span())#Return the tuple(start,end)
# print("Start:",match.start())#Return the starting index
# print("End:",match.end())#Return the ending index


# import re    
# line = "Learn Python through tutorials on javatpoint"    
# match_object = re.match( r'.w* (.w?) (.w*?)', line, re.M|re.I)    
    
# if match_object:    
#     print ("match object group : ", match_object.group())    
#     print ("match object 1 group : ", match_object.group(1))    
#     print ("match object 2 group : ", match_object.group(2))    
# else:    
#     print ( "There isn't any match!!" )   



# import re
# line = "Learn Python through tutorials on javatpoint"

# search_object = re.search(r'.*t?(.*t?)(.*t?)',line)

# if search_object:
#     print("search object group :",search_object.group())
#     print("search object group 1:",search_object.group(1))
#     print("search object group 1:",search_object.group(2))

# else:
#     print("Nothing found!!")


# Importing re module  

# import re  
  
# # Defining parameters  
# pattern = "like" # to be replaced  
# repl = "love" # Replacement  
# text = "I like Javatpoint!" # String  
  
# # Returns a new string with a substituted pattern  
# new_text = re.sub(pattern, repl, text)  
  
# # Output  
# print("Original text:", text)  
# print("Substituted text: ", new_text)  


# import re
# m = re.search('(?<=abc)def', 'abcdef')
# m.group(0)