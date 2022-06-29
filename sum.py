"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]

Constraints:
2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
"""


# MY SOLUTION

# the cool thing that i see in my a solution is that
# i loop through the list in a way that i add moving forward. not again adding something that if already did. 
# (i know this doesn't make sense to you. but to me it does)


def my2sum(thelist, thetarget):
    thecounter = 1
    for num in thelist:
        start = thecounter
        while start < len(thelist):
            if num + thelist[start] == thetarget:
                return [thelist.index(num), thelist.index(thelist[start])]
            start += 1
        thecounter += 1









# THINKING OUT LOUD
# looping through a list



# finally figured it out after a week.
# thelist =  [2,7,11,15]
# counter = 1
# for num in thelist:
#     print('guy of the show %d',num)
#     start = counter
#     while start < len(thelist):


#         print(num + thelist[start] == 9)
#         print([num, thelist[start]])     
#         start += 1            
#     counter +=1




# thelist =  [2,7,11,15]
# counter = 1

# # print(thelist.index(3))
# for num in thelist:
#     # for i in range(len(thelist)):
#         # if start < len(thelist) and num + thelist[start] == 6 :
#     print('guy of the show %d',num)
#     start = counter
#     while start < len(thelist):


#         print(num + thelist[start] == 9)
#         print([num, thelist[start]])     
#         start += 1            
#     counter +=1

        # print(start)
        # if thelist[num] + thelist[start] == 6 and start < len(thelist):
        #     print(thelist[num], thelist[start])
        # start =start +1    

        # if i != num:
        #     if i + thelist[num] == 6:
        #       print(i, thelist[num])
   
#         # if thelist.index(i) != thelist.index(thelist[num]):
#             if i + thelist[num] == 6:
#                 print(i, thelist[num])

