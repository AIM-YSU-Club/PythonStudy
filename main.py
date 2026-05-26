class Person():
    name: str
    height: int

    def sayHello(self):
        print('Hello, My name is ' + self.name)
    
    def Conversation(self, other_person):
        self.sayHello()
        other_person.sayHello()

    

person1 = Person()
person1.name = '유성원'

person2 = Person()
person2.name = '이상엽'

person1.Conversation(person2)
