import random

rows, cols = 3, 3
room = [[random.choice(["Clean", "Dirty"]) for _ in range(cols)] for _ in range(rows)]

# Step 2: Place vacuum at a random position
agent_x = random.randint(0, rows - 1)
agent_y = random.randint(0, cols - 1)

# Step 3: Reflex agent function
def reflex_agent(x, y):
    if room[x][y] == "Dirty":
        return "Suck"
    else:
        return random.choice(["Up", "Down", "Left", "Right"])

# Step 4: Run simulation
print("Initial Room State:")
for row in room:
    print(row)

print("\nVacuum starting position:", (agent_x, agent_y))
print("-" * 50)

for step in range(10):
    action = reflex_agent(agent_x, agent_y)
    print(f"Step {step + 1}: Position ({agent_x},{agent_y}) | Action: {action}")

    if action == "Suck":
        room[agent_x][agent_y] = "Clean"

    elif action == "Up" and agent_x > 0:
        agent_x -= 1
    elif action == "Down" and agent_x < rows - 1:
        agent_x += 1
    elif action == "Left" and agent_y > 0:
        agent_y -= 1
    elif action == "Right" and agent_y < cols - 1:
        agent_y += 1

print("-" * 50)
print("Final Room State:")
for row in room:
    print(row)
