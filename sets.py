from inspect import currentframe

studentsSet = {"John", "Jane", "Jack", "Jill"}
print(currentframe().f_lineno, ":", studentsSet)

for student in studentsSet:
    print(currentframe().f_lineno, ":", student)

print(currentframe().f_lineno, ":", "Jack" in studentsSet)

if "John" in studentsSet:
    print(currentframe().f_lineno, ":", "John is in the set")

studentsSet.add("James")
print(currentframe().f_lineno, ":", studentsSet)

studentsSet.update(["Jenny", "Jeniffer", "Joe"])
print(currentframe().f_lineno, ":", studentsSet)

studentsSet.remove("Jenny")
print(currentframe().f_lineno, ":", studentsSet)

studentsSet.discard("jenny")
print(currentframe().f_lineno, ":", studentsSet)

x=studentsSet.pop()
print(currentframe().f_lineno, ":", x)
print(currentframe().f_lineno, ":", studentsSet)

studentsSet.clear()
print(currentframe().f_lineno, ":", studentsSet)

studentsSet2 = set(("John", "Jane", "Jack", "Jill"))
print(currentframe().f_lineno, ":", studentsSet2)
