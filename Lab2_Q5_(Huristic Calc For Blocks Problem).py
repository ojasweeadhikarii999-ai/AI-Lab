def calculate_heuristic(start, goal):
    score = 0
    
    for i in range(4):
        block = start[i]
        
        # Start support for this block
        start_support = start[:i+1]
        
        # Find where this block is in goal
        goal_index = goal.index(block)
        
        # Goal support for this block
        goal_support = goal[:goal_index+1]
        
        if start_support == goal_support:
            score += len(start_support)
        else:
            score -= goal_index  # number of blocks below it in goal
    
    return score


print("Enter Start state (bottom to top) for 4 blocks:")
start_state = input().split()

print("Enter Goal state (bottom to top) for 4 blocks:")
goal_state = input().split()

h_value = calculate_heuristic(start_state, goal_state)
print("Heuristic value:", h_value)
