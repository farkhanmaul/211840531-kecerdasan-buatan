from kanren.facts import Relation, facts
from kanren.core import var, run, conde, eq

def get_sibling(x, y):
    temp = var()
    return conde((parent(temp, x), parent(temp, y)))

parent = Relation()
facts(parent, ("Slamet", "Amin"),
        ("Slamet", "Anang"),
        ("Amin", "Badu"),
        ("Amin", "Budi"),
        ("Anang", "Didi"),
        ("Anang", "Dadi"))

x = var()
child = "Amin"
ayah = run(1, x, parent(x, child))
print("\nNama ayah " + child + ": ")
for item in ayah:
    print(item)

siblings = run(0, x, get_sibling(x, "Badu"))
siblings = [x for x in siblings if x != "Badu"]
print("\nNama saudara Badu : ")
for item in siblings:
    print(item)

siblings = run(0, x, get_sibling(x, "Budi"))
siblings = [x for x in siblings if x != "Budi"]
print("\nNama saudara Budi : ")
for item in siblings:
    print(item)