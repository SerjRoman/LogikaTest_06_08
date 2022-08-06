import turtle


from dialogs import *
import pygame


def move_turtle(x,y,object):
    
    object.penup()
    object.goto(x,y)
    object.pendown()
print('hello world')
def write_text_turtle(object,text,font_size):
    object.write(
    text, move=False,
    font=("Helvetica", font_size, "bold"))

def main():
    
    print(dict_dialogs['hello'])
    
    text = str(input(dict_dialogs['start']))
    
    my_turtle = turtle.Turtle()
    
    my_turtle.hideturtle()
    while True:
        
        move_turtle(-400,300,my_turtle)

        write_text_turtle(my_turtle,text,25)
        
        text = str(input(dict_dialogs['start']))
            
        if text == 'Стоп':
            print(dict_dialogs['bye-bye'])
            turtle.done()
            break
        
        my_turtle.clear()
        
    

main()
    