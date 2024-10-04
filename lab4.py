import random
import time

def get_next(x):
    return random_even_number_in_range(1, 100)

def random_even_number_in_range(start, end):
    if start % 2 != 0:
        start += 1
    
    return random.randrange(start, end + 1, 2)

def is_even(x):
    rand = random_even_number_in_range(1, 100)
    return True if x % 2 == 0 else False

##
# Ask user to create a list from the terminal
def task1():
    input("Enter 10 digits into a list when prompted. (Press any key)")
    time_it = time.time()
    user_list = []
    for i in range(10):
        user_list.append(int(input("Enter a digit: ")))
    
    elapsed = time.time() - time_it
    print(f"Time taken to fill this list: {elapsed:1.0f}")


##
# Fill in a list of a given size and record the time it takes to do so
def task2(size):
    
    print(f"Filling a list of size: {size}")
    L1 = []
    # Create a list with a for loop and append()
    start = time.time_ns()
    for _ in range(size):
        L1.append(random.randint(1, 100))

    end = time.time_ns()
    elapsed = end - start
    print(f"Time to fill the first list: {elapsed:1.0f}")

    # use list comprehension to create the list
    start3 = time.time_ns()
    L3 = [x for x in random.randint(1, 100)]
    end3 = time.time_ns()

    elapsed3 = end3 - start3
    print(f"Time to fill the second list with comprehension: {elapsed:1.0f}")


def task3():
    # Using a for loop like in task 2 pt1
    primes_L1 = []
    start = time.time_ns()

    for _ in range(500):
        primes_L1.append(random_even_number_in_range(1, 100))

    end = time.time_ns()
    elapsed = end - start
    print(f"Filled the list of size {len(primes_L1)} using Style 1 in: {elapsed:1.0f} nanoseconds")

    # Using comprehension from tas 2 to fill a list
    start2 = time.time_ns()
    primes_L2 = [x for x in primes_L1]
    end2 = time.time_ns()
    elapsed2 = end2 - start2
    print(f"Filled the list of size {len(primes_L2)} using Style 2 in: {elapsed2:1.0f} nanoseconds")

    # Using a map to fill a list
    start3 = time.time_ns()
    holder = map(get_next, range(500))
    primes_L3 = list(holder)
    end3 = time.time_ns()
    elapsed3 = end3 - start3
    print(f"Filled the list of size {len(primes_L3)} using Style 3 in: {elapsed3:1.0f} nanoseconds")

    # using a VERY ineffcient filter to fill a list
    start4 = time.time_ns()
    primes_L4 = []
    for i in range(500):
        # fill it with the even numbers from this range 
        filter_holder = filter(is_even, range(100))
        primes_L4.append(list(filter_holder))
    end4 = time.time_ns()
    elapsed4 = end4 - start4
    print(f"Filled the list of size {len(primes_L4)} using Style 4 in: {elapsed4:1.0f} nanoseconds")

    # using an improved filter to a fill a list
    start5 = time.time_ns()
    filter_holder_ex = filter_holder(is_even, random.choices(range(1, 101), k=500))
    primes_L5 = list(filter_holder_ex)
    end5 = time.time_ns()
    elapsed5 = end5 - start5
    print(f"Filled the list of size {len(primes_L5)} using Style 4 in: {elapsed5:1.0f} nanoseconds")








if __name__ == "__main__":
    #task1()
    #input("Press any key to continue...")
    #task2(int(input("Input the size of the list: ")))
    task3()
    