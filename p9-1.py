#필요한 함수를 만들어보세요!
def upHandler(floorNum):
    if(floorNum%2==1):
        goToFloor(floorNum,True)
    else:
        goToFloor(floorNum,False)
        

def downHandler(floorNum):
    if(floorNum%2==1):
        goToFloor(floorNum,True)
    else:
        goToFloor(floorNum,False)    
        
    
def floorHandler(floorNum):
    if(currentFloor()%2==1):
        goToFloor(floorNum,True)
    elif(floorNum%2==1):
        goToFloor(floorNum,True)
    else:
        goToFloor(floorNum,False)
    

#엘리베이터의 실행코드를 작성해보세요!      
on_up_button_pressed(upHandler)
on_down_button_pressed(downHandler)
on_floor_button_pressed(floorHandler)


