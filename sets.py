#Radhe Radhe
#This is for sets.
s=set()
print(type(s))

#elemens cannot be repeated in a set
#even if we add duplicate values to the sets , the interpreter will still give them as single.
s={1,2,3,4,5,6,7,"harry"}
print(s)

#Meethods on sets.
q=set()
q.add(2)
print(q)

q.update([9,8,7])
print(q)

#the output we get is {8,9,2,7} and not {2,9,8,7}
#This happens as the python language does maintains the sequence and order in case of sets.
#And sets use hash values to insert the values due to which he order of the values stored inthe set is not fixed or sequenced.

p={1,3,9}
p.update([2,4,3])
print(p)


#remove
p.remove(2)
print(p)
#In case of remove if we try to remove an element which is not presesnt in the set, it raises an error.
#But to avoid this error we  use the discard method.
#The discard method doesnot returns an error if the element is not present in the set.

p.discard(10)
print(p)

#pop
#It removes an element from the start of the set.
p.pop()
print(p)
p.pop()
print(p)

print(p)
p.clear()
print(p)


#Union
set1={1,2,3,4,5}
set2={4,5,6}
print(set1.union(set2))

#Intersection
print(set1.intersection(set2))

#Difference
print(set1.difference(set2))

#Symmetric Difference
print(set1.symmetric_difference(set2))

#Subset and Superset checks
set3={1,2,3,4,5}
set4={4,5}
print(set4.issubset(set3))
print(set3.issuperset(set4))

#Disjoint checks (Check whether there is any common element in both the sets.)
a={1,2}
b={4,6}
print(a.isdisjoint(b))

c={6,7,9}
d={6,5,4}
print(c.isdisjoint(d))


#Copying Sets.
original_set={1,3,5}
copied_set=original_set.copy()
print(copied_set)

#Length
print(len(original_set))

#Membership Testing  (returns either true or false)
my_set={1,2,3,44}

#1)element in set
print(1 in my_set)
#output=True

#2)element not in set
print(88 not in my_set)
#output=True




#Set Comprehensions
squares={x**2 for x in range(8)}
print(squares)

#Output may be ordered or inordered due the property
#of sets of arranging the elements based on their 
#hash values.