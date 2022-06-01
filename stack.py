#Implementation of a stack in python
#Operations ==> Push(), pop (), empty(), size (), top(),


#Creating a stack.
def create_stack ():
    stack = []
    return stack

#Checking for empty
def check_empty(stack):
    stack_length = len(stack)
    return stack_length == 0

# Pushing an item to a stack.
def push (stack, item):
    stack.append(item)
    print("Pushed Item: " + item)

#Popping out an item from a stack.
def pop (stack):
    if (check_empty(stack)):
        return "Sorry, the stack is already empty."

    return stack.pop()


stack = create_stack()
name1 = input("Enter name-1 to stack: \n")
push(stack, name1)
print("Stack status: \n" + str(stack))
name2 = input("Enter name-2 to stack: \n")
push(stack, name2)
print("Stack status: \n" + str(stack))
name3 = input("Enter name-3 to stack: \n")
push(stack, name3)
print("Stack status: \n" + str(stack))

#pop(stack)
print("Popped item: " + pop(stack))
print("Popped item: " + pop(stack))
print("Stack after popping an element: \n" + str(stack))

