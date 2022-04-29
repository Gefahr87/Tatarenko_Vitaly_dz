'''
Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield, например:
odd_to_15 = odd_nums(15)
next(odd_to_15) 1
next(odd_to_15)
3
next(odd_to_15) 15
next(odd_to_15) ...StopIteration...
'''

def gen_of_interstage(num):
    for i in range(1, num + 1, 2):
        yield i


if __name__ == "__main__":
    num = 15
    result = gen_of_interstage(num)
    for _ in range(num):
        print(next(result))

