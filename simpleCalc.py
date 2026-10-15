# Fix applied
def operation(a,b,op):
    if op=='+':
        return a+b
    elif op=='-':
        return a-b
    elif op=='*':
        return a*b
    elif op=='/':
        return a/b
    else:
        print('Invalid operation')

a=int(input())
b=int(input())
op=input()
result=operation(a,b,op)
print(result)
