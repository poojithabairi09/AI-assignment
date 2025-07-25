def move_options(state_str):
    moves = []
    tiles = list(state_str)

    for i in range(len(tiles)):
        ch = tiles[i]

        if ch == '_':
            continue

        if ch == 'W':
            # Move right by rabbit
            if i + 1 < len(tiles) and tiles[i + 1] == '_':
                temp = tiles[:]
                temp[i], temp[i + 1] = temp[i + 1], temp[i]
                moves.append(''.join(temp))
            # Jump over one rabbit
            if i + 2 < len(tiles) and tiles[i + 2] == '_' and tiles[i + 1] in ['W', 'E']:
                temp = tiles[:]
                temp[i], temp[i + 2] = temp[i + 2], temp[i]
                moves.append(''.join(temp))

        elif ch == 'E':
            # Move left by 1
            if i - 1 >= 0 and tiles[i - 1] == '_':
                temp = tiles[:]
                temp[i], temp[i - 1] = temp[i - 1], temp[i]
                moves.append(''.join(temp))
            # Jump over one rabbit
            if i - 2 >= 0 and tiles[i - 2] == '_' and tiles[i - 1] in ['W', 'E']:
                temp = tiles[:]
                temp[i], temp[i - 2] = temp[i - 2], temp[i]
                moves.append(''.join(temp))

    return moves

def puzzle_bfs(start, target):
    q = [[start]]
    seen = []

    while q:
        current_path = q[0]
        del q[0]
        latest = current_path[-1]

        if latest == target:
            return current_path

        if latest not in seen:
            seen.append(latest)
            for new_state in move_options(latest):
                if new_state not in seen:
                    q.append(current_path + [new_state])
    return None

# Run the logic
initial = "WWW_EEE"
goal = "EEE_WWW"

result = puzzle_bfs(initial, goal)

if result:
    print("Steps needed:", len(result) - 1)
    for step in result:
        print(step)
else:
    print("No solution available.")

