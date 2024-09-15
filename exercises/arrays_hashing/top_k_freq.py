'''
Top K Elements in List

Difficulty: MEDIUM

Given an integer array nums and an integer k, return the k most frequent elements within the array.

The test cases are generated such that the answer is always unique.

You may return the output in any order.

Example 1:

    Input: nums = [1,2,2,3,3,3], k = 2

    Output: [2,3]

Example 2:

    Input: nums = [7,7], k = 1

    Output: [7]

Constraints:

    * 1 <= nums.length <= 10^4.
    * -1000 <= nums[i] <= 1000
    * 1 <= k <= number of distinct elements in nums.

'''

def topKFrequent(nums, k):
    my_dict = {}
    res = []
    
    for n in nums:
        if n not in my_dict:
            my_dict[n] = 1
        else:
            my_dict[n] += 1

    bucket = [[] for i in range(0,len(nums) + 1)]

    for key, value in my_dict.items():
        bucket[value].append(key)

    i = len(bucket) - 1
    while i > 0:

        if len(bucket[i]) != 0:
            j = 0
            while j < len(bucket[i]):
                res.append(bucket[i][j])
                j += 1
                if len(res) == k:
                    return res

        i -= 1

def topKFrequent_old(nums, k):
    my_dict = {}

    for n in nums:
        if n not in my_dict:
            my_dict[n] = 1
        else:
            my_dict[n] += 1

    my_sorted_list_tuples = sorted(my_dict.items(), key = lambda x: x[1], reverse = True)

    my_dict = dict(my_sorted_list_tuples)

    res = []
    i = 0
    while i < k:
        res.append(list(my_dict.keys())[i])
        i += 1

    return res


print(topKFrequent([1,2,2,3,3,3], 2))

# print(topKFrequent([7,7], 1))

# print(topKFrequent())
