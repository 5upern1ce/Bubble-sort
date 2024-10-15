import random 
def randomlist():
    nums = []
    for i in range(0,10):
        n = random.randint(1,30)
        nums.append(n)
    return (nums)

def lengthchecker(listinp):
    return len(listinp)

def bubblesort():
    lst1 = randomlist()
    print (f"The unsorted list is {lst1}")
    counter = lengthchecker(lst1)
    while counter > 1:
        for sort in range(9):
            if lst1 [sort] > lst1 [sort+1]:
                switch = lst1 [sort]
                lst1 [sort] = lst1 [sort + 1]
                lst1 [sort+1] = switch
        counter -=1
    print(f"The sorted list is {lst1}")
bubblesort()
