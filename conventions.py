class MyClass:
    def __init__(self, name):
        self.name = name
        self.long_name = "This is an attribute with a long name"
        self.protected_attribute = "This can only be accessed from this superclass and its subclasses"
        self.private_attribute = "This can only be accessed from this class"

    @property
    def protected_attribute(self):
        return self._protected_attribute

    @protected_attribute.setter
    def protected_attribute(self, protected_attribute):
        self._protected_attribute = protected_attribute

    @property
    def private_attribute(self):
        return self.__private_attribute

    @private_attribute.setter
    def private_attribute(self, private_attribute):
        self.__private_attribute = private_attribute

        

my_object = MyClass('Vibe')

"""
Kommentar kommentar
"""

