# Write your solution here:
from datetime import datetime, timedelta
class Clock:
    def __init__(self, h: int, m: int, s: int) -> None:
        self.clock = timedelta(hours=h, minutes=m, seconds=s)
    
    def __str__(self):
        base = datetime(2000,1,1)
        time = (base + self.clock).strftime("%H:%M:%S")
        return f"{time}"
    
    def tick(self):
        self.clock += timedelta(seconds=1)
    
    def set(self, h, m):
        self.clock = timedelta(hours=h, minutes=m)


if __name__ == "__main__":
    clock = Clock(23, 59, 55)
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)

    clock.set(12, 5)
    print(clock)
