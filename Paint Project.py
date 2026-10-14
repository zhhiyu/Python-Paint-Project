# Paint Project
# Zhiyu Su
# This paint program allows the user to draw, stamp, and create shapes on the
# canvas. The pencil is selected by default, but the user can select different
# tools to which a dialogue box pops up telling the user how to use it.

# Individual features: undo redo, spraypaint, highlighter, changing size/thickness,
# dialogue box, recent colours, dropper, brush, polygon

from pygame import *
from tkinter import *                
from pygame import *
from tkinter import filedialog
from math import *
from  random import *

root = Tk()     #for saving
root.withdraw()

font.init()     #for text
title = font.SysFont("Bodoni", 60)
dialogue = font.SysFont("Bodoni", 23)

WHITE = (255,255,255)

rectList = [] #changes the tool border if it is hovered or clicked
selectList = [] #determines which tools are selected
#dialogue that pops up when a tool is selected
dialogueList = ["Pencil: left click and drag to draw. Scroll up to increase size, down to decrease it.",
            "Brush: left click and drag to draw. Scroll up to increase size, down to decrease it.",
            "Eraser: left click and drag to erase. Scroll up to increase size, down to decrease it.",
            "Highlighter: left click and drag to highlight. Scroll up to increase size, down to decrease it.",
            "Undo: left click to undo.",
            "Redo: left click to redo.",
            "Spray: left click and drag to spray. Scroll up to increase size, down to decrease it.",
            "Dropper: left click on the canvas to select a colour on it.",
            "Fill: left click on the canvas to fill it with your colour.",
            "Clear Screen: left click on the canvas to clear it all.",
            "Stamp: drag and drop to draw a stamp.", "Stamp: drag and drop to draw a stamp.",
            "Stamp: drag and drop to draw a stamp.", "Stamp: drag and drop to draw a stamp.",
            "Stamp: drag and drop to draw a stamp.", "Stamp: drag and drop to draw a stamp.",
            "Filled Rectangle: left click and drag, release to draw.",
            "Unfilled rectangle: left click and drag, release to draw. Scroll up to increase thickness, down to decrease it.",
            "Line: left click and drag, release to draw. Scroll up to increase  thickness, down to decrease it.",
            "Filled ellipse: left click and drag, release to draw.",
            "Unfilled Ellipse: left click and drag, release to draw. Scroll up to increase thickness, down to decrease it.",
            "Filled Polygon: Left click 3 or more points, then right click to draw.",
            "Unfilled polygon: Left click 3 or more points, then right click to draw. Scroll up to increase thickness, down to decrease it.",
            "Image saved. Click twice to select another tool.",
            "Image loaded. Click twice to select another tool."]

colList = [] #list that all the colour selectors go in
recentc = [WHITE,WHITE,WHITE] #recent colours that show up on the screen
recentc2 = [(0),(0),(0)] #list that doesnt make the recent colour boxes go weird because it used to show the colour multiple times
oldc = [0] #the old colour that goes in the recent colours section
cList = [] #the collidepoint list that allows the user to select a colour inside the box

screen = display.set_mode((1500, 1000))
background = image.load("images/newbackground.jpg")
sunshine = image.load("images/Sunshine.png")
screen.blit(background,(0,0))
screen.blit(sunshine, (-20,-30)) #part of the background

#title
txtPic=title.render("Caterpillar Creations", True, (0))
screen.blit(txtPic,(550,100))

#canvas and border
canvasRect = Rect(300,300,1000,600)
draw.rect(screen, WHITE, canvasRect)
draw.rect(screen, (0,0,0), (299, 299, 1002, 602), 1)

#colours
c = 0 #this is default colour when the program is first opened
cDrop = 0 #to make the eyedropper colour show on the rectangle w/o selecting it
colourspectrum = image.load("images/spectrum.png") #colour spectrum
screen.blit(colourspectrum,(300,175))
specrect = Rect(298,173,102,102)
colList.append(specrect)
smallerspec = Rect(300,175,98,98)
draw.rect(screen, (0), smallerspec,-1) #to make the colour picker not get green
cList.append(smallerspec)

#black and white rectangle to get pure black/white
whiteRect = Rect(410,175,50,25)
colList.append(whiteRect)
draw.rect(screen,WHITE,whiteRect)
smallwhiteRect = Rect(412,177,46,21)
draw.rect(screen,(0),smallwhiteRect,-1)
cList.append(smallwhiteRect)

blackRect = Rect(410,200,50,25)
colList.append(blackRect)
draw.rect(screen,(0),blackRect)
smallblackRect = Rect(412,202,46,21)
draw.rect(screen,(0),smallblackRect,-1)
cList.append(smallblackRect)

#these are for the 3 recent colours next to the spectrum and under the current colour
recentrect1 = Rect(410,245,30,30)
colList.append(recentrect1)
smallrecent1 = recentrect1 #the small ones dont select the green colour
draw.rect(screen,(0),smallrecent1,-1)
cList.append(smallrecent1)

recentrect2 = Rect(450,245,30,30)
colList.append(recentrect2)
smallrecent2 = recentrect2
draw.rect(screen,(0),smallrecent2,-1)
cList.append(smallrecent2)

recentrect3 = Rect(490,245,30,30)
colList.append(recentrect3)
smallrecent3 = recentrect3
draw.rect(screen,(0),smallrecent3,-1)
cList.append(smallrecent3)

#tools
tool = "pencil" #default tool when program is launched

pencilRect = Rect(20,300,60,60)
rectList.append(pencilRect)
selectList.append("pencil")
draw.rect(screen,WHITE,pencilRect)
pencilimg = image.load("images/pencil.png")
screen.blit(pencilimg,(20,300))

brushRect = Rect(100,300,60,60)
rectList.append(brushRect)
selectList.append("brush")
draw.rect(screen,WHITE,brushRect)
brushimg = image.load("images/brush.png")
screen.blit(brushimg,(100,300))

eraserRect = Rect(180,300,60,60)
rectList.append(eraserRect)
selectList.append("eraser")
draw.rect(screen,WHITE,eraserRect)
eraserimg = image.load("images/eraser.png")
screen.blit(eraserimg,(180,300))

highRect = Rect(20,400,60,60)
rectList.append(highRect)
selectList.append("highlighter")
draw.rect(screen,WHITE,highRect)
hlimg=image.load("images/highlighter.png")
screen.blit(hlimg,(20,400))

undoRect = Rect(1160, 215, 60,60)
rectList.append(undoRect)
selectList.append("undo")
draw.rect(screen,WHITE,undoRect)
undoimg=image.load("images/undo.png")
screen.blit(undoimg,(1160,215))

redoRect = Rect(1240, 215, 60,60)
rectList.append(redoRect)
selectList.append("redo")
draw.rect(screen,WHITE,redoRect)
redoimg=image.load("images/redo.png")
screen.blit(redoimg,(1240,215))

sprayRect = Rect(100,400,60,60)
rectList.append(sprayRect)
selectList.append("spraypaint")
draw.rect(screen,WHITE,sprayRect)
sprayimg = image.load("images/spray.png")
screen.blit(sprayimg,(100,400))

dropRect = Rect(180,400,60,60)
rectList.append(dropRect)
selectList.append("dropper")
draw.rect(screen,WHITE,dropRect)
dropperimg = image.load("images/dropper.png")
screen.blit(dropperimg,(180,400))

fillRect = Rect(20,500,60,60)
rectList.append(fillRect)
selectList.append("fill")
draw.rect(screen,WHITE,fillRect)
fillimg=image.load("images/fill.png")
screen.blit(fillimg,(20,500))

clearRect = Rect(100,500,60,60)
rectList.append(clearRect)
selectList.append("clearscreen")
draw.rect(screen,WHITE,clearRect)
clearimg = image.load("images/clear.png")
screen.blit(clearimg,(100,500))


#stamps
apple = image.load("images/Apple.png")
appleRect = Rect(1400,400,70,70)
rectList.append(appleRect)
selectList.append("applestamp")
draw.rect(screen,WHITE,appleRect)
appleimg=transform.scale(apple,(90,66))
screen.blit(appleimg,(1390,400))

pear = image.load("images/Pear.png")
pearRect = Rect(1400,500,70,70)
rectList.append(pearRect)
selectList.append("pearstamp")
draw.rect(screen,WHITE,pearRect)
pearimg=transform.scale(pear, (60,68))
screen.blit(pearimg, (1405,500))

plum = image.load("images/Plum.png")
plumRect = Rect(1400,600,70,70)
rectList.append(plumRect)
selectList.append("plumstamp")
draw.rect(screen,WHITE,plumRect)
plumimg=transform.scale(plum, (70,72))
screen.blit(plumimg, (1405,600))

strawberry = image.load("images/Strawberry.png")
strawbRect = Rect(1400,700,70,70)
rectList.append(strawbRect)
selectList.append("strawbstamp")
draw.rect(screen,WHITE,strawbRect)
strawimg=transform.scale(strawberry, (56,70))
screen.blit(strawimg, (1405,700))

orange = image.load("images/Orange.png")
orangeRect = Rect(1400,800,70,70)
rectList.append(orangeRect)
selectList.append("orangestamp")
draw.rect(screen,WHITE,orangeRect)
orangeimg=transform.scale(orange, (60,79))
screen.blit(orangeimg, (1405,790))

caterpillar = image.load("images/Caterpillar.png")
caterpillarRect = Rect(1370,300,100,70)
rectList.append(caterpillarRect)
selectList.append("caterpillarstamp")
draw.rect(screen,WHITE,caterpillarRect)
caterpillarimg=transform.scale(caterpillar, (100,70))
screen.blit(caterpillarimg, (1370,300))

#shapes
rectfillRect = Rect(20,600,60,60)
rectList.append(rectfillRect)
selectList.append("rectfill")
draw.rect(screen,WHITE,rectfillRect)
rectfillimg = image.load("images/fillrectangle.png")
screen.blit(rectfillimg, (20,600))

rectunfillRect = Rect(100,600,60,60)
rectList.append(rectunfillRect)
selectList.append("rectunfill")
draw.rect(screen,WHITE,rectunfillRect)
rectunfillimg = image.load("images/unfillrectangle.png")
screen.blit(rectunfillimg, (100,600))

lineRect = Rect(180,600,60,60)
rectList.append(lineRect)
selectList.append("line")
draw.rect(screen,WHITE,lineRect)
lineimg = image.load("images/line.png")
screen.blit(lineimg, (180,600))

ellipsefillRect = Rect(20,700,60,60)
rectList.append(ellipsefillRect)
selectList.append("ellipsefill")
draw.rect(screen,WHITE,ellipsefillRect)
ellifillimg = image.load("images/fillellipse.png")
screen.blit(ellifillimg, (20,700))

ellipseunfillRect = Rect(100,700,60,60)
rectList.append(ellipseunfillRect)
selectList.append("ellipseunfill")
draw.rect(screen,WHITE,ellipseunfillRect)
elliunfillimg = image.load("images/unfillellipse.png")
screen.blit(elliunfillimg, (100,700))

polylist= []

polyfillRect = Rect(20,800,60,60)
rectList.append(polyfillRect)
selectList.append("polygonfill")
draw.rect(screen,WHITE,polyfillRect)
polyfillimg = image.load("images/fillpolygon.png")
screen.blit(polyfillimg, (20,800))

polyunfillRect = Rect(100,800,60,60)
rectList.append(polyunfillRect)
selectList.append("polygonunfill")
draw.rect(screen,WHITE,polyunfillRect)
polyunfillimg = image.load("images/unfillpolygon.png")
screen.blit(polyunfillimg, (100,800))

#for drawing shapes
start = 0,0

#for highlighter
cover = Surface((1000,600)).convert()
cover.set_alpha(5)
cover.fill((255,0,255))
cover.set_colorkey((255,0,255))

#undo and redo lists
undolist = [screen.subsurface(canvasRect).copy()]
redolist = []

#save and load
saveRect = Rect(720,215,60,60)
rectList.append(saveRect)
selectList.append("save")
draw.rect(screen,WHITE,saveRect)
saveimg=image.load("images/save.png")
screen.blit(saveimg,(720,215))

loadRect = Rect(800,215,60,60)
rectList.append(loadRect)
selectList.append("load")
draw.rect(screen,WHITE,loadRect)
loadimg=image.load("images/load.png")
screen.blit(loadimg,(800,215))

#border for the text explanations
draw.rect(screen,(0),(199,929,1202,57),1)

#size for tools
sizeshape = 3 #default size for shape outlines
size1 = 3 #default size for pencil
size2 = 10 #default size for eraser and paint brush
sizespray = 40 #default size for spray can
sizehl = 30 #default size for highlighter

running = True
while running:
    click = False
    rightclick = False
    for e in event.get():
        if e.type == MOUSEBUTTONDOWN:
            if e.button == 1:
                start = e.pos
                click = True
                back = screen.copy()
                sav = screen.subsurface(canvasRect).copy()
            if e.button == 3:
                rightclick = True
            if e.button == 4: #scroll wheel up
                if tool == "line" or tool == "rectunfill" or tool == "ellipseunfill" \
                or tool == "polygonunfill":
                    sizeshape += 1
                if tool == "pencil":
                    if size1 < 5:   #pencil looks ugly if it gets really big
                        size1 += 1
                if tool == "brush" or tool == "eraser":
                    size2 += 1
                if tool == "spraypaint":
                    sizespray += 1
                if tool == "highlighter":
                    sizehl +=1
            if e.button == 5: #scroll wheel down
                if tool == "line" or tool == "rectunfill" or tool == "ellipseunfill" \
                or tool == "polygonunfill":
                    if sizeshape > 1:    #sizeshape cannot be 0 because it will not draw
                        sizeshape -= 1
                if tool == "pencil":
                    if size1 > 1:
                        size1 -= 1
                if tool == "brush" or tool == "eraser":
                    if size2 > 1:
                        size2 -= 1
                if tool == "brush" or tool == "eraser":
                    if size2 >1:
                        size2 -= 1
                if tool == "spraypaint":
                    if sizespray > 1:
                        sizespray -= 1
                if tool == "highlighter":
                    if sizehl > 1:
                        sizehl -= 1
                    
        if e.type == MOUSEBUTTONUP: #for undo and redo
                if mb[0]==1 and canvasRect.collidepoint(omx,omy):
                    if (tool != "eyedropper" and tool != "save" and tool != "load"
                    and tool != "undo" and tool != "redo" and tool != "polygonfill"
                    and tool != "polygonunfill"): #these tools do not draw and for polygon you click to add points
                        undolist.append(screen.subsurface(canvasRect).copy())
        if e.type == QUIT:
            running = False
            
    mb = mouse.get_pressed()
    mx,my = mouse.get_pos()
    
    draw.rect(screen,c,(470,175,50,50)) #current colour
    draw.rect(screen,recentc[2],(410,245,30,30)) #recent colours
    draw.rect(screen,recentc[1],(450,245,30,30))
    draw.rect(screen,recentc[0],(490,245,30,30))

    #colour picker
    for i in range(len(cList)):
        if mb[0] and cList[i].collidepoint(mx,my): #inside the spectrum
            c = screen.get_at((mx,my))

    #colours of buttons, selecting the tool, tools dialogues
    for i in range(len(rectList)):
        draw.rect(screen,(0),rectList[i],2) #buttons when not pressed
        if rectList[i].collidepoint(mx,my): #button is yellow when hovered
            draw.rect(screen,(255,255,0),rectList[i],2)
            if mb[0]==1:
                tool = selectList[i] #changes the tool
        if tool == selectList[i]:    #button turns green when pressed
            draw.rect(screen,(0,255,0),rectList[i],2)
            draw.rect(screen,WHITE,(200,930,1200,55)) #white rectangle and text
            txtPic = dialogue.render(dialogueList[i], True, (0))
            screen.blit(txtPic,(210,943))
            
    for i in range(len(colList)): #colours are not tools, dont have to change back every time you use it
        draw.rect(screen,(0),colList[i],2)
        if colList[i].collidepoint(mx,my):
            draw.rect(screen,(255,255,0),colList[i],2) #turns border yellow
            if mb[0]==1:
                draw.rect(screen,(0,255,0),colList[i],2) #turns border green

    #clipping and tools
    if mb[0]==1 and (canvasRect.collidepoint(mx,my) or canvasRect.collidepoint(omx,omy)):
        screen.set_clip(canvasRect)  #only allows drawing inside canvas

        if (tool != "eyedropper" and tool != "save" and tool != "load"
        and tool != "undo" and tool != "redo"): #these tools don't draw
            redolist = [] #redo list is cleared
            if click: #for the recent colours
                if c != recentc2[-1]: #doesnt make the recent colours all turn the old colour if drawn >1 times
                    oldc.append(c)
                    recentc2.append(c)
                    del recentc[0]
                    recentc.append(oldc[-2])
                    
        #tools for drawing
        if tool == "pencil":
            draw.line(screen, c,(omx,omy),(mx,my),size1)
        elif tool == "eraser":
            draw.circle(screen,WHITE,(mx,my),size2)
            d = dist((omx,omy), (mx,my))
            bigX = mx-omx
            bigY = my-omy
            for i in range(int(d)): #smooth eraser
                d = max(1, d)   # if 0, make it 1
                sx = (bigX) / d
                sy = (bigY) / d
                draw.circle(screen,WHITE,(omx+sx*i,omy+sy*i),size2)
        elif tool == "fill":
            screen.fill(c)
        elif tool == "highlighter":
            d = dist((omx,omy),(mx,my))
            bigX = mx-omx
            bigY = my-omy
            for i in range(int(d)): #smooth highlighter
                d = max(1,d)
                sx = bigX / d
                sy = bigY / d
                cover.fill((255,0,255)) #doesn't draw multiple highlighters
                draw.rect(cover,c,(sizehl,sizehl,sizehl,sizehl))            #centers to mouse
                screen.blit(cover,((omx+sx*i)-(sizehl+(sizehl/2)),(omy+sy*i)-(sizehl+(sizehl/2))))
        elif tool == "dropper":
            c = screen.get_at((mx,my))
        elif tool == "clearscreen":
            screen.fill(WHITE)
        elif tool == "brush":
            draw.circle(screen,c,(mx,my),size2)
            d = dist((omx,omy), (mx,my))
            bigX = mx-omx
            bigY = my-omy
            for i in range(int(d)): #making the dots connect for a smooth brush
                d = max(1, d)   # if 0, make it 1
                sx = (bigX) / d
                sy = (bigY) / d
                draw.circle(screen,c,(omx+sx*i,omy+sy*i),size2)
        elif tool == "spraypaint":
            for i in range(2):
                x = randint(-sizespray,sizespray)
                y = randint(-sizespray,sizespray)
                if (x ** 2 + y ** 2) <= sizespray ** 2: #dots make circle instead of rect
                    draw.circle(screen,c,(mx + x, my + y),2)
        #stamps
        elif tool == "applestamp":
            screen.blit(back, (0,0))
            screen.blit(apple, (mx-apple.get_width()//2,my-apple.get_height()//2))
        elif tool == "strawbstamp":
            screen.blit(back, (0,0))
            screen.blit(strawberry, (mx-strawberry.get_width()//2,my-strawberry.get_height()//2))
        elif tool == "pearstamp":
            screen.blit(back, (0,0))
            screen.blit(pear, (mx-pear.get_width()//2,my-pear.get_height()//2))
        elif tool == "orangestamp":
            screen.blit(back, (0,0))
            screen.blit(orange, (mx-orange.get_width()//2,my-orange.get_height()//2))
        elif tool == "plumstamp":
            screen.blit(back, (0,0))
            screen.blit(plum, (mx-plum.get_width()//2,my-plum.get_height()//2))
        elif tool == "caterpillarstamp":
            screen.blit(back, (0,0))
            screen.blit(caterpillar, (mx-caterpillar.get_width()//2,my-caterpillar.get_height()//2))
            
        #shapes
        elif tool == "line":
            screen.blit(back,(0,0))
            draw.line(screen, c, start, (mx,my), sizeshape)
        elif tool == "rectfill":
            screen.blit(back,(0,0))
            rec = Rect(start[0],start[1],mx-start[0],my-start[1])
            rec.normalize()
            draw.rect(screen,c,(rec))
        elif tool == "rectunfill":
            screen.blit(back,(0,0))
            rec = Rect(start[0],start[1],mx-start[0],my-start[1])
            rec.normalize()
            draw.rect(screen,c,(rec),sizeshape)
        elif tool == "ellipsefill":
            screen.blit(back,(0,0))
            ellipse = Rect(start[0],start[1],mx-start[0],my-start[1])
            ellipse.normalize()
            draw.ellipse(screen,c,ellipse)
        elif tool == "ellipseunfill":
            screen.blit(back,(0,0))
            ellipse = Rect(start[0],start[1],mx-start[0],my-start[1])
            ellipse.normalize()
            draw.ellipse(screen,c,ellipse,sizeshape)
        if tool == "polygonfill" or tool == "polygonunfill":
            if click:
                polylist.append((mx,my))
            
        screen.set_clip(None)
    
    if click:   #for the tools that do not need to touch the canvas to work  
        #save and load
        if saveRect.collidepoint(mx,my):
            tool == "save"
            result = filedialog.asksaveasfilename()
            if ".jpg" not in result:
                result = result + ".jpg"
            image.save(sav, result)
            
        elif loadRect.collidepoint(mx,my):
            tool == "load"
            result = filedialog.askopenfilename(filetypes = [("Picture files", "*.png;*.jpg")])
            openimg = image.load(result)
            screen.set_clip(canvasRect)
            screen.blit(openimg,canvasRect)
            undolist.append(openimg) #undoing the loaded image
            screen.set_clip(None)
                            
            
        #undo and redo
        elif tool == "undo":
            if len(undolist) >1:
                redolist.append(undolist.pop()) #adds to redo list
                screen.blit(undolist[-1],(300,300)) #blits the previous drawing
        elif tool == "redo":
            if len(redolist)>0:
                undolist.append(redolist.pop()) #adds the copy to the undo list
                screen.blit(undolist[-1],(300,300)) #blits the undid drawing
                
    if rightclick and canvasRect.collidepoint(mx,my): #what draws the polygon
        screen.set_clip(canvasRect)
        if tool == "polygonfill":
            if len(polylist) >= 3: #must have 3 or more sides
                draw.polygon(screen,c,(polylist))
                undolist.append(screen.subsurface(canvasRect).copy()) #only after the polygon appears does it get added to the undolist
                polylist = []
        if tool == "polygonunfill":
            if len(polylist) >= 3:
                draw.polygon(screen,c,(polylist),sizeshape)
                undolist.append(screen.subsurface(canvasRect).copy())
                polylist = []
        screen.set_clip(None)
                
    omx, omy = mx,my
    display.flip()

quit()
