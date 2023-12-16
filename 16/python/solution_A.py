def walk(input: list[str], start_pos=[-1, 0], start_dir=1):
    seen = [[[] for _ in input[0]] for _ in input]
    positions = [[start_pos[0], start_pos[1]]]
    directions = [start_dir]
    while len(positions) > 0:
        new_dir = []
        new_pos = []
        for pos, dir in zip(positions, directions):
            # make sure it's not start pos
            if 0 <= pos[0] < len(input[0]) and 0 <= pos[1] < len(input):
                if dir in seen[pos[1]][pos[0]]:
                    continue
                seen[pos[1]][pos[0]].append(dir)
            if dir == 0:
                pos[1] -= 1
            elif dir == 1:
                pos[0] += 1
            elif dir == 2:
                pos[1] += 1
            elif dir == 3:
                pos[0] -= 1
            if not (0 <= pos[0] < len(input[0]) and 0 <= pos[1] < len(input)):
                continue
            c = input[pos[1]][pos[0]]
            if c == "|" and dir in [1, 3]:
                new_dir.append(0)
                new_dir.append(2)
                new_pos.append([pos[0], pos[1]])
                new_pos.append([pos[0], pos[1]])
            elif c == "-" and dir in [0, 2]:
                new_dir.append(1)
                new_dir.append(3)
                new_pos.append([pos[0], pos[1]])
                new_pos.append([pos[0], pos[1]])
            elif c == "\\":
                new_dir.append(3 - dir)
                new_pos.append(pos)
            elif c == "/":
                new_dir.append((1 - dir) % 4)
                new_pos.append(pos)
            else:
                new_dir.append(dir)
                new_pos.append(pos)
        directions = new_dir
        positions = new_pos

    sum_ = 0
    for line in seen:
        for e in line:
            if len(e) > 0:
                sum_ += 1
    return sum_


def part1(input: list[str]) -> int:
    return walk(input)


def part2(input: list[str]) -> int:
    max_ = 0
    for y in range(len(input)):
        max_ = max(max_, walk(input, [-1, y], 1))
        max_ = max(max_, walk(input, [len(input[0]), y], 3))
    for x in range(len(input[0])):
        max_ = max(max_, walk(input, [x, -1], 2))
        max_ = max(max_, walk(input, [x, len(input)], 0))
    return max_


if __name__ == "__main__":
    with open("input.txt", "r") as f:  # your file here
        input = f.read().splitlines()
        print(part1(input))
        print(part2(input))
