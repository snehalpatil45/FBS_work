s1 = input('Enter string 1:')
s2 = input('Enter string 2:')
count = {}
for char in s1:
    count[char] = count.get(char,0)+1
for char in s2:
    count[char] = count.get(char,0)-1
for value in count.values():
    if(value != 0):
        print('Not Anagram')
else:
    print('Anagram')