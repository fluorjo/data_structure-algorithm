#스택이 비었는지 확인하는 함수

SIZE = 5
stack = [ None for _ in range(SIZE) ]
top = -1



def isStackEmpty() :
	global SIZE, stack, top
	if (top == -1) :
		return True
	else :
		return False

def pop():
	global SIZE, stack, top
	if (isStackEmpty()):
		print('스택 비었음')
		return None
	else:
		data= stack[top]
		stack[top]=None
		top -=1
		return data

def peek():
	global SIZE, stack, top
	if (isStackEmpty()):
		print('스택 비었음')
		return None
	return stack[top]

retData=[pop()]
print('추출=',retData)

print("스택이 비었는지 여부 ==>", isStackEmpty())
print('다음 나올 데이터:',peek())