#Printing the sum of the given array
def array_sum(array):
    sum=0
    for i in range (0,len(array)):
        sum+=array[i]
    return sum

print("Sum : ",array_sum([1,2,3]))