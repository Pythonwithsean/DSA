q = [-1] * (20)
front = len(q) - 1
back = len(q) - 1

def enqueue(val): 
	global back
	back = (back + 1) % (len(q))
	q[back] = val
def dequeue(): 
	global front
	front = (front + 1) % (len(q))
	q[front] = -1
def peek(): 
	global front
	global back
	if front == back: 
		return "Empty"
	return q[(front + 1) % len(q)] if q[(front + 1) % len(q)] != -1 else "Empty"

enqueue(100)
enqueue(99)
enqueue(150)
dequeue()
dequeue()
dequeue()
print(peek())
