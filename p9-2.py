#필요한 함수를 만들어보세요!
def upHandler(floorNum):
    if floorNum not in destinationQueue:
       goToFloor(floorNum, False)
        

def downHandler(floorNum):
    if floorNum not in destinationQueue:
       goToFloor(floorNum, False)
        
    
def floorHandler(floorNum):
    goToFloor(floorNum, False)
    if(currentFloor()==0):
        destinationQueue.sort()
    else:
        destinationQueue.sort(reverse=True)

#엘리베이터의 실행코드를 작성해보세요!      
on_up_button_pressed(upHandler)
on_down_button_pressed(downHandler)
on_floor_button_pressed(floorHandler)