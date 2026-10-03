import random

rooms = {
    "A": input("Enter the state of Room A (dirty/clean): ").lower(),
    "B": input("Enter the state of Room B (dirty/clean): ").lower(),
    "C": input("Enter the state of Room C (dirty/clean): ").lower()
}


def is_dirty(room):
    return rooms[room] == "dirty"


def clean_room(room):
    rooms[room] = "clean"


def display_grid(agent_location):
    print("\nText-Based Grid:")
    print("+-----------+")
    
    for room in rooms:
        state = rooms[room].upper()
        
        if room == agent_location:
            print(f"| [{room}*] {state:<6}|")
        else:
            print(f"| [{room}]  {state:<6}|")
    
    print("+-----------+")


class VacuumAgent:

    def __init__(self, location):
        self.location = location

    def move_to_random_dirty_room(self):
        dirty_rooms = [
            room for room in rooms
            if is_dirty(room)
        ]

        if dirty_rooms:
            self.location = random.choice(dirty_rooms)
            return True

        return False

    def perceive_and_act(self):

        if is_dirty(self.location):
            clean_room(self.location)
            return "Cleaned Room " + self.location

        else:
            if self.move_to_random_dirty_room():
                return "Moved to Room " + self.location
            else:
                return "All rooms are clean"


print("\nInitial Environment:")
for room in rooms:
    print("Room", room + ":", rooms[room])

agent = VacuumAgent("A")

steps = int(input("\nEnter number of simulation steps: "))

print("\nSimulation Started")
print("----------------------------")

display_grid(agent.location)

for step in range(1, steps + 1):

    action = agent.perceive_and_act()

    print("\nStep", step)
    print("Agent Location:", agent.location)
    print("Action:", action)

    for room in rooms:
        print("Room", room + ":", rooms[room])

    display_grid(agent.location)


print("\nSimulation Finished")
print("----------------------------")

print("Final Environment:")

for room in rooms:
    print("Room", room + ":", rooms[room])

print("Agent Location:", agent.location)
