#x= int(input("enter num"))
#y=0
#List= []
#while y<x:
  #List.append(int(input("enter num")))
  #y= y+1
#print (List)


#List.insert(1,99)
#print (List)

#List.remove (99)
#List.insert(1,100)

#print (List)

#aman=[500,600,700,800,900]
#print (aman)

#List.extend (aman)
#print (List)

#List.remove (800)
#print (list)

#list.pop(2)
#print (list)

grades=["A","B","C","A","A","C"]
x=grades.count("A")
print (x)

a=grades.index("B")
print (a)

z=grades.count ("F")
if z==0:
 print ("F is not in the list")

second_list = [500, 600, 700, 800, 900]
print("Second List before clearing:", second_list)

second_list.clear()
print("Second List after clearing:", second_list)

del second_list

players = ["Rizzo", "Davis", "Baez", "Happ", "Bryan"]
print("Original list of players:", players)

players.sort()
print("Sorted list of players:", players)

players2 = players.copy()
print("Copy of the list of players (players2):", players2)

players2.reverse()
print("Reversed order of players2:", players2)