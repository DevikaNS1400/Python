str1='First day of Python coding'
print('====Length of the string====')
print(len(str1))
print('====Finding the index====')
print(str1.find('d'))
print(str1.find('D'))
print('====Converting to upper case and lower case====')
print(str1[0:5].upper()+str1[5:])
print(str1.lower())
print(str1.title())
print('====Replacing the string====')
print(str1.replace('First','Second'))
print('====Presence of a character====')
print('Python' in str1)
print('====Reversing the string====')
print(str1[::-1])

'''
Output

====Length of the string====
26
====Finding the index====
6
-1
====Converting to upper case and lower case====
FIRST day of Python coding
first day of python coding
First Day Of Python Coding
====Replacing the string====
Second day of Python coding
====Presence of a character====
True
====Reversing the string====
gnidoc nohtyP fo yad tsriF
'''
