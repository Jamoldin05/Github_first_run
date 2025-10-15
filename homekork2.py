




# class FibonacciIterator:
#     def __init__(self, limit):
#         self.limit = limit
#         self.a = 0
#         self.b = 1
#         self.count = 0

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.count >= self.limit:
#             raise StopIteration
#         if self.count == 0:
#             self.count += 1
#             return self.a
#         elif self.count == 1:
#             self.count += 1
#             return self.b
#         else:
#             self.a, self.b = self.b, self.a + self.b
#             self.count += 1
#             return self.b



# fib_iter = FibonacciIterator(10)
# for num in fib_iter:
#     print(num, end=" ")





def fibonacci_generator(limit):
    a, b = 0, 1
    for i in range(limit):
        if i == 0:
            yield a
        elif i == 1:
            yield b
        else:
            a, b = b, a + b
            yield b


for num in fibonacci_generator(10):
    print(num, end=" ")
