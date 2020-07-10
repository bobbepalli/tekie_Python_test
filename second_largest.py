#method-1

list = [int(x) for x in input().split()] #taking list as dynamic input

list.sort() #sorting the list in ascending order

second_largest = list[-2] # -ve sign represents backward direction

print(second_largest)

#method - 2

list = [int(x) for x in input().split()] #taking list as dynamic input

list.remove(max(list)) # to remove first largest value in a list

second_largest = max(list)# after removing first lagest value, now it is the largest value

print(second_largest)