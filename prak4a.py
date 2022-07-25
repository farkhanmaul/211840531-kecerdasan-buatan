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
    A, B = map(Expr, 'AB')
    model = {A: False, B: True}

    # a.	Query 1 : not ( A and B) 
    query1 = ~(A & B)
    print(query1 , ' \t\t: ' , is_true(query1, model))
    
    # b.	Query 2 : not ( A and B) or not (A or B) 
    query2 = (~ (A & B) | (~(A | B)))
    print(query2 , ' \t: ' , is_true(query2, model))
    
    # c.	Query 3 : not ( A or B) and not ( A and B) 
    query3 = (~ (A | B) & (~(A & B)))
    print(query3 , ' \t: ' , is_true(query3, model))
    
    # d.	Query 4: not (A or B) and not (B) 
    query4 = (~ (A | B) & (~ B))
    print(query4 , ' \t: ' , is_true(query4, model))
    

    # 1.	Query 1 : not ( A and B) 
    query1 = ~(A & (A | B))
    print(query1 , ' \t: ' , is_true(query1, model))
    
    # 2.	Query 2 : not ( A and B) or not (A or B) 
    query2 = ~ (A & (A & B))
    print(query2 , ' \t: ' , is_true(query2, model))
    
    # 3.	Query 3 : not ( A or B) and not ( A and B) 
    query3 = ~ (A | B)
    print(query3 , '\t\t: ' , is_true(query3, model))