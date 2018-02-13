def power_of_number(number, pow_):
    if pow_ == 0:
        return 1
    if pow_ == 1:
        return number

    res = power_of_number(number, pow_ // 2)

    if pow_ % 2 == 0:
        result = res * res

    else:
        result = number * res * res

    return result

a = power_of_number(2.1, 3)
print(a)