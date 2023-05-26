#필요한 함수를 만들어보세요!


#엘리베이터의 실행코드를 작성해보세요!
floorList=[0, 1, 2, 3, 4]

#필요한 함수를 만들어보세요!

def floorHandler(floorNum):
    if floorNum not in destinationQueue:
        goToFloor(floorNum, False)

def upHandler(floorNum):
    print(floorList[floorNum]," 층 -> 엘리베이터 점검중입니다.")
    
def downHandler(floorNum):
    print(floorList[floorNum]," 층 -> 엘리베이터 점검중입니다.")

        
#엘리베이터의 실행코드를 작성해보세요!

on_up_button_pressed(upHandler)
on_down_button_pressed(downHandler)