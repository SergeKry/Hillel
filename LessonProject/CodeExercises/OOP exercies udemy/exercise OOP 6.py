prices = {"Strawberries": 1.5, "Banana": 0.5, "Mango": 2.5, "Blueberries": 1 ,"Raspberries": 1, "Apple": 1.75,
          "Pineapple": 3.5}


class Beverage:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    def get_cost(self):
        cost = 0
        for item in self.ingredients:
            cost += prices.get(item)
        cost = round(cost, 2)
        return '${cost:.2f}'.format(cost=cost)

    def get_price(self):
        cost = 0
        for item in self.ingredients:
            cost += prices.get(item)
        price = round(cost * 2.5, 2)
        return '${price:.2f}'.format(price=price)

    def get_name(self):
        type = 'Fusion' if len(self.ingredients) > 1 else 'Smoothie'
        ingredients = []
        for item in sorted(self.ingredients):
            if 'berries' in item:
                item = item[:-3] + 'y'
                ingredients.append(item)
            else:
                ingredients.append(item)
        ingredients.append(type)
        return ' '.join(ingredients)

