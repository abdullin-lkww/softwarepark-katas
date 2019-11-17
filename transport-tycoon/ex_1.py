import sys

INPUT = 'AABABBAB' if len(sys.argv) == 1 else sys.argv[1]
print(f"Deliver {INPUT}")

FACTORY = list(INPUT)
A = []
B = []
PORT = []

WORLD = {'FACTORY': FACTORY, 'PORT': PORT, 'A': A, 'B': B}
PLAN = {
    ('TRUCK', 'FACTORY', 'A'): ('PORT', 1),
    ('TRUCK', 'FACTORY', 'B'): ('B', 5),
    ('TRUCK', 'PORT', None): ('FACTORY', 1),
    ('TRUCK', 'B', None): ('FACTORY', 5),
    ('SHIP', 'PORT', 'A'): ('A', 4),
    ('SHIP', 'A', None): ('PORT', 4),
}
TIME = 0


class Transport:
    def __init__(self, loc, kind):
        self.loc = loc
        self.kind = kind
        self.eta = 0
        self.cargo = None

    def move(self):
        if self.eta > TIME:
            # print(f"{self.kind} arrives to {self.loc} in {self.eta-TIME}")
            return

        place = WORLD[self.loc]
        if self.cargo:
            place.append(self.cargo)
            print(f'  {self.kind} drops {self.cargo} at {self.loc}')
            self.cargo = None
        else:
            if place:
                self.cargo = place.pop(0)
                print(f'  {self.kind} picks {self.cargo} at {self.loc}')

        plan = (self.kind, self.loc, self.cargo)

        if plan in PLAN:
            destination, eta = PLAN[plan]
            self.loc = destination
            self.eta = eta + TIME
        else:
            # print(f'{self.kind} has no plan for {plan}')
            pass


transport = [Transport('FACTORY', 'TRUCK'), Transport('FACTORY', 'TRUCK'), Transport('PORT', 'SHIP')]


def cargo_delivered():
    return len(A) + len(B) == len(INPUT)


while not cargo_delivered():
    print(TIME)

    for t in transport:
        t.move()

    TIME +=1
