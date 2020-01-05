import string

# This Program was developed by Rajesh Ramesh without cloning from any sources
# TimeStamp --> 03-01-2019 10.25pm
# IDE: Pycharm Community edition 2019
# Operating System: Windows 10

class Robot:
    def __init__(self, name, x, y, move):
        self.name = name
        self.x = x
        self.y = y
        self.movement = move

    def left(self, steps):
        self.x -= steps

    def right(self, steps):
        self.x += steps

    def up(self, steps):
        self.y += steps

    def down(self, steps):
        self.y -= steps

    def __str__(self):
        return "Robot({0},{1},{2},{3})".format(self.name, self.x, self.y, self.movement)


inputs = open("input.txt", "r")
robots = []
for line in inputs:
    robot_name, x_pos, y_pos, moves = line.strip("\n").split(",")
    robots.append(Robot(robot_name, int(x_pos), int(y_pos), moves))
step = 1
for bot in robots:
    for movement in bot.movement:
        if movement in string.digits:
            step = int(movement)
            continue
        else:
            if movement == "U":
                bot.up(step)
            if movement == "D":
                bot.down(step)
            if movement == "L":
                bot.left(step)
            if movement == "R":
                bot.right(step)
        step = 1

result = {}
for robot in robots:
    key = str(robot.x) + ',' + str(robot.y)
    if key not in result:
        result[key] = [robot.name]
    else:
        result.update(key=result[key].append(robot.name))
del result["key"]
print(result)
output = open("output.txt", "a")
for res in result:
    output.write("\n{},{}".format(res, ":".join(result[res])))
inputs.close()
output.close()
