# -------------------------------
# Booth's Algorithm in Python
# -------------------------------

def booths_algorithm():
    multiplicand_dec = getInput("Multiplicand")
    multiplier_dec = getInput("Multiplier")

    multiplicand_bin = convertDec(multiplicand_dec)
    multiplier_bin = convertDec(multiplier_dec)

    boothsTriumph(multiplicand_bin, multiplier_bin)

    print("\nDecimal Result:", int(multiplier_dec) * int(multiplicand_dec))


def boothsTriumph(mcand, plier):
    print("\nMultiplicand:", mcand)
    print("Multiplier  :", plier)

    product = "00000000" + plier + "0"

    print("Initial Product:", product)
    print(buildLine(0, mcand, product))

    for i in range(1, 9):
        operation = product[-2:]
        product = perform_operation(product, mcand, operation)
        print(buildLine(i, mcand, product))

    product = shift(product)
    product = product[9:17]

    print("\nFinal Binary Product:", product)


def perform_operation(product, mcand, operation):

    if operation == "00":
        product = shift(product)
        print("No Operation")

    elif operation == "01":
        temp = binAdd(product[:8], mcand)
        product = temp + product[8:]
        product = shift(product)
        print("Addition")

    elif operation == "10":
        product = subtraction(product, mcand)
        product = shift(product)
        print("Subtraction")

    elif operation == "11":
        product = shift(product)
        print("No Operation")

    return product


def subtraction(product, mcand):

    carry = 0
    prime_product = product[:8]
    final_product = ""

    for i in range(len(prime_product) - 1, -1, -1):

        if mcand[i] == "0" and prime_product[i] == "0":
            if carry == 1:
                final_product = "1" + final_product
            else:
                final_product = "0" + final_product

        elif mcand[i] == "1" and prime_product[i] == "0":
            if carry == 1:
                final_product = "0" + final_product
            else:
                final_product = "1" + final_product
            carry = 1

        elif mcand[i] == "0" and prime_product[i] == "1":
            if carry == 1:
                final_product = "0" + final_product
                carry = 0
            else:
                final_product = "1" + final_product

        elif mcand[i] == "1" and prime_product[i] == "1":
            if carry == 1:
                final_product = "1" + final_product
                carry = 1
            else:
                final_product = "0" + final_product

    return final_product + product[8:]


def shift(product):
    return "0" + product[:-1]


def binAdd(num1, num2):

    result = ""
    carry = "0"

    for i in range(len(num1) - 1, -1, -1):

        if carry == "0":

            if num1[i] == "0" and num2[i] == "0":
                result = "0" + result

            elif num1[i] == "1" and num2[i] == "1":
                result = "0" + result
                carry = "1"

            else:
                result = "1" + result

        else:

            if num1[i] == "0" and num2[i] == "0":
                result = "1" + result
                carry = "0"

            elif num1[i] == "1" and num2[i] == "1":
                result = "1" + result
                carry = "1"

            else:
                result = "0" + result
                carry = "1"

    return result


def buildLine(iteration, mcand, product):

    return (
        f"Step {iteration} | "
        f"Multiplicand: {mcand} | "
        f"{product[:8]} | {product[8:16]} | {product[16]}"
    )


def convertDec(dec):

    if int(dec) < 0:
        binary = twos_complement(int(dec))
    else:
        binary = format(int(dec), "b")

    binary = binary.zfill(8)

    return binary


def getInput(name):

    value = input(f"Please enter your {name}: ")

    while int(value) > 127 or int(value) < -128:
        print("Value must be between -128 and 127.")
        value = input(f"Please enter your {name}: ")

    return value


def twos_complement(dec):

    adjusted = abs(dec + 1)

    binary = format(adjusted, "b")

    flipped = flip(binary)

    while len(flipped) < 8:
        flipped = "1" + flipped

    return flipped


def flip(bits):

    result = ""

    for bit in bits:
        if bit == "1":
            result += "0"
        else:
            result += "1"

    return result


# -------------------------------
# Main Program
# -------------------------------
booths_algorithm()