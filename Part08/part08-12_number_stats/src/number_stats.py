# Write your solution here!
class NumberStats:
    
    def __init__(self) -> None:
        self.numbers = []
    
    def add_number(self, number:int):
        self.numbers.append(number)
        

    def count_numbers(self) -> int:
        return len(self.numbers)
    
    def get_sum(self) -> int:
        return sum(self.numbers)
    
    def average(self) -> float:
        
        if not self.numbers:
            return 0.0
        else:
            return sum(self.numbers) / len(self.numbers)
    
    def sum_of_even_odd(self) -> tuple:
        odd = 0
        even = 0
        
        for num in self.numbers:
            if num % 2:
                odd += num
            else:
                even += num
            
        return even, odd
    

stats = NumberStats()
while True:
    num = int(input("Please type in integer numbers: "))
    if num == -1:
        break
        
    stats.add_number(num)

# print("Numbers added:", stats.count_numbers())
even, odd = stats.sum_of_even_odd()
print("Sum of numbers:", stats.get_sum())
print("Mean of numbers:", stats.average())
print("Sum of even numbers:", even)
print("Sum of odd numbers:", odd)