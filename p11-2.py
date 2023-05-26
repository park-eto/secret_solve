#필요한 함수를 만들어보세요!
countToZero = [0, 0, 0, 0]

def floorHandler(floorNum):
    if(currentFloor()==0):
        countToZero[floorNum-1] = countToZero[floorNum-1] + 1
    
    if floorNum not in destinationQueue:
        goToFloor(floorNum, False)

def upHandler(floorNum):
    if floorNum not in destinationQueue:
        goToFloor(floorNum, False)
    
def downHandler(floorNum):
    if floorNum not in destinationQueue:
        goToFloor(floorNum, False)

def passingHandler(floorNum):
    if floorNum in destinationQueue:
        destinationQueue.remove(floorNum)
        goToFloor(floorNum, True)
        
def idleHandler():
    if(currentFloor() != 0):
        mx = countToZero.index(max(countToZero)) + 1
        print("0 층에서 ",mx," 층으로 ", countToZero[mx-1]," 번 이동했습니다.")
        goToFloor(mx, False)
#엘리베이터의 실행코드를 작성해보세요!

on_floor_button_pressed(floorHandler)
on_up_button_pressed(upHandler)
on_down_button_pressed(downHandler)
on_passing_floor(passingHandler)
on_idle(idleHandler)