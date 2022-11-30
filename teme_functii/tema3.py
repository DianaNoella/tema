def f4():
    x = input()
    try:
        x = int(x)
    except ValueError:

        if x == 'quit' or 'exit':
            return 0

    def pal():
        if str(x) == str(x[::-1]):
            return "is_palindrome", True
        else:
            return "is_palindrome", False

    def prime():
        if x > 1:
            for i in range(2, x):
                if x % i == 0:
                    return "is_prime", False
            return "is_prime", True

    def div():
        x = int(x)
        my_list = []
        for i in range(1, n + 1):
            if x % i == 0:
                my_list.append(i)
            print(my_list)
        return 'max_div:', my_list[-2]

    def digits():
        count = 0
        while x != 0:
            x //= 10
            count += 1
        return count


print(f4())



