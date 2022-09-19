@@ -5,12 +5,14 @@ class Evaluate:
       size_of_stack: An integer which represents the size of stack.
       stack: A List which acts as a Stack.
   """

     # Write your code here

   def __init__(self, size):
     """Inits Evaluate with top, size_of_stack and stack.
     Arguments:
       size_of_stack: An integer to set the size of stack.
       top:An integer which points to the top most element in the stack.
       size_of_stack: An integer which represents size of stack.
       stack: A list which maintians the elements of stack.
     """
     self.top = -1
     self.size_of_stack = size
 @@ -23,10 +25,11 @@ def isEmpty(self):
     Returns:
       True if it is empty, else returns False.
     """
       if self.top == -1:
       				return True
    			else:
       				return False
     # Write your code here
     if self.top == -1:
       return True
     else:
       return False


   def pop(self):
 @@ -35,9 +38,9 @@ def pop(self):
     Returns:
       The data which is popped out if the stack is not empty.
     """
     # Write your code here
     if not self.isEmpty():
       				self.stack.pop()

       self.stack.pop()


   def push(self, operand):
 @@ -46,10 +49,9 @@ def push(self, operand):
     Arguments:
       operand: The operand to be pushed.
     """
     # Write your code here
     if self.top != self.size_of_stack - 1:
       				self.stack.append(operand)


       self.stack.append(operand)


   def validate_postfix_expression(self, expression):
 @@ -60,19 +62,18 @@ def validate_postfix_expression(self, expression):
     Returns:
       True if the expression is valid, else returns False.
     """
     # Write your code here
     a = 0
     b = 0
     	for element in expression:
      	if element.isnumeric():
         a= a + 1
     for element in expression:
       if element.isnumeric():
         a = a + 1
       else:
         b = b + 1
       if b == a - 1:
       	return True
     	else:
       	return False


     if b == a - 1:
       return True
     else:
       return False


   def evaluate_postfix_expression(self, expression):
 @@ -83,30 +84,28 @@ def evaluate_postfix_expression(self, expression):
     Returns:
       The result of evaluated postfix expression.
     """
     # Write your code here
     stack = []
     			for i in expression:
       				if i.isnumeric():
         					stack.append(int(i))
       				if len(stack) >= 2:
         					if i == '+':
           						stack[-2] = stack[-2] + stack[-1]
           						stack.pop()
         					elif i == '-':
           						stack[-2] = stack[-2] - stack[-1]
           						stack.pop()
         					elif i == '*':
           						stack[-2] = stack[-2] * stack[-1]
           						stack.pop()
                   elif i == '/':
           						stack[-2] = stack[-2] / stack[-1]
           						stack.pop()
         					elif i == '^':
           						stack[-2] = stack[-2] ^ stack[-1]
           						stack.pop()
     			return int(stack[-1])



     for i in expression:
       if i.isnumeric():
         stack.append(int(i))
       if len(stack) >= 2:
         if i == '+':
           stack[-2] = stack[-2] + stack[-1]
           stack.pop()
         elif i == '-':
           stack[-2] = stack[-2] - stack[-1]
           stack.pop()
         elif i == '*':
           stack[-2] = stack[-2] * stack[-1]
           stack.pop()
         elif i == '/':
           stack[-2] = stack[-2] / stack[-1]
           stack.pop()
         elif i == '^':
           stack[-2] = stack[-2] ^ stack[-1]
           stack.pop()
     return int(stack[-1])


 # Do not change the following code
