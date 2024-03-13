import functools


class FactorialError(Exception):
    pass


class Calculator:

    def __init__(self, a):
        self.a = a

    def add(self, b):
        try:
            return self.a + b
        except TypeError:
            print('Please enter a number')
        except Exception as err:
            print('Oops, something went wrong: {}'.format(err))

    def subtract(self, b):
        try:
            return self.a - b
        except TypeError:
            return "Please enter a number"
        except Exception as err:
            print('Oops, something went wrong: {}'.format(err))

    def multiply(self, b):
        try:
            return self.a * b
        except TypeError:
            return "Please enter a number"
        except Exception as err:
            print('Oops, something went wrong: {}'.format(err))

    def divide(self, b):
        try:
            return self.a / b
        except TypeError:
            return "Please enter a number"
        except ZeroDivisionError:
            return "Cannot divide by zero"
        except Exception as err:
            print('Oops, something went wrong: {}'.format(err))

    def exponentiation(self, b):
        try:
            return self.a ** b
        except TypeError:
            return "Please enter a number"
        except Exception as err:
            print('Oops, something went wrong: {}'.format(err))

    def sqrt(self):
        try:
            return self.a ** 0.5
        except TypeError:
            return "Only number can get square root"
        except Exception as err:
            print('Oops, something went wrong: {}'.format(err))

    def factorial(self):
        try:
            if self.a < 0:
                raise FactorialError("Factorial can't be negative")
            elif self.a == 0:
                return 1
            else:
                return functools.reduce(lambda x, y: x*y, range(1, self.a+1))
        except TypeError:
            return "You can do factorial only for integers"
        except FactorialError as err:
            return err
        except Exception as err:
            print('Oops, something went wrong: {}'.format(err))
