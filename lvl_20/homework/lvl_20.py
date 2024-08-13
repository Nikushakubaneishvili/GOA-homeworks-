def sum_even_numbers(nums):
    total = 0
    for num in nums:
        if num % 2 == 0:
            total += num
    return total

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(sum_even_numbers(numbers)) 



def reverse_string(s):
    reversed_str = ''
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str



def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)



def common_elements(list1, list2):
    common_list = []
    for element in list1:
        if element in list2 and element not in common_list:
            common_list.append(element)
    return common_list



def count_vowels(s):
    vowels = 'nika'
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count