class Person:
    def __init__(self,name,age):
            self.name = name
            self.age = age
            self.__iq = 160
    @property
    def get_iq(self):
          return self.__iq
    
    @get_iq.setter
    def set_iq(self,nwiq):
          self.__iq = nwiq
class Physics(Person):
      def create_bomb(self):
            print(self.name,"made bomb")
class Chemestry(Person):
      def create_poison(self):
           print(self.name,"made poison") 
class Genius(Physics,Chemestry):
      pass 
person = Person("jahon",18)  
Jahon = Physics()
alisher = Chemestry("alisher",19)
Jahon.create_bomb()
alisher.create_poison()
Baxti = Genius("baxti",18)
Baxti.create_bomb()
Baxti.create_poison()

print(Baxti.get_iq())