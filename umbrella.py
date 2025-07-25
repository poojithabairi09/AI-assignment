
names = ["Amogh", "Ameya", "Grandma", "Grandpa"]
times = [5, 10, 20, 25]

# Store best solution
best_time = [float('inf')]
best_path = []

def crossing_time(group):
    return max(times[i] for i in group)

# Recursive search
def solve(left, right, is_umbrella_left, time_spent, moves):
    global best_time, best_path

    # all on right
    if len(left) == 0:
        if time_spent <= 60 and time_spent < best_time[0]:
            best_time[0] = time_spent
            best_path[:] = moves
        return

    if time_spent >= best_time[0]:
        return

    if is_umbrella_left:
        # Choose 2 to cross right
        for i in range(len(left)):
            for j in range(i+1, len(left)):
                a, b = left[i], left[j]
                t = max(times[a], times[b])
                new_left = [x for x in left if x != a and x != b]
                new_right = right + [a, b]
                move = f"→ {names[a]} & {names[b]} ({t} min)"
                solve(new_left, new_right, False, time_spent + t, moves + [move])
    else:
        # One comes back
        for i in range(len(right)):
            a = right[i]
            t = times[a]
            new_left = left + [a]
            new_right = [x for x in right if x != a]
            move = f"← {names[a]} ({t} min)"
            solve(new_left, new_right, True, time_spent + t, moves + [move])

# Initial state
solve([0, 1, 2, 3], [], True, 0, [])

# Output
if best_path:
    print(f"Solution found in {best_time[0]} minutes:")
    for step in best_path:
        print(step)
else:
    print("No solution found within 60 minutes.")

