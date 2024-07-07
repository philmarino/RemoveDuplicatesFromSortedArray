
def removeDuplicates(list) :
    unique = []
    remove = []
    for item in list:
        if item in unique:
            remove.append(item)
        else:
            unique.append(item)
    #calls remove for each item n-1 times for each duplicate item
    for item in remove:
        list.remove(item)
    return len(list)

#Example 1:
#Input: 
nums = [1,1,2]
k = removeDuplicates(nums)
print(k)
print(nums)

#Output: 2, nums = [1,2,_]
#Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
#It does not matter what you leave beyond the returned k (hence they are underscores).

#Example 2:
#Input: 
nums = [0,0,1,1,1,2,2,3,3,4]
k = removeDuplicates(nums)
print(k)
print(nums)

#Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
#Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
#It does not matter what you leave beyond the returned k (hence they are underscores).
 