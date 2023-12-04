# function template
def first_function():
    pass
print(first_function())

# Challenge 1
def sum_to(num):
    sum = 0
    n = 0
    while n <= num:
        sum += n
        n += 1
    return sum
print(sum_to(10))

# Challenge 2
def largest(nums):
    max = nums[0]
    for n in nums:
        if n > max:
            max = n
    return max
print(largest([10, 4, 2, -231, 91, 54]))

# Challenge 3
def occurrences(string, substring):
    length = len(string)
    new_string = string.replace(substring, "")
    new_len = len(new_string)
    return (length - new_len)/len(substring)
print(occurrences("fleep floop", "ee"))

# Challenge 4
def product(*args):
    result = 0
    for arg in args:
        if arg == args[0]:
            result = arg
        else: result *= arg
    return result
print(product(2,5,5))

# Bonus Challenge
def steps_to_zero(num):
    steps = 0
    while num > 0:
        if num % 2 == 0:
            num /= 2
            steps += 1
        else:
            num -= 1
            steps += 1
    return steps
print(steps_to_zero(14))