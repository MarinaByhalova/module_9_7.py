def is_prime(func):
    def wrapper(*args, **kwargs):
        sum_ = func(*args, **kwargs)
        is_prime = True
        if sum_ % sum_ == 0 and sum_ != 0:
            return 'Простое'
        else:
            return 'Составное'

    return wrapper


@is_prime
def sum_three(num1, num2, num3):
    result = num1 + num2 + num3
    print(result)
    return result


result = sum_three(2, 3, 6)
print(result)
