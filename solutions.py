"""Given two strings s and t, determine whether some anagram of t is a substring of s. For example: if s = "udacity" and t = "ad", then the function returns True. Your function definition should look like: question1(s, t) and return a boolean True or False.
"""





def question1(s, t):

	#Check if the inputs are valid and are of type string. Return False if not.
    if not s or type(s) != str:
    	return False

    if not t or type(t) != str:
    	return False

    #Initialize empty sets
    s_set = set()
    t_set = set()

    #Initialize empty dictionaries
    letter_tally_s = {}
    letter_tally_t = {}

    #Remove all spaces from each string.  Each is O(n)
    s_string = s.replace(" ", "").lower()
    t_string = t.replace(" ", "").lower()

    #Check if the length of s is not less than the length of t
    if len(s_string) < len(t_string):
    	return False

    #Convert the strings into a list of the individual letters of the string. Each is O(n)
    s_list = list(s_string)
    t_list = list(t_string)

    #Put the contents of the list into the corresponding sets. At the same time, tally all the letters
    for x in range(len(s_string)):
        s_set.add(s_string[x])
        count_s = s.count(s_string[x])
        letter_tally_s[s_string[x]] = count_s

    for y in range(len(t_string)):
        t_set.add(t_string[y])
        count_t = t.count(t_string[y])
        letter_tally_t[t_string[y]] = count_t

    #Check if all characters in t are present in s, otherwise return False. O(n).Check if the letter count is the same for all letters in t as in s. O(n)
    for letter in t_set:
    	if letter not in s_set:
    		return False
      if letter_tally_t[letter_t] > letter_tally_s[letter_t]:
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




def question2(s):
  
  str1 = s
  word = ""
  longest = ""
  start = 1
  before = start - 1
  after = start + 1

  #Check if type is string and is not empty
  if not str1 or type(str1) != str:
    return "Input is either None or not type: str."

  #Check if string is longer than one character
  if len(str1) < 2:
    return "Length of string is less than 2."
  #Check if the input is already a palindrome in itself, making itself the longest palindrome.
  if str1 == str1[::-1]:
    return str1
  #Check if the last 2 letters are the same.  If they are, store them as the longest palindrome for now.
  if str1[len(str1)-2] == str1[len(str1)-1]:
    longest = str1[len(str1)-2:len(str1)]

  #Check the second letter of the string.  Check the letter before it and after it and iterate through the string this way
  for x in range(1, len(str1)-2):
    #If the string starts with repeating letters, use the recursive function to see how long it repeats. then increment to check for other repeating letters in the string.
    if str1[before] == str1[start]:
      consec = consecutive(str1, before, start)
      if len(consec) > len(longest):
        longest = consec
      start +=1
      before += 1
      after += 1

    #Keep incrementing if no palindrome is found.
    elif str1[before] != str1[after]:
      start +=1
      before += 1
      after += 1
    #If a palindrome of 3 letters is found, use the palindrome recursive function to keep going further out. Store it in variable longest.
    elif str1[before] == str1[after]:
      word = palindrome(str1, before, after)
      start += 1
      before += 1
      after += 1
      if len(word) > len(longest):
        longest = word

  if longest == "":
    return "There are no palindromes found."
  else:
    return longest
      

#Helper function that compares letters outward from a point in the string
def palindrome(stng, bef, aft): 
  
  if stng[bef] != stng[aft]:
    return stng[bef+1:aft]
  elif bef == 0 or aft == len(stng)-1:
    return stng[bef:aft+1]
  else:
    return palindrome(stng, bef-1, aft+1)

#Helper function that looks for more repeating letters to the right of two repeating letters
def consecutive(stng, b, st):
  if st == len(stng)-1:
    return stng[b:st+1]
  elif stng[b] != stng[st+1]:
    return stng[b:st+1]
  else:
    return consecutive(stng, b, st+1)
 
#Teest Cases:

#Should return "hhhnursesrunhhh"
string1 = "dcknseshhhhnursesrunhhhrun..xxxxxx"
print(question2(string1))

#should return "nursesrun"
string2 = "aaajslsownursesruncox"
print(question2(string2))

#Should return "There are no palindromes found."
string3 = "abcdefghijklmnop"
print(question2(string3))

#Should return "Input is either None or not type: str.""
string4 = ""
print(question2(string4))

#Input is either None or not type: str.
string5 = 12345
print(question2(string5))

#Length of string is less than 2.
string6 = "g"
print(question2(string6))










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


Question 4

m = [[0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0],
     [0, 1, 0, 1, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0],
     [0, 0, 1, 0, 0, 0, 1],
     [0, 0, 0, 0, 0, 0, 0]]

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        self.insert_helper(self.root, new_val)

    def insert_helper(self, current, new_val):
        if current.value < new_val:
            if current.right:
                self.insert_helper(current.right, new_val)
            else:
                current.right = Node(new_val)
        else:
            if current.left:
                self.insert_helper(current.left, new_val)
            else:
                current.left = Node(new_val)

def unzip(matrix, node):
    temp_node = None
    for y in range(len(matrix[node.value])):
      
      if matrix[node.value][y] == 1 and y < node.value:
        temp_node = Node(y)
        node.left = temp_node
        unzip(matrix, node.left)
        
      if matrix[node.value][y] == 1 and y > node.value:
        temp_node = Node(y)
        node.right = temp_node
        unzip(matrix, node.right)
        
def find_ancestor(vertex, smaller, larger):
  if smaller <= vertex.value and larger >= vertex.value:
    return vertex.value
  elif smaller < vertex.value and larger < vertex.value:
    print('smaller is ', smaller, 'vertex ', vertex.value, 'larger ', larger)
    return find_ancestor(vertex.left, smaller, larger)
  elif smaller > vertex.value and larger > vertex.value:
    print('smaller is ', smaller, 'vertex ', vertex.value, 'larger ', larger)
    return find_ancestor(vertex.right, smaller, larger)
        
      


def question4(T, r, n1, n2):

  if type(T) != list:
    return "TypeError: Matrix is not of type List!"
  
  if type(r) != int:
    return "TypeError: r is not an integer!"
  if type(n1) != int:
    return "TypeError: n1 is not an integer!"
  if type(n2) != int:
    return "TypeError: n2 is not an integer!"

  n = Node(r)

  unzip(T, n)

  
  
  current = n
  small = min(n1, n2)
  big = max(n1, n2)
  
  winner = find_ancestor(current, small, big)

  return winner

  


      


  
#should return 2
print(question4(m, 5, 1, 3))


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









