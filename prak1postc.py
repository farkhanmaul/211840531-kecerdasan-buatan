from kanren.facts import Relation, facts
from kanren.core import var, run, conde, eq

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
