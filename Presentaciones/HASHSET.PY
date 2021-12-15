##HashSet 
   ##Se inicializa la estrucuta de datos Bucket
class Bucket:

   def __init__(self):
      self.value=[]
   ##Funcion de actualizar los datos 
   def update(self, key):
      found=False
      for i,k in enumerate(self.value):
         if key==k:
            self.value[i]=key
            found=True
            break
      if not found:
         self.value.append(key)
    
   ##Obtener el valor
   def get(self, key):
      for k in self.value:
         if k==key:
            return True
      return False
   ##Remover el elemento 
   def remove(self, key):
      for i,k in enumerate(self.value):
         if key==k:
            del self.value[i]
 
##clase HashSet
class HashSet:
   def __init__(self):
      self.key_space = 2096
      self.hash_table=[Bucket() for i in range(self.key_space)]
   def hash_values(self, key):
       hash_key=key%self.key_space
       return hash_key
   ##Añadir elementos
   def add(self, key):
      self.hash_table[self.hash_values(key)].update(key)
   ##Eliminar elementos
   def remove(self, key):
      self.hash_table[self.hash_values(key)].remove(key)
   ##Funcion contains
   def contains(self, key):
      return self.hash_table[self.hash_values(key)].get(key)
   ####Funcion para imprimir    
   def display(self):
       ls=[]
       for i in self.hash_table:
           if len(i.value)!=0:ls.append(i.value[0])
       print(ls)

x=HashSet()
print(x.hash_values(5))
x.add(5)
x.add(6)
x.add(3)
x.add(4)
x.add(1)
x.add(1)
x.add(9)
x.display()
print("Contiene a 5: ", x.contains(5))
print("Contiene a 6: ", x.contains(8))
print("Contiene a 10: ", x.contains(10))
x.add(2)
print("Contiene a 2: ", x.contains(2))
x.remove(2)
print("Contiene a 2: ", x.contains(2))
x.display()




##Fuente: https://www.pythonpool.com/python-hashset/




a=[5,4,1]
b=[2,3,4]
nuevalista=[]
 
for i in range(len(a)):
	nuevalista.append(a[i]+b[i])
 
print (nuevalista)

