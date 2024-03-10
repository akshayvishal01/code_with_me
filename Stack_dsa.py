#This python program demonstrates implementation of stack a

#stack can be implemented using array and also using list *_*

#syntax for creating stack in python
def create_stack():
    stack = []
    return stack

#creating a empty stack
def empty_stack(stack):
    #stack=[]
    return len(stack) == 0

#adding item into stack

def push(stack,item):
    stack.append(item)
    print("Element pushed into stack : "+ item)

#Removing element from stack
def pop(stack):
    if (empty_stack(stack)):
        return "Stack is empty : "
    
    return stack.pop()

stack = create_stack()
push(stack, str(1))
push(stack, str(2))
push(stack, str(3))
push(stack, str(4))
push(stack, str(5))

print("Element popped item : "+pop(stack))
print("Stack items after popping : " + str(stack))

#Time complexity of stack using arrays is O(1) which is constant