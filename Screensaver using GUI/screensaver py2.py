#  importing required modules 
import simplegui
import random

# declaring Global variables 
width = int(raw_input("enter frame size: "))   
height = int(raw_input("enter frame size: "))  
position = [100,100]
message  = "Hello"
interval = 1000

#Handlers

def update_text(text):
    ''' Handler for Text box'''
    global message
    message = text


def update_interval(interval_inp):
    ''' change the interval for screensaver refresh 
    and restart timer to apply updated interval '''
    global width
    global timer
    interval=int(float(interval_inp)*1000)
    timer.stop()
    timer = simplegui.create_timer(interval,tick)
    timer.start()
    

def tick():
    '''Handler for timer and 
    Generate Random position to screensaver text 
    ''' 
    x = random.randrange(0,width-10*len(message))   # width-10*len(message) to avoid text out-of frame
    y = random.randrange(20,height)				  # 20,height to avoid text out-of frame
    position[0] = x
    position[1] = y

def draw_canvas(canvas):
    '''Handler to draw canvas 
    in this program to draw text'''
    canvas.draw_text(message,position,24,"Red")
    #canvas.draw_circle(position,10,1,"White")

    
#create Frame 
frame = simplegui.create_frame("Screensaver",width,height,300)

#create handler even for text
text=frame.add_input("Message:",update_text,150)

#Register event handler 
interval_input = frame.add_input("interval of Frame in seconds(ex:3.123):",update_interval,50)
frame.set_draw_handler(draw_canvas)
timer = simplegui.create_timer(interval,tick)
frame.start()
timer.start()


    
'''
Code to implement other comtrols in frame
not yet implemented
def update_width(width_inp):
    global width
    global frame
    global timer 
    width=int(width_inp)
    print 1
    frame.stop()
    
    print width
    frame.start()
    print 3
    timer.start()

def update_height(height_inp):
    global heigth
    height=int(height_inp)
def update_xpos(xpos):
    position[0] = xpos
def update_ypos(ypos):
    position[1] = ypos'''

'''width_input=frame.add_input("Width of Frame :",update_width,50)
height_input=frame.add_input("Height of Frame:",update_height,50)
xpos=frame.add_input("Message x position: ",update_xpos,50)
ypos=frame.add_input("Message y position: ",update_ypos,50)
'''
