from collections import deque

# Step 1: Define WaterJug class
class WaterJug:
    def __init__(self, initial_state, goal_state):
        self.initial_state = initial_state  
        self.goal_state = goal_state       
        self.jug1_capacity = 4
        self.jug2_capacity = 3

    # Step 2: Goal Test Function
    def goalTest(self, current_state):
        return current_state[0] == self.goal_state[0]

    # Step 3: Successor Function
    # Generates all valid next states

    def successor(self, state):
        x, y = state
        successors = []

        # Fill Jug1
        successors.append((self.jug1_capacity, y))
        # Fill Jug2
        successors.append((x, self.jug2_capacity))
        # Empty Jug1
        successors.append((0, y))
        # Empty Jug2
        successors.append((x, 0))
        # Pour Jug1 -> Jug2
        transfer = min(x, self.jug2_capacity - y)
        successors.append((x - transfer, y + transfer))
        # Pour Jug2 -> Jug1
        transfer = min(y, self.jug1_capacity - x)
        successors.append((x + transfer, y - transfer))

        return successors


# Step 4: Function to generate solution path
def generate_path(CLOSED, goal_state):
    path = []
    while goal_state is not None:
        path.append(goal_state)
        goal_state = CLOSED[goal_state]
    path.reverse()
    return path


# Step 5: BFS Algorithm

def bfs(problem):
    OPEN = deque()      # Queue for BFS
    CLOSED = {}         # Dictionary to store state:parent

    OPEN.append(problem.initial_state)
    CLOSED[problem.initial_state] = None

    while OPEN:
        current = OPEN.popleft()

        # Check if goal reached
        if problem.goalTest(current):
            return generate_path(CLOSED, current)

        # Expand node
        for child in problem.successor(current):
            if child not in CLOSED:
                OPEN.append(child)
                CLOSED[child] = current

    return None


# Step 6: Main Execution
if __name__ == "__main__":
    problem = WaterJug((4, 0), (2, None))

    print("BFS: Successors of initial state (4,0):")
    print(problem.successor((4, 0)))

    print("\nBFS Solution Path:")
    bfs_path = bfs(problem)
    for state in bfs_path:
        print(state)
