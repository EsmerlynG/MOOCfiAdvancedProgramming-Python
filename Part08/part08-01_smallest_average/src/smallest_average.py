
# Write your solution here
def smallest_average(person1: dict, person2: dict, person3: dict) -> dict:
    persons = (person1, person2, person3)
    sm_avg_person = {}
    sm_avg = 0
    index = 0
    for person in persons:
        nums = list(person.values())[1:]
        avg = sum(nums) / len(nums)

        if sm_avg == 0 or sm_avg > avg:
            sm_avg = avg
            sm_avg_person = persons[index]     

        index += 1

    return sm_avg_person
        

    




if __name__ == "__main__":
    person1 = {"name": "Mary", "result1": 2, "result2": 3, "result3": 3}
    person2 = {"name": "Gary", "result1": 5, "result2": 1, "result3": 8}
    person3 = {"name": "Larry", "result1": 3, "result2": 1, "result3": 1}
    print(smallest_average(person1, person2, person3))