class Gamer:
    company = "Nvidia"
    level = 0

    def upgradeLevel(self):
        self.level = self.level + 1

class Livestreamer:
    company = "Dice"
    eCode = 120


class Programmer(Livestreamer , Gamer):
    name = "Dr Disrespect"

p = Programmer()
p.upgradeLevel()
print(p.level)