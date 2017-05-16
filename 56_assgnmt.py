
def push_stack(contents):
    
    if len(stack) >= limit:
        print 'Your Stack is Overflow'
    else:
        stack.append(contents)
    print 'Stack after Push',stack
def pop_stack():
    if len(stack) <= 0:
        print 'Stack Underflow!'
        return 0
    else:
        return stack.pop()
if __name__=="__main__":
    stack = []
    limit = input('Enter the no of elements to be stored in stack :')
    for t in range(limit):
        contents = input('Enter element '+str(t)+' :')
        push_stack(contents)
    for t in range(limit):
        print 'Popping '+str(limit-t)+'th element:',pop_stack()
        print 'Stack after Popping!',stack
		


