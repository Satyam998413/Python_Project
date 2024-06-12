# count = 5
# while (count > 0):
#     print(count)
#     count = count - 1

for i in range(2, 4):
    print(i)

class Details:
    def __init__(self, animal, group):
        self.animal = animal
        self.group = group

obj1 = Details("Crab", "Crustaceans")
print(obj1.animal, "belongs to the", obj1.group, "group.")