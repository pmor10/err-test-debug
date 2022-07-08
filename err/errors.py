# Error Handling
while True:
    try:
        age = int(input('what is your age? '))
        print(age)
    except ValueError:
        print('Please enter a number!!!')
    except ZeroDivisionError:
        print('Please enter age higher than 0')
    else:
        print('Thank you!')
        break
    finally: # runs regardless
        print('OK, I am finally done!')


# def sum(num1, num2):
#     try:
#         return num1 + num2
#     except TypeError as err:
#         print(f'Please enter numbers {err}')


# print(sum('1', 2))


# def sum2(n1, n2):
#     try:
#         return n1/n2
#     except(TypeError, ZeroDivisionError) as err:
#         print(f'Oops {err}')


# print(sum(1, 0))
