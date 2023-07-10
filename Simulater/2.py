import math
import matplotlib.pyplot as plt

class Ship:
    def __init__(self, x, y, heading, speed, acceleration):
        self.x = x
        self.y = y
        self.heading = heading
        self.speed = speed
        self.acceleration = acceleration
        
    def update_position(self, time):
        distance = self.speed * time + 0.5 * self.acceleration * time**2
        x_change = distance * math.sin(self.heading)
        y_change = distance * math.cos(self.heading)
        self.x += x_change
        self.y += y_change
        self.speed += self.acceleration * time
        
# Example usage
ship = Ship(0, 0, math.pi/2, 0, 1) # Starting position at (0,0) facing North, stationary
positions = [(ship.x, ship.y)]

timestep = 0.1
time = 0
while ship.speed < 10:
    ship.update_position(timestep)
    positions.append((ship.x, ship.y))
    time += timestep

# Plot the ship's path
x_vals = [p[0] for p in positions]
y_vals = [p[1] for p in positions]

plt.plot(x_vals, y_vals)
plt.title("Ship's Launch Path")
plt.xlabel("XPosition")
plt.ylabel("Y Position")
plt.show()