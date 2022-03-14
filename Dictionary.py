# Create the dictionary
my_dic = {}
 
# Now populate it
for i in range(97, 97 + 26):
    # Map character to ascii value
    my_dic[chr(i)] = i
 
# Print the populated dictionary
print(my_dic)
