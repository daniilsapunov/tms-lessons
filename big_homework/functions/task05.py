numbers = [int(i) for i in input().split()]

def fileter_negative_numbers(lst:list) -> []:
    return [num for num in numbers if num >= 0]

print(fileter_negative_numbers(numbers))

