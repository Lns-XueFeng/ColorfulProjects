import random

from .vecter import Vector


MOVE_RANGE = 50   # 移动范围
MOVE_SPEED = 3   # 移动速度
INFECTIOUS_RATE = 0.3   # 感染概率
UNSAFE_DISTANCE = 5   # 过于靠近时概率性感染
INFECTIOUS_DURATION = 300   # 康复倒计时


class Person:
    def __init__(self, engine):
        self.position = Vector(
            random.randrange(0, engine.size),
            random.randrange(0, engine.size)
        )
        self.home = self.position.copy()
        self.move_target = self.home.copy()
        self.move_range = MOVE_RANGE
        self.move_speed = MOVE_SPEED
        self.step = Vector(0, 0)
        self.status = 'susceptible'   # SIR模型中的易感染者
        self.infectious_dur_left = 0

    @property
    def x(self):
        return self.position.x

    @property
    def y(self):
        return self.position.y

    def get_new_target(self):
        self.move_target = self.home + Vector(
            random.uniform(-self.move_range, self.move_range),
            random.uniform(-self.move_range, self.move_range)
        )

        self.step = (self.move_target - self.position).uniform(self.move_speed)

    def move(self):
        if self.position == self.move_target:
            self.get_new_target()

        if (self.move_target - self.position).length < self.move_speed:
            self.position = self.move_target.copy()
        else:
            self.position = self.position + self.step

    def is_close(self, other):
        if (self.position - other.position).length < UNSAFE_DISTANCE:
            return True
        return False

    def try_infect(self, other):
        if random.uniform(0, 1) < INFECTIOUS_RATE:
            other.status = "infectious"
            other.infectious_dur_left = INFECTIOUS_DURATION


class Engine:
    def __init__(self, size, population):
        self.size = size
        self.population = population
        self.person_li = []
        self.infectious_people_num = None

    def create_people(self):
        self.person_li = []
        for i in range(self.population):
            self.person_li.append(Person(self))  # 创建所有人的家

    def next_frame(self):
        infected_people = []
        susceptible_people = []
        for person in self.person_li:
            person.move()
            if person.status == "infectious":
                infected_people.append(person)
            if person.status == "susceptible":
                susceptible_people.append(person)

        for infected_person in infected_people:
            for susceptible_person in susceptible_people:
                if infected_person.is_close(susceptible_person):
                    infected_person.try_infect(susceptible_person)

            if infected_person.infectious_dur_left == 0:
                infected_person.status = "recovered"
            else:
                infected_person.infectious_dur_left -= 1

        self.infectious_people_num = len(infected_people)

    def infect(self):
        initial_infected = random.sample(self.person_li, 10)
        for inf in initial_infected:
            inf.status = "infectious"
            inf.infectious_dur_left = random.randrange(1, INFECTIOUS_DURATION)
