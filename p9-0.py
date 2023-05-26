#필요한 함수를 만들어보세요!
def optiQueue():
    if destinationDirection() == "up":
        destinationQueue.sort()
    elif destinationDirection() == "down":
        destinationQueue.sort(reverse=True)

def upHandler(floorNum):
    if(floorNum%2==1 or floorNum==0):
        if floorNum not in destinationQueue:
          goToFloor(floorNum, False)
        optiQueue()
        

def downHandler(floorNum):
    if(floorNum%2==1 or floorNum==0):
        if floorNum not in destinationQueue:
          goToFloor(floorNum, False)
          print(destinationQueue)
        optiQueue()
    
def floorHandler(floorNum):
    print(floorNum)
    if(floorNum%2==1 or floorNum==0):
        optiQueue()
        if floorNum in destinationQueue:
            destinationQueue.remove(floorNum)
        goToFloor(floorNum, False)
    
    
    
# def stopHandler(floorNum):
#     print(currentFloor()," 층에서 멈춤")
        
        
# def passingHandler(floorNum, direction):
#     if (floorNum%2==0)
        #무시하고 지나가기
        






#엘리베이터의 실행코드를 작성해보세요!      
on_up_button_pressed(upHandler)
on_down_button_pressed(downHandler)
on_floor_button_pressed(floorHandler)
#on_passing_floor(passingHandler)
#on_stopped_at_floor(stopHandler)

