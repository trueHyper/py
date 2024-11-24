numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

elemCount=len(numbers)

sum = 0
iter = 0

for i in range(elemCount):
    if type(numbers[i]) != int: i = iter
    else:  sum += numbers[i]
    
average = sum / elemCount

for j in range(elemCount):
    if type(numbers[j])!= int: numbers[j] = average

print(numbers)
