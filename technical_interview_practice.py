
### QUESTION 1:
### Given 2 strings s and t, determine wether some anagram
### of t is a substring of s.  For example if s = "udacity"
### and t = "ad", then the function returns True.

### METHOD:
### For string 'abc', keep 'a' the same and find all permutations of 'bc'
### Then swap 'a' with 'b' and find all permutations of 'ac'
### Return to the original string, swap 'a' with 'c' and find all
### permutations of 'ba'
### 'abc', 'acb', 'bac', 'bca', 'cba', 'cab'

### This method is recursive because we are iteratively returning to 
### earlier versions of the string 'abc', swapping characters, and 
### having permutations() call itself until the base
### base case is reached and the string is added to the list.
### This is done until the outermost call of permutations() has 
### gone through the whole string.

### NEED LIST OF PERMUTATIONS FOR "t"
t_perm = []

### GET PERMUTATIONS
def permutations(string, step = 0):
	# This is the base case.
    # if we've gotten to the end, add the permutation
    if step == len(string):
    	new_string = "".join(string)
    	t_perm.append(new_string)
    # everything to the right of step has not been swapped yet
    for i in range(step, len(string)):
        # copy the string as a list of characters
        chars = [character for character in string]

        # Swap the current index with the step
        # A swap only occurs if i is greater than step
        # The new string is only printed if it reaches the base case
        chars[step], chars[i] = chars[i], chars[step]

        # recurse on the portion of the string that has not been swapped yet
        permutations(chars, step + 1)


### CHECK IF SUBSTRING
def question1(s, t):
	check = 0
	permutations(t)
	#print t_perm

	# If any of the "t" permutations 
	# are in "s", break out of loop.
	#print t_perm
	for string in t_perm:
		if string in s:
			check = True
			break
	
	if check == True:
		return True
	else:
		return False

		


### TEST question1()
s = "udacity"
t = "cda"
#print question1(s, t)



### QUESTION 2:
### Given a string 'a', find the longest palindromic substring
### contained in 'a' and return it.


### METHOD:
### We can break this problem into 3 main tasks.  We need to 
### write a helper function reverse() to reverse a list.
### We need a helper function sub_string() to find all possible
### substrings in a string.  Our main function will loop over
### all substrings to find all palindromic substrings and 
### return the longest one.



### Takes in a string with left and right place markers
### 'l' and 'r'.  Returns the reversed string.
def reverse(s, l, r):

	# Find the middle char in string
	if float(len(s) % 2) != 0:
		middle = float(len(s))/2 - 0.5
		middle = int(middle)
	else:
		middle = (int(len(s))/2) - 1

	# Copy string as a list
	s = [char for char in s]

	# Swap the l and r elements
	for i in range(l, middle + 2):	
		if l == middle + 1:
			return ''.join(s)

		s[l], s[r] = s[r], s[l]
		l += 1
		r -= 1





### Find all substrings, duplicates allowed
def sub_string(string, right):
	if right == 1:
		substrings.append("".join(string[0]))
		return substrings

	for i in range(0, right):
		string = [char for char in string]
		sub = string[i:right]
		substrings.append("".join(sub))
		sub_string(string, right-1)




### Find all palindromic substrings
def question2(a, r):
	palindromes = []
	sub_string(a, r)
	for sub in substrings:
		if sub == reverse(sub, 0, len(sub)-1):
			palindromes.append(sub)

	### Find the longest palindromic substring
	return max(palindromes, key=len)



### TEST question2()
a = 'aabacd'
r = len(a)
substrings = []

#print question2(a, r)



### QUESTION 3:
### Given an undirected graph G, find the minimum spanning tree 
### within G.  Function should take in and return an adjacency
### list.

### METHOD:
### Apply Kruskal's algorithm.  Initialize list for minimum spanning tree edges.  
### For each vertex, make a disjoint set(v).  Sort all edges by increasing weight.  
### For each edge (v_i, v_j), use the smallest edge first.  
### If the set of v_i is not in set of v_j, append the edge (v_i, v_j) to list
### and merge set(v_i) and set(v_j) into one set.


# Adjacency list of our graph
#adjacency = {'A':[('B',3), ('C',5)], 'B':[('D',4)], 'C':[('D',1)], 'D':[('D',0)]}
adjacency = {'A':[('B',3), ('E',5), ('C',2)], 'B':[('E',1), ('C',6), ('D',4)]}

# List of minimum spanning tree edges
mst_edges = []

# Adjacency list of minimum spanning tree
mst = {}


# Sort all edges by increasing weight.
# Make edge weight dict {weight:(v_i, v_j)}
edges = {}
for key in adjacency.keys():
	for element in adjacency[key]:
		v1 = key
		v2 = element[0]
		edges[element[1]] = (v1, v2)



# Store sets for each Vertex in dictionary
vertex = {}
for key in adjacency.keys():
	vertex[key] = set(key)



# For each edge value, if edge not in vertex dictionary key, add it
for e in edges:
	v1 = edges[e][0]
	v2 = edges[e][1]
	if v1 not in vertex.keys():
		vertex[v1] = set(v1)
	if v2 not in vertex.keys():
		vertex[v2] = set(v2)



# Apply Kruskal's algorithm.
for i, e in enumerate(edges.keys()):


	# Define two vertices
	v1 = edges[e][0]
	v2 = edges[e][1]
	#print v1, v2

	# If set of vertex 1 is not in set of vertex 2
	if vertex[v1] != vertex[v2]:

		# Set vertex 1 equal to set of vertex 1 and vertex 2
		# and vertex 2 equal to set of vertex 1 and vertex 2
		#vertex[v1] = vertex[v1].union(vertex[v2])
		#vertex[v2] = vertex[v1].union(vertex[v2])
		merge = vertex[v1].union(vertex[v2])

		# For each vertex in merged set
		for m in merge:
			vertex[m] = merge

		# Add edge to minimum spanning tree list
		mst_edges.append((v1, v2))


		# Add edge and weight to minimum spanning tree adjacency list
		# If v1 is not a key in the mst dictionary, add key and value
		# If v1 is a key, append the value to the current list
		if v1 not in mst.keys():
			mst[v1] = [(v2, e)]
		else:
			mst[v1].append((v2, e))



print mst

