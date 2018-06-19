"""Given two strings s and t, determine whether some anagram of t is a substring of s. For example: if s = "udacity" and t = "ad", then the function returns True. Your function definition should look like: question1(s, t) and return a boolean True or False.
"""


'''My first question is if the string being input will be an English word that can be found in the dictionary, or can it be a string with letters, numbers, ASCII characters, and spaces that the function will need to sort through?

I will assume that it can be anything as long as the data type is a string.  My function will have to check for any character in string form.'''



def question1(s, t):

	#Check if the inputs are valid and are of type string. Return False if not.
    if not s or type(s) != str:
    	return False

    if not t or type(t) != str:
    	return False

    #Remove all spaces from each string.

	s_string = s.replace(" ", "")
	t_string = t.replace(" ", "")

    #Check if the length of s is not less than the length of t

    if len(s_string) < len(t_string):
    	return False

    #Convert the strings into a list of the individual letters of the string

    s_list = list(s_string)
    t_list = list(t_string)

    #Initialize empty sets

    s_set = set()
    t_set = set()

    #Put the contents of the list into the corresponding sets

    for x in s_list:
    	s_set.add(x)

    for y in t_list:
    	t_set.add(y)



    #Check if all characters in t are present in s, otherwise return False

    for letter in t_set:
    	if letter not in s_set:
    		return False

    

    #Initialize empty dictionaries

    letter_tally_s = {}
    letter_tally_t = {}

    #Tally all letters from each set

    for letter_t in t_string:
    	count_t = t.count(letter_t)
    	letter_tally_t[letter_t] = count_t

    for letter_s in s_string:
    	count_s = s.count(letter_s)
    	letter_tally_s[letter_s] = count_s

    #Check if the letter count is the same for all letters in t as in s

    for letter_t in t_set:
    	if letter_tally_t[letter_t] != letter_tally_s[letter_t]:
    		return False

    #If every letter in t_string is in s_tring and each letter has a count equal to its corresponding letter in s_set, return True
    return True

#Should return True
print(question1("udacity", "ad"))
print(question1("abc123", "321cba"))
print(question1("4321", "1234"))
print(question1("abcdabcdabcdabcd", "aaaabbbbccccdddd"))
print(question1("asdgawregasdgasdasdgasbadsfas", "dawreg"))
print(question1("!@#$%^&*() ~", "$%^&"))
print(question1("hello world", "dellrow"))

#Should return False

print(question1("ad", "udacity"))
print(question1("", ""))
print(question1(" ", "hello"))
print(question1(12345, "12345"))
print(question1("12345", 12345))
print(question1(None, "hello"))
print(question1("abc", "aaabbbccc"))

Question 2



Question 3



