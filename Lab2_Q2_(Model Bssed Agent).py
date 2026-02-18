import random

# Room size
rows, cols = 3, 3

# Actual environment
room = [[random.choice(["Clean", "Dirty"]) for _ in range(cols)] for _ in range(rows)]

# Agent's internal model (initially unknown)
model = [["Unknown" for _ in range(cols)] for _ in range(rows)]

# Initial agent position
agent_x = random.randint(0, rows - 1)
agent_y = random.randint(0, cols - 1)

def model_based_agent(x, y):
    # Update model with current perception
    model[x][y] = room[x][y]

    if room[x][y] == "Dirty":
        return "Suck"

    # Search for a dirty block in model
    for i in range(rows):
        for j in range(cols):
            if model[i][j] == "Dirty":
                if i < x:
                    return "Up"
                elif i > x:
                    return "Down"
                elif j < y:
                    return "Left"
                elif j > y:
                    return "Right"

    return "NoOp"  # Everything is clean

# Simulation
print("Initial Room:")
for row in room:
    print(row)

print("\nAgent start position:", (agent_x, agent_y))
print("-" * 50)

for step in range(15):
    action = model_based_agent(agent_x, agent_y)
    print(f"Step {step+1}: Position ({agent_x},{agent_y}), Action: {action}")

    if action == "Suck":
        room[agent_x][agent_y] = "Clean"
        model[agent_x][agent_y] = "Clean"
    elif action == "Up" and agent_x > 0:
        agent_x -= 1
    elif action == "Down" and agent_x < rows - 1:
        agent_x += 1
    elif action == "Left" and agent_y > 0:
        agent_y -= 1
    elif action == "Right" and agent_y < cols - 1:
        agent_y += 1
