class MuffledCalculator:
    muffled = False
    def calc(self,expr):
        try:
            return eval(expr)
        except ZeroDivisionError:
            if self.muffled:
                print("Division by zero is illegal")
            else:
                raise

calculator = MuffledCalculator()


calculator.muffled = True
print(calculator.calc('10/0'))

