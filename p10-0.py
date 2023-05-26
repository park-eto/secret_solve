#필요한 함수를 만들어보세요!
def floorHandler(floorNum):
    goToFloor(floorNum, False)

def downHandler(floorNum):
    goToFloor(floorNum, False)

def upHandler(floorNum):
    goToFloor(floorNum, False)

def stopHandler(floorNum):
    if(floorNum==0):
        destinationQueue.sort()
    elif(floorNum==4):
        goToFloor(0, True)

#엘리베이터의 실행코드를 작성해보세요!
on_floor_button_pressed(floorHandler)
on_up_button_pressed(upHandler)
on_down_button_pressed(downHandler)
on_stopped_at_floor(stopHandler)