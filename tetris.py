
class Grid:
  def __init__(self):
    self.grid = list()
    for line in range(20):
      self.grid.append([0,0,0,0,0,0,0,0,0,0])

  def print(self):
    for line in range(20):
      print(self.grid[line])





print("TETRIS grid")

test = Grid()
test.print()