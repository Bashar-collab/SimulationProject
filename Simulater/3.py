import math
import pygame

class Ship:
    def __init__(self, x, y, heading, speed, acceleration):
        self.x = x
        self.y = y
        self.heading = heading
        self.speed = speed
        self.acceleration = acceleration
        
    def update_position(self, time, wind_speed, wind_direction, wave_height, wave_period):
        # Calculate the effective wind speed and direction
        wind_angle = wind_direction - self.heading
        wind_speed_x = wind_speed * math.sin(wind_angle)
        wind_speed_y = wind_speed * math.cos(wind_angle)
        effective_speed_x = self.speed + wind_speed_x
        effective_speed_y = wind_speed_y
        
        # Calculate the distance and direction of movement
        distance = math.sqrt(effective_speed_x**2 + effective_speed_y**2) * time
        movement_angle = math.atan2(effective_speed_x, effective_speed_y)
        wave_factor = math.sin((2 * math.pi / wave_period) * time)
        x_change = distance * (math.sin(movement_angle) + wave_factor * wave_height)
        y_change = distance * (math.cos(movement_angle) + wave_factor * wave_height)
        
        # Update the position
        self.x += x_change
        self.y += y_change
        # Update the position
        self.x += x_change
        self.y += y_change
        self.speed += self.acceleration * time

# Set up simulation parameters
time_step = 0.1
total_time = 20
wind_speed = 5
wind_direction = math.pi/4
wave_height = 0.5
wave_period = 2

# Set up initial conditions
ship = Ship(0, 0, math.pi/4, 0, 1)

# Initialize Pygame
pygame.init()
screen_width, screen_height = 500, 500
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Ship Launch Simulation")

# Set up colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Run simulation
clock = pygame.time.Clock()
time = 0
positions = []
while time < total_time:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            
    # Update ship position
    ship.update_position(time_step, wind_speed, wind_direction, wave_height, wave_period)
    positions.append([ship.x,ship.y])
   # positions.append(ship.y)
    time += time_step
    
    # Draw ship and path
    screen.fill(WHITE)
    pygame.draw.circle(screen, BLACK, (int(ship.x), int(ship.y)), 10)
    for i ,p in enumerate(positions) :

        pygame.draw.circle(screen, BLACK, (p[0], p[1]), 2)
        
    pygame.display.flip()
    clock.tick(60)

pygame.quit()