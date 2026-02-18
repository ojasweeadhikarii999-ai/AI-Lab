import heapq

goal = ((1,2,3),
        (4,5,6),
        (7,8,0))

# Manhattan Distance Heuristic
def heuristic(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0:
                value = state[i][j]
                goal_x = (value-1) // 3
                goal_y = (value-1) % 3
                distance += abs(goal_x - i) + abs(goal_y - j)
    return distance


def get_neighbors(state):
    neighbors = []
    state = [list(row) for row in state]

    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                x, y = i, j

    moves = [(0,1),(1,0),(0,-1),(-1,0)]

    for dx, dy in moves:
        nx, ny = x+dx, y+dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            neighbors.append(tuple(tuple(row) for row in new_state))

    return neighbors


def astar(start):
    open_list = []
    heapq.heappush(open_list, (heuristic(start), 0, start))
    visited = set()

    while open_list:
        f, g, current = heapq.heappop(open_list)

        if current == goal:
            print("Goal Reached!")
            return

        visited.add(current)

        for neighbor in get_neighbors(current):
            if neighbor not in visited:
                heapq.heappush(open_list,
                    (g+1+heuristic(neighbor), g+1, neighbor))


# Example start state
start = ((1,2,3),
         (4,0,6),
         (7,5,8))

astar(start)
