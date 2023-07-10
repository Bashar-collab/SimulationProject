import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Set up the display
width = 800
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Launching Ship Simulation")

# Set up the ship
ship_x = width // 2
ship_y = height - 50
ship_speed = 0
ship_acceleration = 0
ship_mass = 1000
ship_thrust = 20000
ship_image = pygame.image.load("ship.png")

# Set up the water
water_height = height // 3
water_color = (0, 0, 255)

# Set up the wave animation
wave_height = 20
wave_speed = 3
wave_colors = [(0, 0, 255), (0, 100, 255), (0, 150, 255), (0, 100, 255)]
wave_offset = 0

# Set up the launch platform
platform_width = 200
platform_height = 20
platform_color = (200, 200, 200)
platform_x = width // 2 - platform_width // 2
platform_y = height - water_height - platform_height

# Set up the text
font = pygame.font.SysFont(None, 30)

# Set up the gameloop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Start the ship launch
                ship_acceleration = ship_thrust / ship_mass

    # Update the ship
    ship_speed += ship_acceleration
    ship_y += ship_speed
    ship_acceleration = 0

    # Check if the ship has landed on the platform
    if ship_y + ship_image.get_height() >= platform_y and \
       ship_x + ship_image.get_width() >= platform_x and \
       ship_x <= platform_x + platform_width:
        # Display a success message
        message = font.render("Success!", True, (0, 255, 0))
        screen.blit(message, (width // 2 - message.get_width() // 2, height // 2 - message.get_height() // 2))
        pygame.display.update()
        pygame.time.wait(2000) # Wait 2 seconds before quitting
        running = False

    # Draw the water
    pygame.draw.rect(screen, water_color, (0, height - water_height, width, water_height))

    # Draw the waves
    for i in range(0, width, wave_height * 2):
        pygame.draw.polygon(screen, wave_colors[i // (wave_height * 2) % len(wave_colors)], [(i - wave_offset, height - water_height), (i - wave_offset + wave_height, height - water_height - wave_height), (i - wave_offset + wave_height * 2, height - water_height)], 0)

    # Update the wave animation
    wave_offset += wave_speed
    if wave_offset >= wave_height * 2:
        wave_offset -= wave_height * 2

    # Draw the launch platform
    pygame.draw.rect(screen, platform_color, (platform_x, platform_y, platform_width, platform_height))

    # Update the ship acceleration based on gravity and thrust
    gravity_acceleration = 9.8
    ship_acceleration += gravity_acceleration
    if ship_acceleration > 0:
        ship_acceleration -= 0.1 # Air resistance
    else:
        ship_acceleration += 0.1 # Air resistance
    if ship_y + ship_image.get_height() >= height - water_height: # Ship is in the water
        ship_acceleration -= gravity_acceleration * 0.1 # Buoyancy

    # Update the ship speed and position based on the acceleration
    if ship_acceleration > 0 and ship_speed > 0:
        ship_speed -= 0.1 # Air resistance
    elif ship_acceleration < 0 and ship_speed < 0:
        ship_speed += 0.1 # Air resistance
    ship_y += 0.5 * ship_acceleration
    ship_x += ship_speed

    # Draw the ship
    rotated_ship_image = pygame.transform.rotate(ship_image, -math.degrees(math.atan2(ship_speed, ship_acceleration)))
    screen.blit(rotated_ship_image, (ship_x, ship_y))

    # Update the display
    pygame.display.update()

    # Wait a short time before updating the screen again
    pygame.time.wait(10)

# Clean up Pygame
pygame.quit()