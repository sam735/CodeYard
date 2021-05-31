# ATBASH Palindrome
# W (4-Z) 
#     I (9-A) 
#         Z (0-Z) 
#         A (0-A) 
#     R (9-Z) 
# D (4-A)
# W I Z A R D


word = input("Enter the string to check:").lower()
#word = "wizard"
l1=[]
l2=[]
print ("Word to check:"+word)

rev_word = word[::-1]
print("Word in reverse order:"+rev_word)


for char in word:
    #print ("print ASCII values of {} is {}".format(char,ord(char)))
    
    if (word.index(char) % 2 ==0):
        values = abs(ord('z')-ord(char))
        l1.append(values)

    if (word.index(char) % 2 !=0):
        values = abs(ord('a')-ord(char))
        l1.append(values)
#checking the content in list
#print (l1)
#print (l1[::-1])

for char in rev_word:
    #print ("print ASCII values of {} is {}".format(char,ord(char)))
  
    if (rev_word.index(char) % 2 ==0):
        values = abs(ord('a')-ord(char))
        l2.append(values)

    if (rev_word.index(char) % 2 !=0):
        values = abs(ord('z')-ord(char))
        l2.append(values)
#checking the content in list
#print (l2)



if l1 == l2:
    print("Is ATBASH Palindrome {}:true".format(word))
else:
    print ("Is ATBASH Palindrome {}:false".format(word))
