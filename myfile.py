#Printing the sum of the given array
def error1():
    array = [1, 6, 3, 7, 9]
    sum=0
    for i in range (0,5):
        sum+=array[i]
    return sum

print("Sum : ",error1())