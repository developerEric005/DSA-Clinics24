def reverse_integer(n):
    sign = -1 if n < 0 else 1
    n = abs(n)
    reversed_n = int(str(n)[::-1])
    return sign * reversed_n

# Example usage
num = int(input("Enter an integer: "))
print("Reversed integer:", reverse_integer(num))
