class Lion:
    def __init__ (self, name):
        self.name = name

    def __repr__ (self):
        return self.name

lion = Lion ("jj")
print(lion)


        
    
x=None
if x is None:
    print ("x равно None")
else:
    print("x равно None:(")



#Добавьте переменную square_list в класс Square так, чтобы всякий раз,
#когда вы создаете новый объект Square, он добавлялся в список

class Square:
    square_list = []

    def __init__ (self, w1,w2,l1, l2):
        self.width1 = w1
        self.width2 = w2
        self.len1 = l1
        self.len2 = l2
        self.square_list.append((self.width1,self.width2,
                          self.len1, self.len2))

    
    def __repr__ (self):
        return "{} на {} на {} на {}".format(self.width1,self.width2,
                         self.len1, self.len2)


s1 = Square (10,10,33,44)
s2 = Square (11,22,23,21)

print (s1)  


#Напишите функцию, которая принимает два объекта в качестве параметров
#и возвращает True, если они являются одним и тем же объектом, и False в
#противном случае.

class Objects:
    def __init__(self):
        self.name = 'bob'

bob = Objects()
same_bob = bob
print(bob is same_bob)

another_bob = Objects()
print(bob is another_bob)
