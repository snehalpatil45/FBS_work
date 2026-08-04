# Time complexity - o(n)

def linearsearch(li,search_ele):
    for i in range(0,len(li)):
        if(search_ele == li[i]):
            return i
    else:
        return -1
    
li = [45,32,89,56,21,90,42,77]
ele = int(input('Enter element to search:'))
res = linearsearch(li,ele)
if(res != -1):
    print(f'{ele} is present at index {res}.')
else:
    print(f'{ele} is not present.')