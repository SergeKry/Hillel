class Name:
    def __init__(self, name, surname):
        self.first_name = str(name).title()
        self.last_name = str(surname).title()
        self.full_name = str(f'{self.first_name} {self.last_name}')
        self.initials = str(f'{self.first_name[0]}.{self.last_name[0]}')


