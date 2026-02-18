from collections import deque

# Goal Test
def goalTest(current_state, goal_state):
    return current_state == goal_state

# Valid State Check
def is_valid(state):
    ML, CL, boat = state
    MR = 3 - ML
    CR = 3 - CL

    # No negative or overflow values
    if ML < 0 or CL < 0 or ML > 3 or CL > 3:
        return False

    # Missionaries should not be outnumbered
    if (ML > 0 and ML < CL):
        return False
    if (MR > 0 and MR < CR):
        return False

    return True
# Successor Function
def successor(state):
    ML, CL, boat = state
    children = []

    # Production rules (boat capacity = 2)
    moves = [
        (1, 0),   # 1 missionary
        (2, 0),   # 2 missionaries
        (0, 1),   # 1 cannibal
        (0, 2),   # 2 cannibals
        (1, 1)    # 1 missionary & 1 cannibal
    ]

    for m, c in moves:
        if boat == 1:  # boat on left
            new_state = (ML - m, CL - c, 0)
        else:          # boat on right
            new_state = (ML + m, CL + c, 1)

        if is_valid(new_state):
            children.append(new_state)

    return children

# Verify Successor Function
print("Successors of (3,3,1):")
print(successor((3,3,1)))
print("-" * 40)

# Generate Path

def generate_path(closed, goal_state):
    path = []
    state = goal_state

    while state is not None:
        path.append(state)
        state = closed[state]

    path.reverse()
    return path
# BFS Algorithm
def BFS(initial_state, goal_state):
    OPEN = deque([initial_state])
    CLOSED = {initial_state: None}

    while OPEN:
        state = OPEN.popleft()

        if goalTest(state, goal_state):
            return generate_path(CLOSED, state)

        for child in successor(state):
            if child not in CLOSED:
                OPEN.append(child)
                CLOSED[child] = state

    return None
# DFS Algorithm
def DFS(initial_state, goal_state):
    OPEN = [initial_state]
    CLOSED = {initial_state: None}

    while OPEN:
        state = OPEN.pop()

        if goalTest(state, goal_state):
            return generate_path(CLOSED, state)

        for child in successor(state):
            if child not in CLOSED:
                OPEN.append(child)
                CLOSED[child] = state

    return None
# Run the Program
initial_state = (3,3,1)
goal_state = (0,0,0)

print("BFS Solution Path:")
bfs_path = BFS(initial_state, goal_state)
print(bfs_path)

print("\nDFS Solution Path:")
dfs_path = DFS(initial_state, goal_state)
print(dfs_path)
