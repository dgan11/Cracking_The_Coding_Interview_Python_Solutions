def urlify(s):
	#return s.strip().replace(" ", "%20") # actual
    return " ".join(s.strip().split()).replace(" ","%20") # more robust and useful

# Time: O(2n) -- two passes one to remove leading and trailing whitespace, another to replace
# Space: O(1) -- modify the string in place


t = " Mr John    Smith		 "
y = "			j "
z = ""
w = " "

#print(t.strip())                # "Mr John    Smith"         s.strip() -- removes leading white space
#print(t.split())                # ['Mr', 'John', 'Smith']    s.split() -- gets non-whitespace charachters in a list
#print(" ".join(t.split()))      # "Mr John Smith"            " ".join(['a', 'b']) -- make whatever at the beginiing between each string in the array
#print(w.replace(" ", "%20"))    # "%20"                      s.replace(old, new) -- replace old with new     


assert(urlify(t) == "Mr%20John%20Smith")

