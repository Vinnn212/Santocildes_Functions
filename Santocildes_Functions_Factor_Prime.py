print("")
print("What do you want to do?")
print("")
print("[1] is to find the smallest factor")
print("[2] is to find a prime number of range")
print("")

while True:
    try:
        find = float(input("Choose either 1 or 2: "))
        if find < 1:
            print("Please choose from 1 or 2 only.")
            print("")
            continue
        if find > 2:
            print("Please choose from 1 or 2 only.")
            print("")
            continue
    except ValueError:
        print("You must enter a number from 1 or 2 only.")
        continue
    break

if find == 1:
    print("You have chosen to find the smallest factor of a number.")
    print("")
    def smallest_factor(n):
        if n <= 1:
            return None
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return i
        return None


    n = int(input("Enter a number: "))
    smallest_factor = smallest_factor(n)

    if smallest_factor is None:
        print(n, "is prime")

    else:
        print(f"The smallest factor for", n, "is", smallest_factor)

elif find == 2:
    print("You have chosen to find a prime number of a range.")
    print("")
    print("Note to remember:")
    print("[1] Starting digit should not be a negative number.")
    print("[2] Ending digit should not be lower than Starting digit.")
    print("[3] If starting digit is equal to zero(0), the program will end.")
    print("")


    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True


    while True:
        try:
            print("")
            print('')
            lower = int(input("Enter a starting digit: "))
            if lower < 0:
                print("You must enter a non-negative integer!")
                print()
                continue
            if lower == 0:
                print("Invalid. Please run the program again.")
                break
        except ValueError:
            print("Invalid! Enter a integer number!")
            continue

        while True:
            try:
                upper = int(input("Enter the ending digit: "))
                if upper <= lower:
                    print("You must enter an integer greater than", lower)
                    continue
            except ValueError:
                print("You must enter a Integer number!")
                continue
            break

        print("Prime numbers between", lower, "and", upper, "are:", end=' ')

        for num in range(lower, upper + 1):
            if is_prime(num):
                print(num, end=' ')
