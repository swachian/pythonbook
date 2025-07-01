from random import choice

class RandomWalk:
    def __init__(self, num_points=5000):
        self.num_points = num_points
    
        self.x_values = [0]
        self.y_values = [0]
    
    def fill_walk(self):
        while len(self.x_values) < self.num_points:
            x_step = self._get_step()
            y_step = self._get_step([1, -1], [1, 2, 3, 4, 5, 6, 7, 8])

            if x_step == 0 and y_step == 0:
                continue

            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step
            
            self.x_values.append(x)
            self.y_values.append(y)
    
    def _get_step(self, direction = [1, -1], distance = [0, 1, 2, 3, 4]):
        step = choice(direction) * choice(distance)
        return step