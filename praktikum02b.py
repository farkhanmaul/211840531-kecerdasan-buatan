# Program aktivitas 2
from kanren.facts import Relation, facts, fact
from kanren.core import var, run
from kanren.goals import membero
suka = Relation()
facts(suka, ("ellen", "tenis"),
("john", "football"),
("mary", "renang"),
("tom", "tenis"),
("eric", "renang"))
x = var()

mary_hobbies = run(0, x, suka("mary", x))
ann_hobbies = run(0, x, suka("ann", x))
tom_hobbies = run(0, x, suka("tom", x))
ellen_hobbies = run(0, x, suka("ellen", x))
eric_hobbies = run(0, x, suka("eric", x))
suka("mary",x),suka("ann ",x) 
q1 = run(0, x, membero(x, mary_hobbies), membero(x,ann_hobbies))
print("Hobi mary yang sama dengan ann adalah : ", q1)

q1 = run(0, x, membero(x, mary_hobbies), membero(x,eric_hobbies))
print("Hobi mary yang sama dengan eric adalah : ", q1)

q1 = run(0, x, membero(x, ellen_hobbies), membero(x,tom_hobbies))
print("Hobi ellen yang sama dengan tom adalah : ", q1)



# print("Tom: ", tom_hobbies)
# for hobby in tom_hobbies:
#     fact(suka, ("bill"), hobby)

# bill_hobbies = run(0, x, suka("bill", x))
# print("Bill: ", bill_hobbies)


# print("Mary: ", mary_hobbies)

# for hobby in mary_hobbies:
#     fact(suka, ("ann"), hobby)

# print("Ann: ", ann_hobbies)
