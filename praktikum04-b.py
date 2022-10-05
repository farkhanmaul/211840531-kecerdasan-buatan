from ai_pkg.utils import Expr

def is_prop_symbol(s):
    return isinstance(s, str) and s[:1].isalpha() and s[0].isupper()

def is_true(exp, model={}):
    if exp in (True, False):
        return exp
    op, args = exp.op, exp.args
    if is_prop_symbol(op):
        return model.get(exp)
    elif op == '~':
        p = is_true(args[0], model)
        if p is None:
            return None
        else:
            return not p
    elif op == '|':
        result = False
        for arg in args:
            p = is_true(arg, model)
            if p is True:
                return True
            if p is None:
                result = None
        return result
    elif op == '&':
        result = True
        for arg in args:
            p = is_true(arg, model)
            if p is False:
                return False
            if p is None:
                result = None
        return result
    p, q = args
    if op == '==>':
        return is_true(~p | q, model)
    elif op == '<==':
        return is_true(p | ~q, model)
    pt = is_true(p, model)
    if pt is None:
        return None
    qt = is_true(q, model)
    if qt is None:
        return None
    if op == '<=>':
        return pt == qt
    elif op == '^':
        return pt != qt
    else:
        raise ValueError("illegal operator" + str(exp))

if __name__=='__main__':
    A, B, C, D = map(Expr, 'ABCD')
    model = {A: False, B: True, C: False, D: True}

# Query 1 : (A or B) and (C or D) 
    query1 = (A | B) & (C | D)
    print(query1 , ' \t\t: ' , is_true(query1, model))

# Query 2 : (A and B) and (C or D) 
    query2 = (A & B) & (C | D)
    print(query2 , ' \t\t: ' , is_true(query2, model))

# Query 3 : not (A or B) and (C or D) 
    query3 = ~(A | B) & (C | D)
    print(query3 , ' \t\t: ' , is_true(query3, model))

# Query 4 : (A and B) and (not (C or D)) 
    query4 = (A & B) & (~(C | D))
    print(query4 , ' \t\t: ' , is_true(query4, model))

# Query 5 : (A or B) or (C and D) 
    query5 = (A | B) | (C & D)
    print(query5 , ' \t\t: ' , is_true(query5, model))
