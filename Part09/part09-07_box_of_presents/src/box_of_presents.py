# WRITE YOUR SOLUTION HERE:

class Present:
    def __init__(self, name: str, weight: int) -> None:
        self.name = name
        self.weight = weight

    def __str__(self) -> str:
        return f"{self.name}({self.weight}kg)"

class Box:
    def __init__(self) -> None:
        self.presents = []

    def add_present(self, present: Present) -> None:
        self.presents.append(present)
    
    def total_weight(self) -> int:
        return sum(present.weight for present in self.presents)
    
            

if __name__ == "__main__":
    book = Present("ABC Book", 2)
    print("The name of the present:", book.name)
    print("The weight of the present:", book.weight)
    print("Present", book)

    box = Box()
    box.add_present(book)
    print(box.total_weight())

    cd = Present("Pink Floyd: Dark Side of the Moon", 1)
    box.add_present(cd)
    print(box.total_weight())