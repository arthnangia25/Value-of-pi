# Value of pi= 3.14 3.141592653...
# Program to calulate the value of PI
# Let the user enter a number 'n'
# and print out value PI to the 'n'th digit!


def calcPi(limit):
    """
    To print the value of PI till it is required.
    """

    q, r, t, k, n, l = 1, 0, 1, 1, 3, 3

    decimal = limit
    counter = 0

    while counter != decimal + 1:
            if 4 * q + r - t < n * t:
                    # yield digit
                    yield n
                    # insert period after first digit
                    if counter == 0:
                            yield '.'
                    # end
                    if decimal == counter:
                            print('')
                            break
                    counter += 1
                    nr = 10 * (r - n * t)
                    n = ((10 * (3 * q + r)) // t) - 10 * n
                    q *= 10
                    r = nr
            else:
                    nr = (2 * q + r) * l
                    nn = (q * (7 * k) + 2 + (r * l)) // (t * l)
                    q *= k
                    t *= l
                    l += 2
                    k += 1
                    n = nn
                    r = nr


def main():  

    pi_digits = calcPi(int(input(
        "Enter the number of decimals to calculate to: ")))

    i = 0

    # Prints the output

    for d in pi_digits:
            print(d, end='')
            i += 1
			# Inserts a newline after every 40th number
            if i == 40:
                print("")
                i = 0

if __name__ == '__main__':
    main()
