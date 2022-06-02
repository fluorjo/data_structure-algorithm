#스택이 꽉 찼는지 확인하는 함수
def isStackFull() :
	global SIZE, stack, top
	if (top >= SIZE-1) :
		return True
	else :
		return False
def push(data) :
	global SIZE, stack, top

	if (isStackFull() == True):
		print('스택 꽉')
		return  #아무것도 하지 마라
	else:
		top+=1
		stack[top]=data


SIZE=5
stack=[None for _ in range(SIZE)]
top = -1

push('커피')
push('녹차')
push('꿀물')
push('콜라')
push('환타')

print(stack)

push('사이다')
print(stack)
