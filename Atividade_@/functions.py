from copy import copy

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


def move_copy_point(point, x, y):
  c_point = copy(point)
  c_point.x += x
  c_point.y += y
  return c_point


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

def rect_4_points(rect):
  p1 = copy(rect.corner)
  p2 = move_copy_point(p1, rect.width, 0)
  p3 = move_copy_point(p1, 0, rect.height)
  p4 = move_copy_point(p1, rect.width, rect.height)

  return p1, p2, p3, p4
  

def rect_in_circle(circle, rect):
  for point in rect_4_points(rect):
    if distance_point(point, circle.center) > circle.radius:
      return False
  return True