# "Sum Of Array Singles
# --------------------
# Given an array of numbers in which two numbers occur once and the rest occur only twice. Your task will be to return the sum of the numbers that occur only once.
# Example 1:
# Input: repeats([4, 5, 7, 5, 4, 8])
# Output: 15
# Explanation: only the numbers 7 and 8 occur once, and their sum is 15. Every other number occurs twice.

# Example 2:
# Input: repeats([13, 8, 7, 4, 4, 8])
# Output: 20
# Explanation: only the numbers 13 and 7 occur once, and their sum is 20. Every other number occurs twice."

def solution(given_list):
    # write your code here
    seen_once = set()
    seen_twice = set()
    for num in given_list:
        if num in seen_once:
            seen_twice.add(num)
        else:
            seen_once.add(num)
    only_once = seen_once - seen_twice
    return sum(only_once)

print(solution([4, 5, 7, 5, 4, 8]))


def solution(given_list):
    # write your code here
    numbers = set()
    for num in given_list:
        if num in numbers:
            numbers.remove(num)
        else:
            numbers.add(num)
    return sum(numbers)

print(solution([4, 5, 7, 5, 4, 8]))



def solution(given_list): # O(n**2)
    # write your code here
    numberss = [] # O(1)
    for num in given_list: # O(n)
        num2 = given_list.count(num) # O(n)
        if num2 != 2: # O(1)
            numberss.append(num) # O(1)
    x = 0 # O(1)
    for num1 in numberss: # O(1)
        x +=  num1 # O(1)
    return x # O(1)
