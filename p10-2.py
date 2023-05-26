#필요한 함수를 만들어보세요!
count = 0

def floorHandler(floorNum):
    if(floorNum==2):
        count += 1
    goToFloor(floorNum, False)

def upHandler(floorNum):
    goToFloor(floorNum, False)

def downHandler(floorNum):
    goToFloor(floorNum, False)

def idleHandler():
    if(count >= 3):
        goToFloor(2, False)
    else:
        goToFloor(0, False)

#엘리베이터의 실행코드를 작성해보세요!
on_idle(idleHandler)
on_up_button_pressed(upHandler)
on_down_button_pressed(downHandler)
on_floor_button_pressed(floorHandler)