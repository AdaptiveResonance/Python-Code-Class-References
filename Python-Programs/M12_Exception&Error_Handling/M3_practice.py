class Number:
    def __init__(self, num):
        assert 0 <= num <= 32000 and isinstance(num, int), "Invalid Number"
        self.__num = num

    @staticmethod
    def __opr(other_number, operation):
        assert isinstance(other_number, Number), "Passed argument is not a number"
        try:
            return Number(operation(other_number.get_num()))
        except AssertionError:
            return Number(0)

    def get_num(self):
        return self.__num

    def add(self, other_number):
        return Number.__opr(other_number, self.get_num().__add__)

    def multiply(self, other_number):
        return Number.__opr(other_number, self.get_num().__mul__)

    def subtract(self, other_number):
        return Number.__opr(other_number, self.get_num().__sub__)

    def divide(self, other_number):
        assert isinstance(other_number, Number), "Passed argument is not a number"
        try:
            return Number(self.get_num() // other_number.get_num())
        except AssertionError:
            return Number(0)


number = Number(320)
other = Number(2)
print(number.divide(other).get_num())
