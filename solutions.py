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

string = "dcknseshhhhnursesrunhhhrun..xxxxxx"


def question2(s):
  
  str1 = s
  word = ""
  longest = ""
  start = 1
  before = start - 1
  after = start + 1

  if not str1 or type(str1) != str:
    return False

  if len(str1) < 2:
    return False

  if str1 == str1[::-1]:
    return str1

  if str1[len(str1)-2] == str1[len(str1)-1]:
    longest = str1[len(str1)-2:len(str1)]

  for x in range(1, len(str1)-2):

    if str1[before] == str1[start]:
      consec = consecutive(str1, before, start)
      if len(consec) > len(longest):
        longest = consec
      start +=1
      before += 1
      after += 1


    elif str1[before] != str1[after]:
      start +=1
      before += 1
      after += 1
      
    elif str1[before] == str1[after]:
      word = palindrome(str1, before, after)
      start += 1
      before += 1
      after += 1
      if len(word) > len(longest):
        longest = word
  return longest
      


def palindrome(stng, bef, aft): 
  
  if stng[bef] != stng[aft]:
    return stng[bef+1:aft]
  elif bef == 0 or aft == len(stng)-1:
    return stng[bef:aft+1]
  else:
    return palindrome(stng, bef-1, aft+1)

def consecutive(stng, b, st):
  if st == len(stng)-1:
    return stng[b:st+1]
  elif stng[b] != stng[st+1]:
    return stng[b:st+1]
  else:
    return consecutive(stng, b, st+1)
 

print(question2(string))

Question 3


def question3(g):

    graph = g
    vert_set = []
    edges = set()
    tree_set = []
    chosen_edges = []
    final_output = {}

    if type(graph) != dict:
        return "Input must be a dictionary"

    if len(graph) < 2:
        return "There are not enough nodes to form a tree"
  
    for x in graph:
        vert_set.append(set(x))

  

    for key, vertex in graph.items():
        for each in vertex:
            if key > each[0]:
                edges.add((each[1], each[0], key))
        else:
            edges.add((each[1], key, each[0]))
  
    sorted_e = sorted(edges)

    holding_cell = []
    for edge in sorted_e:
        edge1 = edge[1]
        edge2 = edge[2]

        if tree_set == []:
            tree_set.append({edge1, edge2})
            chosen_edges.append(edge)
        else: 
            index1 = -1
            index2 = -1

        for index in range(len(tree_set)):
            if edge1 in tree_set[index]:
                index1 = index

            if edge2 in tree_set[index]:
                index2 = index

            if index1 == -1 and index2 == -1:
                tree_set.append({edge1, edge2})
                chosen_edges.append(edge)
            elif (index1 == index2) and (index1 > 0 and index2 > 0):
                index1 = -1
                index2 = -1
            elif index1 == -1 and index2 > 0:
                holding_cell.append({edge1})
                tree_set[index2] = tree_set[index2].union(tree_set[holding_cell[0]])
                holding_cell.pop(0)
                index2 = -1
                chosen_edges.append(edge)

            elif index2 == -1 and index1 >= 0:
                holding_cell.append({edge2})
                tree_set[index1] = tree_set
                tree_set[index1] = tree_set[index1].union(holding_cell[0])
                holding_cell.pop(0)
                index1 = -1
                chosen_edges.append(edge)
        

            elif (index1 != -1 and index2 != -1) and (index1 != index2):
                tree_set[index1] = tree_set[index1].union(tree_set[index2])
                tree_set.pop(index2)
                index1 = -1
                index2 = -1
                chosen_edges.append(edge)
        

    for chosen in chosen_edges:
        value = chosen[0]
        key = chosen[1]
        connects_to = chosen[2]
        if key in final_output:
            final_output[key].append((value, connects_to))
        else: 
            final_output[key] = [(value, connects_to)]

    return final_output





    





Question 5

class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
    
    def append(self, new_element):
        current = self.head
        if self.head:
          while current.next:
            current = current.next
          current.next = new_element
        else:
          self.head = new_element




def question5(ll, m):

    if not ll.head:
      return None

    if m == 0:
      return None

    counter = 1
    current = ll.head
    while current.next:
        current = current.next
        counter += 1
       
    temp = counter - m
    winner = temp +1
    if counter == winner:
       return current.value
    elif m > counter:
       return None

    new_counter = 1
    new_counter = ll.head
    while new_current.next:
      if new_counter == winner:
          return new_current.value
      else: 
          new_current = new_current.next
          new_counter +=1



node1 = Node('A')
ll = LinkedList(node1)
ll.append(Node('B'))
ll.append(Node('C'))
ll.append(Node('D'))
ll.append(Node('E'))
ll.append(Node('F'))

print(question5(ll, 4))









