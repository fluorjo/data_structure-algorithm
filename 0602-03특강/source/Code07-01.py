#함수


#전역
SIZE=5
queue = [None for _ in range(SIZE)]

front = rear = -1
#'front 값과 rear의 값이 같을 때' 큐는 비어있다.

#메인

#enqueue()
rear += 1
queue[rear] = "화사"
rear += 1
queue[rear] = "솔라"
rear += 1
queue[rear] = "문별"

print("----- 큐 상태 -----")
print ( '[출구] <-- ', end='')




for i in range(0, len(queue), 1) :
	print(queue[i], end=' ')
print ( '<-- [입구] ')


#dequeue()
front+=1
data=queue[front]
queue[front] = None
print('손님:',data)