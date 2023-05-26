#필요한 함수를 만들어보세요!
def floorHandler(floorNum):
    if floorNum not in destinationQueue:
        goToFloor(floorNum, False)

def upHandler(floorNum):
    if floorNum not in destinationQueue:
        goToFloor(floorNum, False)

def downHandler(floorNum):
    if floorNum not in destinationQueue:
        goToFloor(floorNum, False)

def passingHandler(floorNum, direction):
    if floorNum in destinationQueue:
        destinationQueue.remove(floorNum)
        goToFloor(floorNum, True)
        

#엘리베이터의 실행코드를 작성해보세요!
on_up_button_pressed(upHandler)
on_down_button_pressed(downHandler)
on_floor_button_pressed(floorHandler)
on_passing_floor(passingHandler)