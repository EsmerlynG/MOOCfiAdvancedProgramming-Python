# WRITE YOUR SOLUTION HERE:
class Car:
    def __init__(self) -> None:
        self.__tank = 0
        self.__odometer = 0

    def __str__(self) -> str:
        return f"Car: odometer reading {self.__odometer} km, petrol remaining {self.__tank} litres"
    
    def fill_up(self) -> None:
            self.__tank = 60
    
    def drive(self, km: int) -> None:
        if km > self.__tank:
             km = self.__tank
        
        self.__odometer += km
        self.__tank -= km
            


if __name__ == "__main__":
    car = Car()
    print(car) 
    car.fill_up() 
    print(car) 
    car.drive(20) 
    print(car)
    car.drive(50)
    print(car)
    car.drive(10)
    print(car)
    car.fill_up()
    car.fill_up()
    print(car)
  
