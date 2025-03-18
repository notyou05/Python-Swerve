import time

def sim_drive(X, Y, rot, duration=500000000000):
    sim_x, sim_y, sim_rot = 0, 0, 0  # Initialize the simulation state

    for _ in range(duration):  # Run for a fixed number of iterations
        time.sleep(0.001)
        sim_x += X
        sim_y += Y
        sim_rot += rot
        print(f"Position: ({sim_x}, {sim_y}), Rotation: {sim_rot}")

    return sim_x, sim_y, sim_rot  # Return final state

# Call the function and print the result
print(sim_drive(1, 1, 2))

