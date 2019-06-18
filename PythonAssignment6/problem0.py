'''
- Look around your classroom or your bedroom and come up with 5 classes that you see there.
- No.1 For each class define 5 instance Variables
- No.2 For each class define 1 static variable
- No.3 For each class define an accessor and a mutator for each instance variable
- No.4 For each class define 2 instance methods in addition to the accessors and the mutators.
- No.5 For each class define a constructor which initializes all its instance variables.

 - No.1 あなたの教室や寝室を見回して、そこに見える5つのクラスを思い付きましょう。
 - No.2 各クラスに5つのインスタンス変数を定義
 - No.3 クラスごとに1つの静的変数を定義します
 - No.4 クラスごとに、インスタンス変数ごとにアクセサとミューテータを定義する
 - No.5 ???各クラスに対して、アクセサとミューテータに加えて2つのインスタンスメソッドを定義します。
 - No.6 各クラスに対して、そのすべてのインスタンス変数を初期化するコンストラクタを定義します。
'''

import random

class Human():
    def __init__(self, name, country, eyes, hight, age):
        # instanc variable (No.2.6)
        self.name = name
        self.country = country
        self.eyes = eyes
        self.hight = hight
        self.age = age

    # Accessor Methods (No.4)
    def get_name(self):
        return self.name

    def get_country(self):
        return self.country

    def get_eyes(self):
        return self.eyes

    def get_hight(self):
        return self.hight

    def get_age(self):
        return self.age

    # Mutator Methods (No.4)
    def set_name(self, name):
        self.name = name

    def set_country(self, country):
        self.country = country

    def set_eyes(self, eyes):
        self.eyes = eyes

    def set_hight(self, hight):
        self.hight = hight

    def set_age(self, age):
        self.age = age

    # Instance Methods (No.5)
    def self_taka(self):
        print('Taka is from ' + someone.get_country() + '.')

    def self_kim(self):
        print("Kim's hight is " + someone.get_hight() + "cm.")

    # static variable (class variable) (No.3)
    hmp = random.randint(2,30)

print('Today there is', Human.hmp, 'people in the class.')

someone = Human('Taka', 'Japan', 'Black', '171', '31')
someone.self_taka()

someone.set_name("Kim")
someone.set_country("Korea")
someone.set_eyes("Black")
someone.set_hight("175")
someone.set_age("30")
someone.self_kim()


class Computer():
    def __init__(self, os, kind, cpu, memory, storage):
        # instanc variable (No.2.6)
        self.os = os
        self.kind = kind
        self.cpu = cpu
        self.memory = memory
        self.storage = storage

    # Accessor Methods (No.4)
    def get_os(self):
        return self.os

    def get_kind(self):
        return self.kind

    def get_cpu(self):
        return self.cpu

    def get_memory(self):
        return self.memory

    def get_storage(self):
        return self.storage

    # Mutator Methods (No.4)
    def set_os(self, os):
        self.os = os

    def set_kind(self, kind):
        self.kind = kind

    def set_cpu(self, cpu):
        self.cpu = cpu

    def set_memory(self, memory):
        self.memory= memory

    def set_storage(self, storage):
        self.storage = storage

    # Instance Methods (No.5)
    def self_mac(self):
        print("These are my new computer's spec.\n"
              + "OS: " + computer.get_os() + '\n'
              + "Kind: " + computer.get_kind() + '\n'
              + "CPU: " + computer.get_cpu() + '\n'
              + "Memory: " + computer.get_memory() + '\n'
              + "Storage: " + computer.get_storage() + '\n')

    def self_win(self):
        print("These are his computer's spec.\n"
              + "OS: " + computer.get_os() + '\n'
              + "Kind: " + computer.get_kind() + '\n'
              + "CPU: " + computer.get_cpu() + '\n'
              + "Memory: " + computer.get_memory() + '\n'
              + "Storage: " + computer.get_storage() + '\n')

    # static variable (class variable) (No.3)
    hmc = 10

print('\nthere is only', Computer.hmc, 'computers in the class.')


computer = Computer('macOSX', 'laptop', 'IE5-2650V3', '16GB', 'SSD 1TB')
computer.self_mac()

computer.set_os("win10")
computer.set_kind("desktop")
computer.set_cpu("i9-9980XE")
computer.set_memory("24GB")
computer.set_storage("SSD 512GB, HDD 4TB")
computer.self_win()


class Phone():
    def __init__(self, os, colour, screen, memory, price):
        # instanc variable (No.2.6)
        self.os = os
        self.colour = colour
        self.screen = screen
        self.memory = memory
        self.price = price

    # Accessor Methods (No.4)
    def get_os(self):
        return self.os

    def get_colour(self):
        return self.colour

    def get_screen(self):
        return self.screen

    def get_memory(self):
        return self.memory

    def get_price(self):
        return self.price

    # Mutator Methods (No.4)
    def set_os(self, os):
        self.os = os

    def set_colour(self, colour):
        self.colour = colour

    def set_screen(self, screen):
        self.screen = screen

    def set_memory(self, memory):
        self.memory= memory

    def set_price(self, price):
        self.price = price

    # Instance Methods (No.5)
    def self_BlackBerry(self):
        print("I bought this phone!\n"
              + "OS: " + phone.get_os() + '\n'
              + "colour: " + phone.get_colour() + '\n'
              + "screen: " + phone.get_screen() + '\n'
              + "Memory: " + phone.get_memory() + '\n'
              + "price: " + phone.get_price() + '\n')

    def self_WindowsPhone(self):
        print("His phone is this.\n"
              + "OS: " + phone.get_os() + '\n'
              + "colour: " + phone.get_colour() + '\n'
              + "screen: " + phone.get_screen() + '\n'
              + "Memory: " + phone.get_memory() + '\n'
              + "price: " + phone.get_price() + '\n')

    # static variable (class variable) (No.3)
    hmp = 2

print('\nI have', Phone.hmp, 'iphone.')


phone = Phone('Black Berry', 'White', '5inch', '500MB', '200CAD')
phone.self_BlackBerry()

phone.set_os("Windows Phone")
phone.set_colour("Black")
phone.set_screen("12inch")
phone.set_memory("1TB")
phone.set_price("1,600CAD")
phone.self_WindowsPhone()


class Dog():
    def __init__(self, name, kind, age, sex, weight):
        # instanc variable (No.2.6)
        self.name = name
        self.kind = kind
        self.age = age
        self.sex = sex
        self.weight = weight

    # Accessor Methods (No.4)
    def get_name(self):
        return self.name

    def get_kind(self):
        return self.kind

    def get_age(self):
        return self.age

    def get_sex(self):
        return self.sex

    def get_weight(self):
        return self.weight

    # Mutator Methods (No.4)
    def set_name(self, name):
        self.name = name

    def set_kind(self, kind):
        self.kind = kind

    def set_age(self, age):
        self.age = age

    def set_sex(self, sex):
        self.sex = sex

    def set_weight(self, weight):
        self.weight = weight

    # Instance Methods (No.5)
    def self_dachshund(self):
        print('She has ' + dog.get_kind() + '.')

    def self_goldenRetriever(self):
        print("CICCC has " + dog.get_kind() + ".")

    # static variable (class variable) (No.3)
    hmd = random.randint(2,100)

print('I have', Dog.hmd, 'dogs.')

dog = Dog('Apple', 'Dachshund', '3', 'Female', '3000g')
dog.self_dachshund()

dog.set_name("Milo")
dog.set_kind("Golden Retriever")
dog.set_age("7")
dog.set_sex("Female")
dog.set_weight("8000g")
dog.self_goldenRetriever()


class Cat():
    def __init__(self, name, kind, age, sex, weight):
        # instanc variable (No.2.6)
        self.name = name
        self.kind = kind
        self.age = age
        self.sex = sex
        self.weight = weight

    # Accessor Methods (No.4)
    def get_name(self):
        return self.name

    def get_kind(self):
        return self.kind

    def get_age(self):
        return self.age

    def get_sex(self):
        return self.sex

    def get_weight(self):
        return self.weight

    # Mutator Methods (No.4)
    def set_name(self, name):
        self.name = name

    def set_kind(self, kind):
        self.kind = kind

    def set_age(self, age):
        self.age = age

    def set_sex(self, sex):
        self.sex = sex

    def set_weight(self, weight):
        self.weight = weight

    # Instance Methods (No.5)
    def self_servelcat(self):
        print('She has ' + cat.get_kind() + '.')

    def self_tiger(self):
        print("I have " + cat.get_kind() + ".")

    # static variable (class variable) (No.3)
    hmc = random.randint(100,1000)

print('\nI have', Cat.hmc, 'cats.')

cat = Cat('Mike', 'Serval cat', '2', 'Female', '2700g')
cat.self_servelcat()

cat.set_name("Dinosaur")
cat.set_kind("Tiger")
cat.set_age("4")
cat.set_sex("Male")
cat.set_weight("240000g")
cat.self_tiger()