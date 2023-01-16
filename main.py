class Person:
    persons_list = []

    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email
        self.persons_list.append(
            [self.name, self.age, self.email]
        )

    def grow_up(self):
        self.age = 1
        print(self.age)

    def __str__(self):
        return f"Person object{self.name}"

    @staticmethod
    def get_info_about_persons():
        for elem in Person.persons_list:
            print(elem)


first_person = Person("Richard", 33, "fdgdfgdf@gmail.com")
second_person = Person("Carol", 22, "2323@gmail.com")
first_person.get_info_about_persons()
