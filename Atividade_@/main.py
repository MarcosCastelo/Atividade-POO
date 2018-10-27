from classes import *
from functions import *
def main():
  c = Circle()
  c.center.x = 150
  c.center.y = 100
  c.radius = 75

  r = Rect()
  r.corner.x = 100
  r.corner.y = 50
  r.width = 25
  r.height = 25

  if rect_in_circle(c, r):
  	print("Esta dentro")
  else:
  	print("Esta fora")



if __name__ == "__main__":
  main()