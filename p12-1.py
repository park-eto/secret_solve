#필요한 함수를 만들어보세요!
floorcount = [0, 0, 0, 0, 0]

def floorHandler(floorNum):
    if floorNum not in destinationQueue:
        goToFloor(floorNum, False)

def upHandler(floorNum):
    if floorNum not in destinationQueue:
        goToFloor(floorNum, False)
    
def downHandler(floorNum):
    if floorNum not in destinationQueue:
        goToFloor(floorNum, False)
    
def stopHandler(floorNum):
    floorcount[floorNum] = floorcount[floorNum] + 1

def passingHandler(floorNum):
    if floorNum in destinationQueue:
        destinationQueue.remove(floorNum)
        goToFloor(floorNum, True)
        
def idleHandler():
    goToFloor(0, False)
#엘리베이터의 실행코드를 작성해보세요!

on_floor_button_pressed(floorHandler)
on_up_button_pressed(upHandler)
on_down_button_pressed(downHandler)
on_stopped_at_floor(stopHandler)
on_passing_floor(passingHandler)
on_idle(idleHandler)