def main():
    n, m = [int(i) for i in input().split()]
    visited = []
    for _  in range(n):
        colors = input().split()
        for color in colors:
            if color not in visited:
                visited.append(color)
    if "C" in visited or "Y" in visited or "M" in visited:
        print("#Color")
    else:
        print("#Black&White")


main()