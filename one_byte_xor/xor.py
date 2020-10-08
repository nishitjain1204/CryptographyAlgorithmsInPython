def main():
    msg = input("enter your msg: ")
    key = int(input("enter one byte key: "))
    enc = ""
    for i in msg:
        enc += chr((ord(i) ^ key) % 0xff)

    print("Your secret msg: " + enc)


if __name__ == "__main__":
    main()