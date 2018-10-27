
def showCircle(circle):
  print('#####Circle#####\n')
  print('center x:', circle.center.x)
  print('center y:', circle.center.y)
  print('\nradius:', circle.radius)
  print('################\n\n')

def showRect(rect):
  print('######Rect######')
  print("width:", rect.width)
  print("height:", rect.height)
  print("\ncorner x:", rect.corner.x)
  print("corner y %d" % rect.corner.y)
  print('################\n\n')


def move_rectangle(rect, dx, dy):
  rect.corner.x += dx
  rect.corner.y += dy

def move_copy_rectangle(rect, dx, dy):
  from copy import deepcopy
  c_rect = deepcopy(rect)
  move_rectangle(c_rect, dx, dy)
  return c_rect

def distance_point(point1, point2):
  x1, y1 = point1.x, point1.y
  x2, y2 = point2.x, point2.y
  distance = (((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** (1/2)
  return distance

def point_in_circle(circle, point):
  distance = distance_point(circle.center, point)
  if distance <= circle.radius:
    return True
  else:
    return False

def rect_4_point(rect):
  p1 = 

def rect_in_circle(circle, rect):
