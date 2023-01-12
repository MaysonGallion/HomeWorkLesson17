# EX_1
class Kalkulator:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def div(self):
        try:
            return self.a // self.b
        except ZeroDivisionError:
            print("Делить на ноль нельзя")

    def minus(self):
        return self.a - self.b

    def plus(self):
        return self.a + self.b

    def mult(self):
        return self.a * self.b

    def k(self):
        return self.a ** self.b


while True:
    user_input = input("Введите операцию которую хотите выполнить(+,-,/,*,**) \n Введите /n для выхода: ")
    example = Kalkulator(int(input("Введите первое число: ")), int(input("Введите второе число: ")))
    if user_input == "+":
        print(example.plus())
    elif user_input == "-":
        print(example.minus())
    elif user_input == "*":
        print(example.mult())
    elif user_input == "/":
        print(example.div())
    elif user_input == "n":
        break
    elif user_input == "**":
        print(example.k())


# EX_2
class MyClass:
    def __init__(self):
        pass

    def first_method(self, input):
        if isinstance(input, str):
            vowels = sum(1 for c in input if c in 'aeiouAEIOU')
            consonants = len(input) - vowels
            if vowels * consonants <= len(input):
                return (c for c in input if c in 'aeiouAEIOU')
            else:
                return (c for c in input if c not in 'aeiouAEIOU')
        elif isinstance(input, int):
            return sum(int(d) for d in str(input) if int(d) % 2 == 0) * len(str(input))

    def second_method(self, input):
        if isinstance(input, (str, int)):
            return len(str(input))



# Usage example
my_class = MyClass()
print(my_class.first_method(input("Введите строку :")))  # "eoo"
print(my_class.first_method(int(input("Введите число: "))))  # 42
print(my_class.second_method(input("Введите строку чтобы проверить длинну: ")))  # 11
print(my_class.second_method(int(input("Введите число чтобы проверить длинну: "))))  # 6
