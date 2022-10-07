def main():
    msg = input()
    # Loop through each character and compute
    i = 0
    decoded = ""
    while i < len(msg):
        if msg[i] == ".":
            decoded += "0"
        else:
            if msg[i] == "-" and msg[i+1] == ".":
                decoded += "1"
                i += 1
            elif msg[i] == "-" and msg[i+1] == "-":
                decoded += "2"
                i += 1
        i += 1
    print(decoded)


main()