from stack import Stack

def balanced_checker(brackets):
    s = Stack()
    balanced = True
    for i in brackets:
        if i in ['{', '[', '(']:
            s.push(i)
        elif i in ['}', ']', ')']:
            if s.isEmpty():
                balanced = False
            else:    
                symbol = s.pop()
                if not ((symbol == '{' and i == '}')
                    or (symbol == '[' and i == ']')
                    or (symbol == '(' and i == ')')):
                    balanced = False

    if balanced and s.isEmpty():
        return 'Сбалансированно'
    else:
        return 'Несбалансированно'

# print(balanced_checker('(((([{}]))))'))
# print(balanced_checker('[([])((([[[]]])))]{()}'))
# print(balanced_checker('{{[()]}}'))
# print(balanced_checker('}{}'))
# print(balanced_checker('{{[(])]}}'))
# print(balanced_checker('[[{())}]'))