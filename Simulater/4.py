import random

def estimate_pi(num_samples):
    inside_circle = 0
    total = 0
    for i in range(num_samples):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        distance = x**2 + y**2
        if distance <= 1:
            inside_circle += 1
        total += 1
    pi = 4 * inside_circle / total
    return pi

# Test the function
num_samples = 1000000
pi = estimate_pi(num_samples)
print("Estimated value of pi:", pi)