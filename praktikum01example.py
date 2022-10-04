# Family relationships from The Godfather
# Translated from the core.logic example found in
# "The Magical Island of Kanren - core.logic Intro Part 1"
# http://objectcommando.com/blog/2011/11/04/the-magical-island-of-kanren-core-logic-intro-part-1/

from kanren import Relation, facts, run, conde, var, eq

father = Relation()
mother = Relation()

facts(father, ('Vito', 'Michael'),
              ('Vito', 'Sonny'),
              ('Vito', 'Fredo'),
              ('Michael', 'Anthony'),
              ('Michael', 'Mary'),
              ('Sonny', 'Vicent'),
              ('Sonny', 'Francesca'),
              ('Sonny', 'Kathryn'),
              ('Sonny', 'Frank'),
              ('Sonny', 'Santino'))

facts(mother, ('Carmela', 'Michael'),
              ('Carmela', 'Sonny'),
              ('Carmela', 'Fredo'),
              ('Kay', 'Mary'),
              ('Kay', 'Anthony'),
              ('Sandra', 'Francesca'),
              ('Sandra', 'Kathryn'),
              ('Sandra', 'Frank'),
              ('Sandra', 'Santino'))

q = var()
ayahvito = run(0, q, father('Vito', q))
print (ayahvito)          # Vito is the father of who?
# ('Sonny', 'Michael', 'Fredo')
