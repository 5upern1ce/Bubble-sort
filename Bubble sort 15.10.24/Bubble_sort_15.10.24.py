import random, time
def randomlist():
    nums = []
    for i in range(0,50000):
        n = random.randint(1,99)
        nums.append(n)
    return (nums)

def lengthchecker(listinp):
    return len(listinp)

def bubblesort():
    start = time.time()
    lst1 = randomlist()
    counter = lengthchecker(lst1)
    n = counter - 1
    while counter > 1:
        for sort in range(0, n):
            if lst1 [sort] > lst1 [sort+1]:
                switch = lst1 [sort]
                lst1 [sort] = lst1 [sort + 1]
                lst1 [sort+1] = switch
        n-=1
        counter -=1
    end = time.time()
    length = end - start
    print(f"The sorted list is {lst1}, it sorted it in {length} seconds!")
bubblesort()
