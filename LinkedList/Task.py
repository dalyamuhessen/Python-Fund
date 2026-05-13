from collections import deque, Counter
# 1. Reverse a String Using a Stack
# 2. For each temperature find how many days until a warmer temperature.
# ex: [22, 18, 28, 32, 25, 20, 23]
# out: [2, 1, 1, 0, 0, 1, 0]
# 3. First Non-Repeating Character in a Stream. As characters arrive return the first non-repeating one.

class Stack:
    def __init__(self):
        self.arr = []
    def push(self, item):
        self.arr.append(item)
    def pop(self):
        if len(self.arr)>0:
            self.arr.pop()
    def peek(self):
        if len(self.arr)>0:
            return self.arr[-1]
    def empty(self):
        return (len(self.arr)==0)  
def reverse(str):
	results=""
	st=Stack();
	for i in str:
		st.push(i)
	while(st.peek()):
		results+=st.peek()
		st.pop()
	return results
str="abcdefg"
print(str)
print(reverse(str))
def warmertemp(arr):
    st=Stack()
    res= (len(arr))*[0]
    for n in range(len(arr)):
     while( st.peek()!=None and arr[n] > arr[st.peek()] ):
       res[st.peek()]=(n-st.peek())
       st.pop()
     st.push(n) 
    return res
print(warmertemp([22, 18, 28, 32, 25, 20, 23]))
def first_non_repeating(stream):
    queue = deque()  #  holds candidates in arrival order
    freq = Counter() # tracks frequency of every character seen
    for char in stream:
        freq[char] += 1
        queue.append(char)
        while queue and freq[queue[0]] > 1:
            queue.popleft()
        result = queue[0] if queue else -1
        print(f"Stream: ...{char}  =>  First non-repeating: {result}")

first_non_repeating("aacbbac")