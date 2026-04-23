# WRITE YOUR SOLUTION HERE:
class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def __str__(self):
        return f"{self.name}, {self.height}"

class Room:
    def __init__(self) -> None:
        self.persons = []
    
    def add(self, person: Person) -> None:
        self.persons.append(person)

    def is_empty(self) -> bool:
        return len(self.persons) == 0
    
    def print_contents(self) -> None:
        total_height = sum(person.height for person in self.persons)
        print(f"There are {len(self.persons)} persons in the room and their combined height is {total_height} cm")
    
        for person in self.persons:
            print(f"{person.name}({person.height})")


    def shortest(self) -> Person | None:
        if len(self.persons) == 0:
            return None
        
        return min(self.persons, key = lambda person: person.height)
    
    def remove_shortest(self) -> Person | None:
        if len(self.persons) == 0:
            return None
        
        shortest_person = self.shortest()
        self.persons.remove(shortest_person)

        return shortest_person
        
            

        


if __name__ == "__main__":
    room = Room()

    room.add(Person("Lea", 183))
    room.add(Person("Kenya", 172))
    room.add(Person("Nina", 162))
    room.add(Person("Ally", 166))
    room.print_contents()

    print()

    removed = room.remove_shortest()
    
    if removed == None:
        print(f"Removed from room: {removed}")
    
    else:
        print(f"Removed from room: {removed.name}")

    print()

    room.print_contents()