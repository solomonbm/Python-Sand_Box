from turtle import *
from datetime import datetime

def moving(distance, angle=0):
    penup()
    right(angle)
    forward(distance)
    left(angle)
    pendown()

def layout(length, vast):
    fd(length*1.5)
    rt(90)
    fd(vast/2.0)
    lt(120)
    fd(vast)
    lt(120)
    fd(vast)
    lt(120)
    fd(vast/2.0)

def timer_hands(name, length, vast):
    reset()
    moving(-length*0.15)
    begin_poly()
    layout(length, vast)
    end_poly()
    clock_labelings = get_poly()
    register_shape(name, clock_labelings)

def clockface(radius):
    reset()
    pensize(7)
    for i in range(60):
        moving(radius)
        if i % 5 == 0:
            fd(25)
            moving(-radius-25)
        else:
            dot(3)
            moving(-radius)
        rt(6)    
                    
def settings():    
    global second_hand, minute_hand, hour_hand
    timer_hands("second_hand", 100, 25)
    timer_hands("minute_hand", 95, 25)
    timer_hands("hour_hand", 70, 25)
    clockface(160)
    second_hand = Turtle()
    second_hand.shape("second_hand")
    second_hand.color("gray40", "black")
    minute_hand = Turtle()
    minute_hand.shape("minute_hand")
    minute_hand.color("red", "orange")
    hour_hand = Turtle()
    hour_hand.shape("hour_hand")
    hour_hand.color("red", "orange")
    for hand in second_hand, minute_hand, hour_hand:
        hand.resizemode("user")
        hand.shapesize(1, 1, 3)
        hand.speed(0)
    ht()

def tick():
    t = datetime.today()
    secondTimer = t.second + t.microsecond*0.000001
    minute = t.minute + secondTimer/60.0
    onTheHour = t.hour + minute/60.0
    try:
        tracer(False)
        second_hand.setheading(6*secondTimer)
        minute_hand.setheading(6*minute)
        hour_hand.setheading(30*onTheHour)
        tracer(True)
        ontimer(tick, 100)
    except Terminator:
        pass

def main():
    tracer(False)
    settings()
    tracer(True)
    tick()

    return "DONE"

if __name__ == "__main__":
    mode("logo")
    msg = main()
    print(msg)
    mainloop()
    
