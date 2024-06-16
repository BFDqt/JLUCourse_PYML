def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n - 1)

s = input()

# 检查输入是否为空
if not s:
    print("error: No input detected.")

# 检查是否为负数，同时确保除了负号外全是数字
elif (s[0] == '-' and s[1:].isdigit()) or s.isdigit():
    n = int(s)
    if n < 0:
        print("error: Negative numbers are not allowed.")
    else:
        print(factorial(n))

# 检查是否为小数，同时确保只有一个小数点且小数点后有数字
elif ('.' in s and s.count('.') == 1 and s[s.index('.'):].isdigit()) or ('.' in s and s.startswith('-') and s[1:].count('.') == 1 and s[1:s.index('.')].isdigit()):
    print("error: Decimal numbers are not allowed.")

# 检查是否为非数字字符
else:
    print("error: Input contains non-numeric characters.")