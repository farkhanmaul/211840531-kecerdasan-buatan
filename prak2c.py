from kanren.facts import Relation, facts, fact
from kanren.core import var, run
from kanren.goals import membero
from kanren import vars

ukuran = Relation()
warna = Relation()
gelap = Relation()
jenis = Relation()
facts(ukuran,   ("beruang", "besar"),
                ("gajah", "besar"),
                ("kucing", "kecil"))
facts(warna,    ("beruang", "cokelat"),
                ("kucing", "hitam"),
                ("gajah", "kelabu"))
fact            (gelap, "hitam")
fact            (gelap, "cokelat")

facts(jenis,    ("beruang", "karnivora"),
                ("kucing", "karnivora"))
z = var()
kecil = run(0, z, ukuran(z, "kecil"))
print("hewan berukuran kecil: ", kecil)

besar = run(0, z, ukuran(z, "besar"))
print("hewan berukuran besar: ", besar)

cokelat = run(0, z, warna(z, "cokelat"))
print("hewan berwarna cokelat : ", cokelat)

gelap = run(0, z, gelap(z, "gelap"))
print("hewan berwarna gelap : ", gelap)

karnivora = run(0, z, jenis(z, "karnivora"))
print("Hewan karnivora: ", karnivora)