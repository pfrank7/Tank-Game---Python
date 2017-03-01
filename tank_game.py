# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 09:02:38 2016

@author: paigefrank,quinnsalditch,carissazukowski
"""


from graphics import *
from random import *
from math import *

def RandomInitialPosition(): 
    #returns starting position of each tank
    x=randrange(100,600)
    return x

def movetank(tank_pos,direction,win2): 
    #moves tank left or right if user chooses (50m)
    direct=direction
    if direct==-1:
        if tank_pos - 50 <0:
            Text(Point(50,90),"Error, stop running away from battle!").draw(win2)
        else:
            tank_pos=tank_pos-50
    else:
        if tank_pos + 50>1000:
            Text(Point(50,90),"Error, stop running away from battle!").draw(win2)
        else:
            tank_pos=tank_pos+50
    return tank_pos
    
def checkshot(shot_pos,opp_pos,tank): 
    #does the ball hit the opponent
    #create a range of tank of 20 m so 10 above 10 below
    tank_boxUP=opp_pos+10
    tank_boxLW=opp_pos-10
    if shot_pos>tank_boxUP or shot_pos<tank_boxLW:
        tank=1
    else:
        tank=0
    return tank
    #returns if tank was hit

def printStat(tank1,tank2):
    if tank1:
        text1="Tank 1 is alive"
    else:
        text1="Tank 1 is dead"
    
    if tank2:
        text2="Tank 2 is alive"
    else:
        text2="Tank 2 is dead"
    
    return text1, text2

def randomwind():
    #creates a random horizontal wind acceleration
    #does not allove for no wind (ie. 0m/s/s)
    #range is -5,5
    val=randrange(0,1)
    if val:
        wind=randrange(-5,-1)
    else:
        wind=randrange(1,5)
    return wind
   
def fireshot(ang, vel, opp_pos, play_pos,wind,win,Lbutt): 
    #shoots the cannon
    xpos,ypos,xvel,yvel=initializeShot(ang,vel,play_pos)
    hit_pos=shotTravel(xvel,yvel,ypos,xpos,wind,Lbutt)
    shotgraphics(play_pos,xvel,yvel,wind,win,Lbutt)
    return hit_pos
    

def initializeShot(ang, vel,play_pos):
    #converts input to be used to calc. projectile
    theta = radians(ang)
    xvel = vel * cos(theta)
    yvel = abs(vel) * sin(theta)
    ypos=0
    xpos=play_pos
    return xpos, ypos,xvel,yvel
    
def shotTravel(xvel, yvel, ypos, xpos,wind,Lbutt): 
    #tracks projectile motion using while loop and incrementing time
    increment=.1
    time=increment
    while ypos>=0:
        velocitylong=(sqrt((xvel**2) + (yvel**2)))
        velocity = int(velocitylong)
        #accounts for air resistance by calculating x acceleration
        axwind=wind*time
        axair=(-.002)*xvel*velocity
        ax=axair+axwind
        xvel1=xvel + ax
        #accounts for air resistance by totaling y acceleration
        ayball=-9.8*time
        ayair=(-.002)*yvel*velocity
        ay=ayball+ayair
        yvel1 = yvel + ay
        #updates position
        xpos = xpos + ((time * (xvel + xvel1)/2.0 )*Lbutt)
        ypos = ypos + (time * (yvel + yvel1) / 2.0 ) 
        yvel = yvel1
        xvel=xvel1
    return xpos

def shotgraphics(xpos,xvel,yvel,wind,win,Lbutt):
    #uses same eq as shottravel to print graphis of projectile
    #leaves projectile on the screen to track previous shots
    y0=0
    x0=xpos
    vx,vy=xvel,yvel
    dt=.1
    p=Point(x0,y0)
    ball=Circle(p,5)
    ball.setFill("black")
    ball.draw(win)
    while y0>=0 and x0>=0 and x0<=1000:
        vellong=(sqrt((vx**2)+(vy**2)))
        vel = int(vellong)
        axair=-.002*vy*vel
        axwind=wind*dt
        ayair=-.002*vx*vel
        ayball=-9.8*dt
        ax=axair+axwind
        ay=ayair+ayball
        vx1=vx+ax
        vy1=vy+ay
        x=x0+((vx+vx1)/2)*dt
        y=y0+((vy+vy1)/2)*dt
        ball.move((x-x0)*Lbutt,y-y0)
        x0=x
        y0=y
        vx=vx1
        vy=vy1
    
def windgraphics(wind,win):
    #arrow denoting wind acceleration
    #arrow head flips to show direction
    Text(Point(500,465),"Wind").draw(win)
    pl=Point(450,440)
    pu=Point(550,460)
    rect=Rectangle(pl,pu)
    rect.setFill("grey")
    rect.draw(win)
    windacc=str(wind)
    Text(Point(500,450),windacc+' m/s/s').draw(win)
    if wind<0: #draw triangle)
        p1=Point(400,450)
        p2=Point(450,420)
        p3=Point(450,480)     
        tri=Polygon(p1,p2,p3)
        tri.draw(win)
        tri.setFill("grey")    
    elif wind>0:
        p1=Point(600,450)
        p2=Point(550,420)
        p3=Point(550,480)
        tri=Polygon(p1,p2,p3)
        tri.draw(win)
        tri.setFill("grey")  
    else:
        p1=Point(600,450)
        p2=Point(550,420)
        p3=Point(550,480)
        tri.draw(win)
        tri.setFill("white")
        tri.setOutline('white')
    return tri
    
def tankGraphics1 (tank1_pos,tank1,win): 
    #graphics for tank 1
    #player 1 is BLUE
    tank1L=tank1_pos-10
    tank1R=tank1_pos+10
    y1=0
    y2=20
    tank1shape=Rectangle(Point(tank1L,y1),Point(tank1R,y2))
    tank1shape.setFill('blue')
    tank1shape.draw(win)
    return tank1shape
    
def tankGraphics2 (tank2_pos,tank2,win):
    #graphics for tank 2
    #player 2 is RED
    tank2L=tank2_pos-10
    tank2R=tank2_pos+10
    y1=0
    y2=20
    tank2shape=Rectangle(Point(tank2L,y1),Point(tank2R,y2))
    tank2shape.setFill('red')
    tank2shape.draw(win)
    return tank2shape
    
def buttongraphicsPlayer1(start,width,height,label,win):
    #graphics for buttons
    bottomcornerY=start.getY()-height/2
    bottomcornerX=start.getX()
    topcornerY=start.getY()+height/2
    topcornerX=start.getX()+width
    button=Rectangle(Point(bottomcornerX,bottomcornerY),Point(topcornerX,topcornerY))
    button.draw(win)
    button.setFill("blue")
    textpointX=start.getX()+width/2
    textpointY=start.getY()
    message=Text(Point(textpointX,textpointY),label)
    message.setTextColor('white')
    message.draw(win)
    return bottomcornerX,topcornerX,bottomcornerY,topcornerY

def buttongraphicsPlayer2(start,width,height,label,win):
    #graphics for buttons
    bottomcornerY=start.getY()-height/2
    bottomcornerX=start.getX()
    topcornerY=start.getY()+height/2
    topcornerX=start.getX()+width
    button=Rectangle(Point(bottomcornerX,bottomcornerY),Point(topcornerX,topcornerY))
    button.draw(win)
    button.setFill("red")
    textpointX=start.getX()+width/2
    textpointY=start.getY()
    message=Text(Point(textpointX,textpointY),label)
    message.setTextColor('white')
    message.draw(win)
    return bottomcornerX,topcornerX,bottomcornerY,topcornerY
    
def buttonclick(BX1,TX1,BY1,TY1,BX2,TX2,BY2,TY2,win):
    #returns which button is clicked
    buttonvalue=0
    while buttonvalue==0:
        dot=win.getMouse()
        if dot.getX()>=BX1 and dot.getX()<=TX1 and dot.getY()>=BY1 and dot.getY()<=TY1:
            buttonvalue=-1
        elif dot.getX()>=BX2 and dot.getX()<=TX2 and dot.getY()>=BY2 and dot.getY()<=TY2:
            buttonvalue=1
    return buttonvalue
    

def choicePlayer1(tank1_pos,tank2_pos,wind,win,tank1,tank2,tankG1,win2):
    #controls Player 1's round
    #make shoot button (returns corner coordinates)
    ShootBx,ShootTx,ShootBy,ShootTy=buttongraphicsPlayer1(Point(20,470),40,30,"Shoot",win) 
    #make move button (returns corner coordinates)
    MoveBx,MoveTx,MoveBy,MoveTy=buttongraphicsPlayer1(Point(20,420),40,30,"Move",win)
    #eval. if shoot or move was clicked
    #shoot = -1 so player shoots
    #shoot = 1 so player moves    
    shoot=buttonclick(ShootBx,ShootTx,ShootBy,ShootTy,MoveBx,MoveTx,MoveBy,MoveTy,win)
    if shoot==-1:
        #draws L button(returns corner coordinates)
        LbuttBX,LbuttTX,LbuttBY,LbuttTY=buttongraphicsPlayer1(Point(80,470),40,30,"Left",win)
        #draws R button (returns corner coordinates)
        RbuttBX,RbuttTX,RbuttBY,RbuttTY=buttongraphicsPlayer1(Point(80,420),40,30,"Right",win) 
        #Lbutt returns 1 or -1 for direction control
        Lbutt=buttonclick(LbuttBX,LbuttTX,LbuttBY,LbuttTY,RbuttBX,RbuttTX,RbuttBY,RbuttTY,win)
        velbox=Entry(Point(160,470),5)
        velbox.setText("Vel")
        velbox.draw(win)
        angbox=Entry(Point(160,420),5)
        angbox.setText("Ang")
        angbox.draw(win)
        win.getMouse() #waits for click to eval
        ang=eval(angbox.getText())
        vel=eval(velbox.getText())
        #calls fireshot to shoot the cannon ball and calculate its final position
        shot_pos=fireshot(ang,vel,tank2_pos,tank1_pos,wind,win,Lbutt)
        tank2=checkshot(shot_pos,tank2_pos,tank2)
        tank1_pos=tank1_pos
        tankG1=tankG1
        #if player chooses to move
    elif shoot == 1:
        LbuttBX,LbuttTX,LbuttBY,LbuttTY=buttongraphicsPlayer1(Point(80,470),40,30,"Left",win)
        RbuttBX,RbuttTX,RbuttBY,RbuttTY=buttongraphicsPlayer1(Point(80,420),40,30,"Right",win)#make L button
        Lbutt=buttonclick(LbuttBX,LbuttTX,LbuttBY,LbuttTY,RbuttBX,RbuttTX,RbuttBY,RbuttTY,win)
        tank1_pos=movetank(tank1_pos,Lbutt,win2)
        #moves tank 50m in direction indicated (Lbutt indicates direction)
        tankG1.move(50*Lbutt,0)
        tank2=tank2
        shot_pos=0
        
    return tank1_pos,tank2,tankG1,shot_pos
    
def choicePlayer2(tank2_pos,tank1_pos,wind,win,tank1,tank2,tankG2,win2):
    #same function as above but controls player 2's move
    ShootBx,ShootTx,ShootBy,ShootTy=buttongraphicsPlayer2(Point(20,470),40,30,"Shoot",win)#make shoot button
    MoveBx,MoveTx,MoveBy,MoveTy=buttongraphicsPlayer2(Point(20,420),40,30,"Move",win)#make move button
    shoot=buttonclick(ShootBx,ShootTx,ShootBy,ShootTy,MoveBx,MoveTx,MoveBy,MoveTy,win)
    if shoot==-1:
        LbuttBX,LbuttTX,LbuttBY,LbuttTY=buttongraphicsPlayer2(Point(80,470),40,30,"Left",win)
        RbuttBX,RbuttTX,RbuttBY,RbuttTY=buttongraphicsPlayer2(Point(80,420),40,30,"Right",win) #make L button
        Lbutt=buttonclick(LbuttBX,LbuttTX,LbuttBY,LbuttTY,RbuttBX,RbuttTX,RbuttBY,RbuttTY,win)
        vel=Entry(Point(160,470),5)
        vel.setText("Vel")
        vel.draw(win)
        ang=Entry(Point(160,420),5)
        ang.setText("Ang")
        ang.draw(win)
        win.getMouse() #need to make an okay button
        ang=eval(ang.getText())
        vel=eval(vel.getText())
        if vel>100:
            vel=100
        else:
            vel=vel
        shot_pos=fireshot(ang,vel,tank1_pos,tank2_pos,wind,win,Lbutt)
        tank1=checkshot(shot_pos,tank1_pos,tank1)
        tank2_pos=tank2_pos
        tankG2=tankG2
    elif shoot == 1:
        LbuttBX,LbuttTX,LbuttBY,LbuttTY=buttongraphicsPlayer2(Point(80,470),40,30,"Left",win)
        RbuttBX,RbuttTX,RbuttBY,RbuttTY=buttongraphicsPlayer2(Point(80,420),40,30,"Right",win) #make L button
        Lbutt=buttonclick(LbuttBX,LbuttTX,LbuttBY,LbuttTY,RbuttBX,RbuttTX,RbuttBY,RbuttTY,win)
        tank2_pos=movetank(tank2_pos,Lbutt,win2)
        tankG2.move((50*Lbutt),0)
        tank1=tank1
        shot_pos=0

        
    return tank2_pos,tank1,tankG2,shot_pos
    

def main(): 
    #sets graphic window for the tanks and buttons
    win=GraphWin("Tank Game",700,350)
    win.setCoords(0,0,700,500)
    #sets graphic window for all output
    win2=GraphWin("Game Stats",300,300)
    win2.setCoords(0,0,100,100)
    #comments all information for the window
    message1=Text(Point(600,400),'Player 1 is Blue')
    message1.setTextColor('blue')
    message1.setSize(20)
    message1.draw(win)
    message2=Text(Point(600,370),'Player 2 is Red')
    message2.setTextColor('red')
    message2.setSize(20)
    message2.draw(win)
    message3=Text(Point(400,350),"DO NOT EXCEED 100m/s.")
    message3.setSize(20)
    message3.draw(win)
    ok=Rectangle(Point(200,425),Point(250,475))
    ok.setFill('green')
    ok.draw(win)
    okbutt=Text(Point(225,450),'OK!').draw(win)
    
    #Random Initial Position of Each Tank to begin the game
    tank1_pos=RandomInitialPosition() 
    tank2_pos=RandomInitialPosition()
    initialPos1=Text(Point(50,90), "The starting position of tank 1 is: "+str(tank1_pos)).draw(win2)
    initialPos2=Text(Point(50,80), "The starting position of tank 2 is: "+str(tank2_pos)).draw(win2)
    #assign initial status of tank1 and tank 2
    #Alive=1 #Dead=0
    tank1=1
    tank2=1
    #keeps track of each found to display on output screen
    rnd=0
    #draws initial tanks
    tankG1=tankGraphics1(tank1_pos,tank1,win)
    tankG2=tankGraphics2(tank2_pos,tank2,win)
    #condition that tank1 and tank2 are both in play to proceed 
    #   keep playing until a tank is "dead"
    while tank1==1 and tank2==1:
        #creates random wind
        wind=randomwind()
        #draws triangle indicating wind
        tri=windgraphics(wind,win)
        #assign randomwindfactor and pass it through the function fireshot
        #Player 1 chooses if they shoot or move 50m
        tank1_pos,tank2,tankG1,shot_pos1=choicePlayer1(tank1_pos, tank2_pos,wind,win,tank1,tank2,tankG1,win2)
        #Player 2 chooses if they shoot or move50
        tank2_pos,tank1,tankG2,shot_pos2=choicePlayer2(tank2_pos, tank1_pos,wind,win,tank1,tank2,tankG2,win2)
     
     
        text1,text2=printStat(tank1,tank2)
        #undraws triangle indicating wind
        tri.undraw()
        #increments the round
        rnd=rnd+1
        #clears output graphics screen
        win2.delete('all')
        #prints output for the round
        RND=Text(Point(15,70),'Round '+str(rnd)).draw(win2)
        printPos1=Text(Point(50,60),'Tank 1 is located at: '+str(tank1_pos)).draw(win2)
        printPos2=Text(Point(50,50),'Tank 2 is located at: '+str(tank2_pos)).draw(win2)
        printShot1=Text(Point(50,40),"Player 1's shot landed at: "+str(shot_pos1)).draw(win2)
        printShot2=Text(Point(50,30),"Player 2's shot landed at: "+str(shot_pos2)).draw(win2)
        printLife1=Text(Point(50,20),text1).draw(win2)
        printLife2=Text(Point(50,10),text2).draw(win2)
        
    message4=Text(Point(350,250),'Game over! Click anywhere to quit')
    message4.setTextColor('red')
    message4.setSize(30)
    message4.draw(win)
    win.getMouse()
    win.close()
    win2.close()
         
main()

