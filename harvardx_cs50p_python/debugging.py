def main():
    height = int(input("Height: "))
    pyramid(height)

# Hay una linea que me imprime sin # 😕
def pyramid(height):
    for i in range(height):
        # print(i, end=" ") breakpoint
        print('#' * (i + 1)) # estaba multiplicando por 0

if __name__ == "__main__":
    main()