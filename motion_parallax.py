from graphics import *
import random
import pyautogui

mouseX, mouseY = pyautogui.position()

def scene(x,y):
    win = GraphWin("Scene", x, y)
    win.setBackground('skyblue')

    #layer 1
    sun = Circle(Point(win.getWidth()*0.8,win.getHeight()*0.2), win.getHeight()*0.1)
    sun.setFill('yellow')
    sun.draw(win)
    

    #layer 2
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    t1 = Polygon(Point(win.getWidth()/2, win.getHeight()*0.3),Point(0,win.getHeight()),Point(win.getWidth(),win.getHeight()))
    t1.setFill(color_rgb(r,g,b))
    t1.draw(win)


    #layer 3
    t2 = Polygon(Point(win.getWidth()*0.3, win.getHeight()*0.45),Point(0,win.getHeight()),Point(win.getWidth()*0.6,win.getHeight()))
    t2.setFill(color_rgb(g,b,r))
    t2.draw(win)

    t3 = Polygon(Point(win.getWidth()*0.7, win.getHeight()*0.5),Point(win.getWidth()*0.4,win.getHeight()),Point(win.getWidth(),win.getHeight()))
    t3.setFill(color_rgb(b,r,g))
    t3.draw(win)

    

    #layer 4
    land = Rectangle(Point(0, win.getHeight()*0.9),Point(win.getWidth(), win.getHeight()))
    land.setOutline('green')
    land.setFill('green')
    land.draw(win)
   
    for i in range(100):
        grass = Rectangle(Point((i/100)*win.getWidth(),win.getHeight()*0.85),Point((i/100)*win.getWidth()+2,win.getHeight()*0.9))
        grass.setOutline('green')
        grass.setFill('green')
        grass.draw(win)

    trunk = Rectangle(Point(win.getWidth()*0.8, win.getHeight()*0.8),Point(win.getWidth()*0.85, win.getHeight()*0.95))
    trunk.setFill('brown')
    trunk.draw(win)

    tree = Oval(Point(win.getWidth()*0.75, win.getHeight()*0.65),Point(win.getWidth()*0.9, win.getHeight()*0.85))
    tree.setFill('green')
    tree.draw(win)


    #birds
    bird1wing1 = Line(Point(-50,100),Point(-40,105))
    bird1wing2 = Line(Point(-40,105),Point(-30,100))
    bird1wing1.draw(win)
    bird1wing2.draw(win)
    
    bird2wing1 = Line(Point(-40,110),Point(-30,115))
    bird2wing2 = Line(Point(-30,115),Point(-20,110))
    bird2wing1.draw(win)
    bird2wing2.draw(win)
    
    bird3wing1 = Line(Point(-30,120),Point(-20,125))
    bird3wing2 = Line(Point(-20,125),Point(-10,120))
    bird3wing1.draw(win)
    bird3wing2.draw(win)

    bird4wing1 = Line(Point(-20,130),Point(-10,135))
    bird4wing2 = Line(Point(-10,135),Point(0,130))
    bird4wing1.draw(win)
    bird4wing2.draw(win)
        
    bird5wing1 = Line(Point(-10,140),Point(0,145))
    bird5wing2 = Line(Point(0,145),Point(10,140))
    bird5wing1.draw(win)
    bird5wing2.draw(win)

    while(1):
        while(bird1wing1.getP1().getX()<win.getWidth()):
            bird1wing1.move(1,0)
            bird1wing2.move(1,0)
            bird2wing1.move(1,0)
            bird2wing2.move(1,0)
            bird3wing1.move(1,0)
            bird3wing2.move(1,0)
            bird4wing1.move(1,0)
            bird4wing2.move(1,0)
            bird5wing1.move(1,0)
            bird5wing2.move(1,0)

            mouseX, mouseY = pyautogui.position()
            sun.undraw()
            sun = Circle(Point(win.getWidth()*0.8+(mouseX-250)/145,win.getHeight()*0.2+(mouseY-250)/145), win.getHeight()*0.1)
            sun.setFill('yellow')
            sun.draw(win)
            
            t1.undraw()
            t1 = Polygon(Point(win.getWidth()/2+(mouseX-250)/65, win.getHeight()*0.3+(mouseY-250)/65),Point(0+(mouseX-250)/65,win.getHeight()+(mouseY-250)/65),Point(win.getWidth()+(mouseX-250)/65,win.getHeight()+(mouseY-250)/65))
            t1.setFill(color_rgb(r,g,b))
            t1.draw(win)

            t2.undraw()
            t3.undraw()
            t2 = Polygon(Point(win.getWidth()*0.3+(mouseX-250)/25, win.getHeight()*0.45+(mouseY-250)/25),Point(0+(mouseX-250)/25,win.getHeight()+(mouseY-250)/25),Point(win.getWidth()*0.6+(mouseX-250)/25,win.getHeight()+(mouseY-250)/25))
            t2.setFill(color_rgb(g,b,r))
            t2.draw(win)

            t3 = Polygon(Point(win.getWidth()*0.7+(mouseX-250)/25, win.getHeight()*0.5+(mouseY-250)/25),Point(win.getWidth()*0.4+(mouseX-250)/25,win.getHeight()+(mouseY-250)/25),Point(win.getWidth()+(mouseX-250)/25,win.getHeight()+(mouseY-250)/25))
            t3.setFill(color_rgb(b,r,g))
            t3.draw(win)

            land.undraw()
            grass.undraw()
            trunk.undraw()
            tree.undraw()

            land = Rectangle(Point(0, win.getHeight()*0.9+(mouseY-250)/5),Point(win.getWidth(), win.getHeight()))
            land.setOutline('green')
            land.setFill('green')
            land.draw(win)
   
            for i in range(100):
                grass = Rectangle(Point((i/100)*win.getWidth()+(mouseX-250)/5,win.getHeight()*0.85+(mouseY-250)/5),Point((i/100)*win.getWidth()+2+(mouseX-250)/5,win.getHeight()*0.9+(mouseY-250)/5))
                grass.setOutline('green')
                grass.setFill('green')
                grass.draw(win)

            trunk = Rectangle(Point(win.getWidth()*0.8+(mouseX-250)/5, win.getHeight()*0.8+(mouseY-250)/5),Point(win.getWidth()*0.85+(mouseX-250)/5, win.getHeight()*0.95+(mouseY-250)/5))
            trunk.setFill('brown')
            trunk.draw(win)

            tree = Oval(Point(win.getWidth()*0.75+(mouseX-250)/5, win.getHeight()*0.65+(mouseY-250)/5),Point(win.getWidth()*0.9+(mouseX-250)/5, win.getHeight()*0.85+(mouseY-250)/5))
            tree.setFill('green')
            tree.draw(win)

        bird1wing1 = Line(Point(-50,100),Point(-40,105))
        bird1wing2 = Line(Point(-40,105),Point(-30,100))
        bird1wing1.draw(win)
        bird1wing2.draw(win)
    
        bird2wing1 = Line(Point(-40,110),Point(-30,115))
        bird2wing2 = Line(Point(-30,115),Point(-20,110))
        bird2wing1.draw(win)
        bird2wing2.draw(win)
    
        bird3wing1 = Line(Point(-30,120),Point(-20,125))
        bird3wing2 = Line(Point(-20,125),Point(-10,120))
        bird3wing1.draw(win)
        bird3wing2.draw(win)

        bird4wing1 = Line(Point(-20,130),Point(-10,135))
        bird4wing2 = Line(Point(-10,135),Point(0,130))
        bird4wing1.draw(win)
        bird4wing2.draw(win)
        
        bird5wing1 = Line(Point(-10,140),Point(0,145))
        bird5wing2 = Line(Point(0,145),Point(10,140))
        bird5wing1.draw(win)
        bird5wing2.draw(win)


        
win = scene(500, 500)
drawSun(win)
drawMt(win)
drawMt2(win)
foreground(win)
birds(win)

