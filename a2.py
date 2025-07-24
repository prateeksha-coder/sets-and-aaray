setx = {"green", "blue"}
sety = {"blue", "yellow"}
print("Original set elements:")
print(setx)
print(sety)
print("\nIntersection of two said sets:")
setz = setx.intersection(sety)
print(setz)
setc = setx.union(sety)
print("\nUnion of above sets:")
print(setc)
print("Difference")
print(setx.difference(sety))#set1-set2
print("Symmeteric Difference")
print(setx.symmetric_difference(sety))

