
# Given a string of lowercase letters, write a function to see if the word is a palindrome 
# (the same word spelled forward and backwards).		
# Example Input: 'racecar'
# Example Output: True 

# def find_palindrome(word):
#     if word == word[::-1]:
#         return True
#     else:
#         return False

# print(find_palindrome('kayak'))

def pal2(string):
    return string == string[::-1]
    
print(pal2('kayak'))

