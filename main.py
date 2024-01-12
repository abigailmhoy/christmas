from tkinter import *
import turtle
import colorsys

screen = turtle.Screen()
screen.setup(860, 525)

t=turtle.Turtle()
t.speed(0)

def drawCool(sat, val):
  n=50
  h=.26
  increasing=True
  for i in range(500):

    c=colorsys.hsv_to_rgb(h, sat, val)
    if increasing:
      h=h+1/n
    if not increasing:
      h=h-1/n
    if h>=.76:
      increasing=False
    if h<=.26:
      increasing=True

    t.color(c)
    t.forward(i*2)
    t.left(145)
def drawWarm(sat, val):
  n=100
  h=0
  increasing=True

  for i in range(500):

    c=colorsys.hsv_to_rgb(h, sat, val)
    if increasing:
      h=h+1/n
    if not increasing:
      h=h-1/n
    if h>=.18:
      increasing=False
    if h<=0:
      increasing=True

    t.color(c)
    t.forward(i*2)
    t.left(145)
def drawRainbow(sat, val):
  n=50
  h=0

  for i in range(500):

    c=colorsys.hsv_to_rgb(h, sat, val)
    h=h+1/n
    t.color(c)
    t.forward(i*2)
    t.left(145)

class Window(Frame):

  def __init__(self, master=None):
    Frame.__init__(self, master)

    self.colorScheme = None
    self.lightnessScheme = None
    self.satu=1
    self.valu=1

    lblColor = Label(root, text="Pick a color and lightness scheme")
    lblColor.pack()

    # widget can take all window
    self.pack(fill=BOTH, expand=1)

    # create button, link it to appropriate setter
    coolButton = Button(self, text="Cool", command=self.pickCool)
    warmButton = Button(self, text="Warm", command=self.pickWarm)
    rainbowButton = Button(self, text="Rainbow", command=self.pickRainbow)
    lightButton = Button(self, text="Light", command=self.pickLight)
    normalButton = Button(self, text="Normal", command=self.pickNormal)
    darkButton = Button(self, text="Dark", command=self.pickDark)

    # places button
    coolButton.place(x=0, y=0)
    warmButton.place(x=0, y=30)
    rainbowButton.place(x=0, y=60)
    lightButton.place(x=0, y=120)
    normalButton.place(x=0, y=150)
    darkButton.place(x=0, y=180)

  # setters
  def pickCool(self):
    self.colorScheme = "cool"

  def pickWarm(self):
    self.colorScheme = "warm"

  def pickRainbow(self):
    self.colorScheme = "rainbow"

  def pickLight(self):
    self.lightnessScheme = "light"
    self.satu=.45
    self.valu=1

  def pickNormal(self):
    self.lightnessScheme = "normal"
    self.satu=1
    self.valu=1

  def pickDark(self):
    self.lightnessScheme = "dark"
    self.satu=1
    self.valu=.45

  def checkScheme(self):
    if self.colorScheme in ["cool", "warm", "rainbow"] and self.lightnessScheme in ["light", "normal", "dark"]:
      root.destroy()

      if self.colorScheme=="cool":
        drawCool(self.satu,self.valu)

      if self.colorScheme=="warm":
        drawWarm(self.satu,self.valu)

      if self.colorScheme=="rainbow":
        drawRainbow(self.satu,self.valu)
    
    else:
      self.after(1000, self.checkScheme)  # check again after 1 second


root = Tk()
app = Window(root)
root.wm_title("Julie")
root.attributes('-fullscreen', True)
app.after(1000, app.checkScheme)  # start checking after 1 second
root.mainloop()

