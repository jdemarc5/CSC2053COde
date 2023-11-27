'''
Joseph DeMarco

Platform Based Computing
Kathleen Malone

Homework 1

# Cite any sources you used to help with the homework including TAs and classmates

function has123
    used: GeeksforGeeks for 

hascode
    used: javatpoint .com  and found the "re" library for the "wildcard" character
        docs.python.org  to find "re" library documentation and functions
        stackoverflow .com  to learn to use "re.findall()" to return a list of occurences then find the length of the list

centered_avg
    used: programiz .com to read about .remove() functionality
'''




import re  #library with wildcard character for hascode()


def string3(string):
    """
    Given a string, return a new string made of 3 copies of the last 2 chars of the original string.
    The string length will be at least 2.
    """

    #nstr = string[-2:] + string[-2:] + string[-2:]
    nstr = string[-2:] * 3

    return nstr



def has123(nums):
    """
    Given an list of ints, return True if the sequence of numbers
    1, 2, 3 appears in the list somewhere.
    """
   
    for i in range(len(nums)-2):
        if nums[i] == 1 and nums[i+1] == 2 and nums[i+2] == 3:
            return True

    return False  #if true doesn't hit for any conditions


# string 2 count_code
def hascode(string):
    """
    Return the number of times that the string "code" appears anywhere in the given string,
    except we'll accept any letter for the 'd', so "cope" and "cooe" count.
    """

    num_code = len(re.findall("co.e", string))
    return num_code

    

def samecatdog(string):
    """
    Return True if the string "cat" and "dog" appear the same number of times in the given string.
   *** This can be simplfied using a Python string method ***
    """
    cat = string.count("cat")
    dog = string.count("dog")

    if cat == dog:
        return True
    else: 
        return False
    

def centered_avg(nums):
    """
    Return the "centered" average of a list of ints, which we'll say is the mean average of the
    values, except ignoring the largest and smallest values in the list. If there are
    multiple copies of the smallest value, use just one copy, and likewise for the largest value.
    Use floor division to produce the final average. You may assume that the list is length 3 or more.
    """

    #identify min and max
    large = max(nums)
    small = min(nums)

    #remove min and max, handles one occurence or two occurence cases
    nums.remove(large)
    nums.remove(small)

    #if more than 1 remains after removing the minumum 1 min/max value, remove all but one
    if nums.count(large) > 1:
        for i in range(nums.count(large) - 1):
            nums.remove(large)
    if nums.count(small) > 1:
        for i in range(nums.count(small) - 1):
            nums.remove(small)


    #floored mean value calculation
    num_sum = sum(nums)
    num_items = len(nums)

    mean = num_sum//num_items
    return mean



# Test functions
assert string3("Hello") == 'lololo', 'string3(Hello) expected lololo'
print("correct")
assert string3("ab") == 'ababab', 'string3(ab) expected ababab'
print("correct")
assert string3("Hi") == 'HiHiHi', 'string3(Hi) expected HiHiHi'
print("correct")

assert has123([1, 1, 2, 3, 1]) is True, '[1, 1, 2, 3, 1] has 123'
print("correct")
assert has123([1, 1, 2, 4, 1]) is False, '[1, 1, 2, 4, 1] does not have 123'  
print("correct")
assert has123([1, 1, 2, 1, 2, 3]) is True, '[1, 1, 2, 1, 2, 3] has 123'
print("correct")

assert hascode("aaacodebbb") == 1, 'aaacodebbb has code'
print("correct")
assert hascode("aaacodebbb") == 1, 'codexxcode has code'  ##TYPO?
print("correct")
assert hascode("cozexxcope") == 2, 'cozexxcope has code'
print("correct")

assert samecatdog("catdog") is True, 'catdog appear same number of times'
print("correct")
assert samecatdog("catcat") is False, 'catcat does not appear same number of times'
print("correct")
assert samecatdog("1cat1cadodog") is True, '1cat1cadodog appear the same number of times'
print("correct")

assert centered_avg([1, 2, 3, 4, 100]) == 3, 'average [1, 2, 3, 4, 100] is 3'
print("correct")
assert centered_avg([1, 1, 5, 5, 10, 8, 7]) == 5, 'average [1, 1, 5, 5, 10, 8, 7] is 5'
print("correct")
assert centered_avg([-10, -4, -2, -4, -2, 0]) == -3, 'average [-10, -4, -2, -4, -2, 0] is -3'
print("correct")


# Problems found on https://codingbat.com/python
