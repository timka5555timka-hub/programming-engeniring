class Tomato:
    """Класс, описывающий один помидор"""

    STAGES = ['отсутствует', 'цветение', 'зеленый', 'красный']

    def __init__(self, number):
        # приватные динамические свойства
        self._number = number
        self._stage = 0
        print(
            f"Создан помидор №{self._number}: стадия '{self.STAGES[self._stage]}'")

    def grow(self):
        """Переход на следующую стадию созревания"""
        if self._stage < len(self.STAGES) - 1:
            self._stage += 1
            print(
                f"Помидор {self._number} → стадия '{self.STAGES[self._stage]}'")

    def is_ready(self):
        """Проверка зрелости"""
        return self._stage == len(self.STAGES) - 1


class TomatoBush:
    """Класс, моделирующий куст с несколькими помидорами"""

    def __init__(self, count):
        self.tomatoes = [Tomato(i + 1) for i in range(count)]
        print(f"\nПосажен куст с {count} помидорами!\n")

    def grow_all(self):
        """Все помидоры растут"""
        print("Куст растет...")
        for tomato in self.tomatoes:
            tomato.grow()

    def are_all_ripe(self):
        """Все ли плоды созрели"""
        return all(tomato.is_ready() for tomato in self.tomatoes)

    def collect_all(self):
        """Сбор урожая (очистка списка)"""
        self.tomatoes.clear()
        print("Куст пуст — урожай собран!")


class Gardener:
    """Класс садовника"""

    def __init__(self, name, plant):
        self.name = name           # публичное свойство
        self._plant = plant        # приватное свойство
        print(f"Садовник {self.name} начал ухаживать за кустом.\n")

    def care(self):
        """Садовник ухаживает за растением"""
        print(f"{self.name} поливает и рыхлит землю...")
        self._plant.grow_all()

    def gather(self):
        """Проверка и сбор урожая"""
        print(f"\n{self.name} проверяет зрелость урожая...")
        if self._plant.are_all_ripe():
            print("Все помидоры красные! Можно собирать!")
            self._plant.collect_all()
        else:
            print("Еще не все помидоры спелые. Нужно подождать.")

    @staticmethod
    def help():
        """Справка по садоводству"""
        print("=" * 55)
        print(" С П Р А В К А   П О   С А Д О В О Д С Т В У ")
        print("=" * 55)
        print("1. Посадите куст с помидорами.")
        print("2. Ухаживайте за ним, пока все плоды не покраснеют.")
        print("3. Соберите урожай и радуйтесь результату!")
        print("=" * 55)


# ===== Тестирование программы =====
if __name__ == '__main__':
    Gardener.help()
    bush = TomatoBush(4)
    gardener = Gardener("Алексей", bush)

    gardener.care()
    gardener.gather()

    gardener.care()
    gardener.gather()

    gardener.care()
    gardener.gather()
