# Eg. of hashmap in python

phone_number={
    'A':'123',
    'B':'456',
    'C':'789'
    }

print(phone_number['A'])
print(phone_number['B'])
print(phone_number['C'])

# we can access using a loop as well

for name in phone_number:
    print(name,"->",phone_number[name])


# Hash Table Class


class HashTable():
    def __init__(self):
        self.table={}

    def insert(self,key,val):
        self.table[key]=val

    def find(self,key):
        for x in self.table:
            if(x==key):
                return m[key]

    def update(self,key,val):
        self.table[key]=val

    def listAll(self):
        lst=[]
        for k in self.table:
            lst.append([k,self.table[k]])
        return lst

# Assertion Error following statement raise error when assert is wrong

assert 5==5, "Different"

# List Comprehension
lst = [x for x in range(10) if x>5] 
print(lst) # [6,7,8,9]


