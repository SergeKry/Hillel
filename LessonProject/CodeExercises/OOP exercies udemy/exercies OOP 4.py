class Pizza:
    ORDER_NUMBER = 0

    def __init__(self, ingredients):
        Pizza.ORDER_NUMBER += 1
        self.order_number = Pizza.ORDER_NUMBER
        self.ingredients = ingredients

    @classmethod
    def garden_feast(self):
        ingredients = ['spinach', 'olives', 'mushroom']
        return Pizza(ingredients)

    @classmethod
    def hawaiian(self):
        ingredients = ['ham', 'pineapple']
        return Pizza(ingredients)

    @classmethod
    def meat_festival(self):
        ingredients = ['beef', 'meatball', 'bacon']
        return Pizza(ingredients)

