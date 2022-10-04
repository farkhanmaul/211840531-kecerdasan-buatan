from kanren.core import var, eq, run
from kanren.facts import Relation, facts

father = Relation()
facts(father, ("Homer", "Bart"),
("Homer", "Lisa"),
("Abe", "Homer"))

x = var()
output = run(1, x, father(x, "Bart"))
print("Ayah Bart adalah : ", output[0])
