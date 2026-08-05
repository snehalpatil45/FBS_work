# Requirements - duplicate elements are not allowed
            #  - sorted (asec)
# Time complexity - o(log n)

def binarySearch(li,search_ele):
    beg = 0
    end = len(li) - 1
    while(beg <= end):
        mid = (beg + end) // 2
        if(search_ele == li[mid]):
            return mid
        elif(search_ele > li[mid]):
            beg = mid + 1
        elif(search_ele < li[mid]):
            end = mid - 1
    else:
        return -1
        
li = [10,20,30,40,50,60,70]
search_ele = int(input('Enter element to search:'))
res = binarySearch(li,search_ele)
if(res != -1):
    print(f'{search_ele} is present at index{res}.')
else:
    print(f'{search_ele} is not present .')

#Time complexity
#1. best case : o(1)
#2. worst case: o(log n)
#3. average case: o(log n)