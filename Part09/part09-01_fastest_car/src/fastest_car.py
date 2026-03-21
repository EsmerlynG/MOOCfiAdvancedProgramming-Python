# Write your solution after the class Car
# Do not make changes to the class!
class Car:
    def __init__(self, make: str, top_speed: int):
        self.make = make
        self.top_speed = top_speed

    def __str__(self):
        return f"Car (make: {self.make}, top speed: {self.top_speed})"

# WRITE YOUR SOLUTION HERE:
def fastest_car(cars: list[Car]) -> str:
    speed = 0
    make = ''
    for car in cars:
        if car.top_speed > speed:
            speed = car.top_speed
            make = car.make
    return make

    top_speed = max([car.top_speed for car in cars])
    return [car.make for car in cars if car.top_speed == top_speed][0]


if __name__ == "__main__":
    car1 = Car("Saab", 195)
    car2 = Car("Lada", 110)
    car3 = Car("Ferrari", 280)
    car4 = Car("Trabant", 85)

    cars = [car1, car2, car3, car4]
    print(fastest_car(cars))


