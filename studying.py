class Tv:
    color = 'красный'
    type_tv = 'oled'
    def __init__(self, what_is_razmer):
        self.razmer = what_is_razmer

lg = Tv(what_is_razmer = 65)
print (lg.razmer)
print (type(lg))