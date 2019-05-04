class Worker:
    """Writed for create easily worker information"""

    extra = 1.8
    count = 0

    def __init__(self,name,surname,time,money):
        self.name = name
        self.surname = surname
        self.time = time
        self.money = money
        Worker.count += 1

    def changetime(self):
        if(self.time=="weekday"):
            self.time = "weekend"
        elif(self.time=="weekend"):
            self.time = "weekday"

    def doraise(self):
        self.money = self.money * Worker.extra

    def changename(self,x):
        self.name = x

print("")
print("Add new class:".upper())
print("Worker(name,surname,time,money)")

Alperen = Worker("Alperen","Ağa","weekend",5000)
Mehmet = Worker("Mehmet","Ünlütürk","weekday",7500)
Danyal = Worker("Danyal","Babur","weekday",4000)

print("")

print("Self.name".upper())
print(Alperen.name)
print(Mehmet.name)
print(Danyal.name)

print("")

print("Self.time".upper())
print(Alperen.time)
print(Mehmet.time)
print(Danyal.time)

print("")

print("Self.changetime".upper())

Alperen.changetime()
print(Alperen.time)
Mehmet.changetime()
print(Mehmet.time)
Danyal.changetime()
print(Danyal.time)

print("")

print("Self.Money".upper())
print("Alperen:",Alperen.money)
print("Mehmet:",Mehmet.money)
print("Danyal:",Danyal.money)

print("")

print("Self.doraise()".upper())

Alperen.doraise()
Mehmet.doraise()
Danyal.doraise()
print("Alperen",Alperen.money)
print("Mehmet",Mehmet.money)
print("Danyal",Danyal.money)

print("")

print("Class.Count()".upper())
print(Worker.count)

print("")

print("Self.changename".upper())

Alperen.changename("Deneme1")
Mehmet.changename("Deneme2")
Danyal.changename("Deneme3")

print("Alperen:",Alperen.name)
print("Mehmet:",Mehmet.name)
print("Danyal:",Danyal.name)

Alperen.changename("Alperen")
Mehmet.changename("Mehmet")
Danyal.changename("Danyal")

print("")

print("Writed by Alperen")
