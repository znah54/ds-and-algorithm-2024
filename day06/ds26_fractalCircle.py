# file : ds26_fractalCircle.py
# desc : 프랙탈 원 그리기

from tkinter import *
import random

def drawCircle(x, y, r):
    canvas.create_oval(x-r, x-y, x+r,y+r,width=2,outline=random.choice(colors))
    if r >=5:
        drawCircle(x-r//2, y, r//2)
        drawCircle(x+r//2, y, r//2)
    

# 전역변수
radius=400
wSize=1000
colors=['red','azure','purple','orange','gray','white','black','green','blue']

# 메인코드
window = Tk()
window.title('프랙탈 원그리기')
canvus = Canvas(window, height=wSize, width=wSize, bg='white')

drawCircle(wSize//2, wSize//2, radius)

canvus.pack()
window.mainloop()