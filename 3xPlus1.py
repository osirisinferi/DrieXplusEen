from sys import exit


def collatz(number, round):
    if number == 1:
        return 1
    elif (number % 2) > 0:
        result = 3 * number + 1
    else:
        result = int(number / 2)
    print("Ronde: {}, oude getal: {}, nieuwe getal: {}".format(round, number, result))
    return result, round+1


def main():
    getal = None
    start = 1

    try:
        getal = int(input("Vul begin-getal in: "))
    except ValueError:
        print("Oeps, graag een positief heel getal boven 0 invullen.")
        exit(1)

    while getal != 1:
        getal, start = collatz(getal, start)


if __name__ == "__main__":
    main()
