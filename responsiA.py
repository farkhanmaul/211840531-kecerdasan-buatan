from kanren.facts import Relation, facts
from kanren.core import var, run

ortu = Relation()
facts(ortu, ("Didi", "Dika"),
                ("Dika", "Dinda"),
                ("Didi", "Darmo"),
                ("Dika", "Kiko"),
                ("Dika", "Dinda"),
                ("Dani", "Hendi"),
                ("Dani", "Dina"),
                ("Dani", "Dini"),
                ("Darmo", "Darto"))

paman = Relation()
facts(paman, ("Dika", "Hendi"),
                ("Dika", "Dina"),
                ("Dika", "Dini"),
                ("Dika", "Darto"),
                ("Dani", "Kiko"),
                ("Dani", "Dinda"),
                ("Dani", "Darto"),
                ("Darmo", "Kiko"),
                ("Darmo", "Dinda"),
                ("Darmo", "Hendi"),
                ("Darmo", "Dina"),
                ("Darmo", "Dini"))
                
saudara = Relation()
facts(saudara, ("Kiko", "Dinda"),
                ("Dinda", "Kiko"),
                ("Hendi", "Dina"),
                ("Hendi", "Dini"),
                ("Dina", "Hendi"),
                ("Dina", "Dini"),
                ("Dini", "Dinda"),
                ("Dini", "Dina"),
                ("Dika", "Dani"),
                ("Dika", "Darmo"),
                ("Dani", "Dika"),
                ("Dani", "Darmo"),
                ("Darmo", "Dika"),
                ("Darmo", "Dani"))

x = var()
child = "Darto"
ayah = run(1, x, ortu(x, child))
print("\nNama ayah " + child + ": ")
for item in ayah:
    print(item)

x = var()
saudara1 = "Dinda"
sdr = run(1, x, saudara(x, saudara1))
print("\nNama ayah " + saudara1 + ": ")
for item in sdr:
    print(item)

x = var()
saudara1 = "Dinda"
sdr = run(1, x, saudara(x, saudara1))
print("\nNama ayah " + saudara1 + ": ")
for item in sdr:
    print(item)
