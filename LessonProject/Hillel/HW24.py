class String(str):

    def __add__(self, other):
        return String(str(self) + str(other))

    def __sub__(self, other):
        if str(other) in str(self):
            return String(str(self).replace(str(other), '', 1))
        else:
            return String(self)
