# Problem: Implement a 3 stack 
# Algorithm for n-stacks using dynamic arrays (list)
#   Stack: LIFO (Last In First Out)
#   pop from top and push to top
#   data = our dynamic array
#   Maintain tops array for n-number of stacks and initialize to -1
#   Maintain lengths for each stack.
# Push(stack, value)
#   Check if stack is empty if yes append to data and tops=len(data)-1
#   Increment lengths by 1
#   Insert at top
#   Increment tops for all stacks which are next in sequence
# Pop(stack)
#   Check if stack is empty if yes return -999
#   Decrement length by 1
#   Delete at top
#   Increment tops for all stacks which are next in sequence

class NStack:
    def __init__(self, n=3):
        self.data = []
        self.tops = []
        self.lengths = []
        # Initialize tops and lengths
        for i in range(n):
            self.tops.append(-1)
            self.lengths.append(0)

    def push(self, stack, value):
        # Case for stack is empty
        if self.tops[stack] == -1:
            self.data.append(value)
            self.tops[stack] = len(self.data)-1
        else:
            self.data.insert(self.tops[stack], value)
        # Increment tops for all stacks which are next in sequence
        for i in range(len(self.tops)):
            if i != stack and self.tops[i] != -1 and self.tops[i] > self.tops[stack]:
                self.tops[i] += 1
        self.lengths[stack] += 1

    def pop(self, stack):
        # Check if stack is empty
        if self.tops[stack] == -1:
            return -9999
        else:
            # save the value to return
            value = self.data[self.tops[stack]]
            # Delete element at tops of given stack
            del self.data[self.tops[stack]]
            self.lengths[stack] += -1
            # Rearrange my indeces in top
            # Stack had only one item
            if self.lengths[stack] == 0:
                self.tops[stack] = -1

            # Decrement tops of all stacks which are next in sequence
            for i in range(len(self.tops)):
                if i != stack and self.tops[i] > self.tops[stack]:
                    self.tops[i] -= 1
            return value

    def print_nstack(self):
        print("Data", self.data, "Lengths", self.lengths, "Top Indices", self.tops)
        for i in range(len(self.tops)):
            print("Stack:", i, "-->", self.data[self.tops[i]:self.tops[i]+self.lengths[i]])


def main():
    nstack = NStack(3)
    nstack.print_nstack()
    nstack.push(0, 10)
    nstack.print_nstack()
    nstack.push(1, 10)
    nstack.print_nstack()
    nstack.push(1, 20)
    nstack.print_nstack()
    nstack.push(2, 30)
    nstack.push(2, 40)
    nstack.push(2, 30)
    nstack.push(2, 40)
    nstack.print_nstack()
    print(nstack.pop(0))
    nstack.print_nstack()
    print(nstack.pop(2))
    nstack.print_nstack()
    print(nstack.pop(2))
    nstack.print_nstack()
    print(nstack.pop(0))
    nstack.print_nstack()
    print(nstack.pop(1))
    nstack.print_nstack()
    print(nstack.pop(1))
    nstack.print_nstack()
    print(nstack.pop(1))
    nstack.print_nstack()
    print(nstack.push(1,90))
    nstack.print_nstack()
if __name__=='__main__':
    main()
