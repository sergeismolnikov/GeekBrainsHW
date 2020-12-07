#1

class Matrix:
    def __init__(self, vectors):
        self.vectors = vectors


    def __str__(self):
        return "\n".join(map(str, self.vectors))

    def __add__(self, other):
        result = []
        for i in range (len(self.vectors)):
            result.append([])
            for j in range (len(self.vectors[0])):
                result[i].append(self.vectors[i][j] + other.vectors[i][j])

        return Matrix(result)


a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
b = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]


matrix_a = Matrix(a)
matrix_b = Matrix(b)


print (matrix_a + matrix_a)


# 2

from abc import ABC, abstractmethod


class Clothes(ABC):
    @staticmethod
    def count(cloth_list):
        return sum(entity.consumption for entity in cloth_list)


    @property
    @abstractmethod
    def consumption(self):
        pass

    def __add__(self,other):
        return self.consuption + other.consumption

class Coat(Clothes):
    def __init__(self, height):
        self.height = height

    @property
    def consumption(self):
        print (f"Consumption for a coat {round(self.height / 6.5)+0.5}")
        return round((self.height / 6.5)+0.5)

class Costume(Clothes):
    def __init__(self, height2):
        self.height2 = height2

    @property
    def consumption(self):
        print (f"Consumption for a costume {round(2 *self.height2 + 0.3) /0.5}")
        return (2 *self.height2 / 0.3)/100



coat1 = Coat(5)
coat2 = Coat (7)

costume = Costume(10)

aaa = [coat1,coat2,costume]

print (Clothes.count(aaa))


#3

class Cell:
    def __init__(self, nums):
        self.nums = nums

    def make_order(self, rows):
        xxx = "\n".join(["*" * rows for i in range (self.nums // rows)])
        return f'{xxx}\n{"*" * (self.nums % rows)}'

    def __str__(self):
        return str(self.nums)

    def __add__(self, other):
        return Cell(self.nums + other.nums)

    def __sub__(self, other):
        if self.nums - other.nums > 0:
                return Cell (self.nums - other.nums)
        raise ValueError ("ячеек недостаточно")
    def __mul__(self, other):
        return Cell (self.nums +other.nums)

    def __truediv__(self, other):
        return Cell(round(self.nums /other.nums))

cell1 = Cell(30)
print(cell1.make_order(10))
cell2 = Cell(20)
cell3 = cell2 + cell1

print(cell3)