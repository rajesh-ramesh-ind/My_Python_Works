electricity = True
current = 0
ground_floor = 0
top_floor = 5


def up(present, dest):
    while present < dest:
        print("going up")
        present += 1
    return present


def down(present, dest):
    while present > dest:
        print("going down")
        present -= 1
    return present


while electricity:
    destination = int(input("enter the destination floor"))
    if ground_floor <= destination <= top_floor:
        if destination < current:
            current = down(current, destination)
            print("Elevator @ floor {}".format(current))
        if destination > current:
            current = up(current, destination)
            print("Elevator @ floor {}".format(current))
        else:
            print("You're in this floor ->{}".format(destination))
    else:
        print("There are only {} floors".format(top_floor))
