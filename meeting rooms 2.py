#Space: O(No. of meeting rooms)
#time: O ( No. of meetings)
import heapq
def sol(meetings):
    if len(meetings) ==0:
        print('no. of rooms is', 0)
        return
    if len(meetings) == 1:
        print('no. of rooms is', 1)
        return
    heap = list()
    meetings= sorted(meetings, key=lambda meetings: meetings[0])
    heap = [meetings[0][1]]
    
    for i in range(1,len(meetings)):
        start= meetings[i][0]
        end=meetings[i][1]
        if start >= heap[0]:
            heapq.heappushpop(heap, end)
        else:
            heapq.heappush(heap,end)
    print('heap is', heap)
    print('no. of rooms is', len(heap))
    return 

print('test case 1')
sol([[0,30],[5,10],[15,20]])
print('test case 2')
sol([[0,30],[5,10],[15,20],[21,25]])
print('test case 3')
sol([[5,10]])
print('test case 4')
sol([])
print('test case 5')
sol([[0,30],[25,35],[30,35],[5,10],[15,20],[21,25]])
        
        
    
        
