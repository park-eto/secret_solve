#필요한 함수를 만들어보세요!
def upHandler(floorNum):
    if floorNum not in destinationQueue:
       goToFloor(floorNum, False)
       print(destinationQueue)
    if destinationDirection() == "up":
        destinationQueue.sort()
    elif destinationDirection() == "down":
        destinationQueue.sort(reverse=True)
        

def downHandler(floorNum):
    if floorNum not in destinationQueue:
       goToFloor(floorNum, False)
       print(destinationQueue)
    if destinationDirection() == "up":
        destinationQueue.sort()
    elif destinationDirection() == "down":
        destinationQueue.sort(reverse=True)
    
def floorHandler(floorNum):
    if destinationDirection() == "up":
        destinationQueue.sort()
    elif destinationDirection() == "down":
        destinationQueue.sort(reverse=True)
    
    if floorNum in destinationQueue:
        destinationQueue.remove(floorNum)
    goToFloor(floorNum, False)
    
# def stopHandler(floorNum):
#     print(currentFloor()," 층에서 멈춤")
        
        
def passingHandler(floorNum, direction):
    if floorNum in destinationQueue:
        destinationQueue.remove(floorNum)
        goToFloor(floorNum, True)
        print(destinationQueue)
    # if(direction=="up"):
    #     print("올라갑니다. ",currentFloor()," 층을 지나는 중")
    # else:
    #     print("내려갑니다. ",currentFloor()," 층을 지나는 중")





#엘리베이터의 실행코드를 작성해보세요!      
on_up_button_pressed(upHandler)
on_down_button_pressed(downHandler)
on_floor_button_pressed(floorHandler)
on_passing_floor(passingHandler)
#on_stopped_at_floor(stopHandler)

