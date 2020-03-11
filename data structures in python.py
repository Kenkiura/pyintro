
#Lists
list1=[1,2,3,4,5,6]

print(list1[3])
print (list1[0])
print (list1[-2])

days=["mon","tue","wed","thur","fri","sat","sun"]

print (days[5:7])
print (days[5:])
print (days[5:6])
print (days[0:3])
print (days[:3])

print (type(list1))

list1.append(7)
print (list1)

print (list1.index(7))

list1.pop()

print (list1)

list1[5]="nikoradar!!"

print(list1)

list1[3]=[]
print (list1)

list1[3]=""
print (list1)

#Tuples
month=("jan","feb","mar","apr","may","jun","jul","aug","sep","oct","nov","dec")
print(month[2])

#month[2]=["jul"]
print (month)


#month.append(dec)
print(month)

print(len(month))

test = (1,2,3,[4,5,6])
print(test)

print(test[3])

test[3][1]=7
print(test[3])
#tuple structure can't be changed because it's immutable but if there's a mutable object in the tuple like a list, the list can be changed


#Nesting

list2=[1,2,[3,4,[5,6,[7,8]]]]
print(len(list2))

print(list2[2][2][2][1])

