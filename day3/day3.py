import fileinput

ORIGIN = (0, 0)


def main():
    line_paths = [paths.split(",") for paths in fileinput.input()]
    lines = [map_line(line_path) for line_path in line_paths]

    print(lines)


def map_line(line_path):
    origin_point = ORIGIN
    line = []

    for path in line_path:
        if path[0] == "U":
            new_point = (origin_point[0], origin_point[1] + int(path[1:]))
            line.append((origin_point, new_point))
            origin_point = new_point
        elif path[0] == "D":
            new_point = (origin_point[0], origin_point[1] - int(path[1:]))
            line.append((origin_point, new_point))
            origin_point = new_point
        elif path[0] == "L":
            new_point = (origin_point[0] - int(path[1:]), origin_point[1])
            line.append((origin_point, new_point))
            origin_point = new_point
        elif path[0] == "R":
            new_point = (origin_point[0] + int(path[1:]), origin_point[1])
            line.append((origin_point, new_point))
            origin_point = new_point
        else:
            raise Exception("wut")

    return line


if __name__ == "__main__":
    # execute only if run as a script
    main()
