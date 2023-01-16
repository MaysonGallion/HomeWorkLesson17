class Tomato:
    states = {1: "green", 2: "yellow", 3: "red"}

    def __init__(self, index):
        self.index = index
        self._state = 1

    def grow(self):
        self._state += 1

    def is_ripe(self):
        if self._state == 3:
            return True
        else:
            return False


class TomatoBush:
    def __init__(self, num_tomato):
        self.tomatoes = []
        for i in range(num_tomato):
            self.tomatoes.append(Tomato(i))

    def grow_all(self):
        for i in self.tomatoes:
            i.grow()

    def all_are_ripe(self):
        false_count = 0
        for i in self.tomatoes:
            if not i.is_ripe():
                false_count += 1
        if false_count == 0:
            return True
        else:
            return False

    def give_away_all(self):
        self.tomatoes.clear()

class Gardener:
    def __init__(self, name, plant):
        self._name = name
        self._plant = plant

    def work(self):
        self._plant.grow_all()
        print(f"{self._name} выполнил свою работу")

    def harvest(self):
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
            print("Все помидоры созрели, урожай собран")
        else:
            print("Надо подождать, не все помидоры созрели")

    @staticmethod
    def knowledge_base():
        print("Спарвка по садоводству")


Gardener.knowledge_base()
bush = TomatoBush(1)
gardner = Gardener("Olga", bush)
gardner.harvest()
gardner.work()
gardner.harvest()
gardner.work()
gardner.harvest()
