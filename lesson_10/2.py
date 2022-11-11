import time

class Mob:
    def __init__(self, x, y, h_speed, v_speed, hp, mana, weapon, ability, is_enemy):
        self.x = x
        self.y = y
        if is_enemy == True:
            self.color = "red"
        else:
            self.color = "blue"
        self.hp = hp
        self.h_speed = h_speed
        self.v_speed = v_speed
        self.mana = mana
        self.weapon = weapon
        self.ability = ability

    def update(self):
        self.x = self.x + self.h_speed

run = True
mob_1 = Mob(0, 0, 1, 1, 100, 100, "pistol", "nothing", True)
while run == True:
    map = ["."] * 120
    map[mob_1.x] = "E"
    mob_1.update()
    print("".join(map))
    time.sleep(0.2)
