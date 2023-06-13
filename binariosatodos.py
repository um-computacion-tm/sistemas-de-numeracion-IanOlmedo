def bin2dec(bin):

    bin2 = bin[::-1]

    bina = []

    suma = 0

    for bi in bin2:

        bina.append(bi)

    for i in range(0,len(bin2)):

        if bina[i] != "0":

            suma += (2**i)

    return suma

#binario a hexadecimal
def bin2hex(bin):

    bin = bin[::-1]

    while True:
        if (len(bin)%4) != 0:
            bin += "0"
        else:
            break

    bin = bin[::-1]

    bina = []
    bin3 = ""

    cont = 0

    long = int(len(bin)/4)

    for i in range(0,long):
        for b in bin:
            bin3 += b
            cont += 1
            bin = bin.replace(b,"",1)
            if cont == 4:
                cont = 0
                break
        bina.append(bin3)
        bin3 = ""

    hex = ""

    for i in bina:

        if i == "0000":
            hex += "0"
        elif i == "0001":
            hex += "1"
        elif i == "0010":
            hex += "2" 
        elif i == "0011":
            hex += "3"
        elif i == "0100":
            hex += "4"
        elif i == "0101":
            hex += "5" 
        elif i == "0110":
            hex += "6"
        elif i == "0111":
            hex += "7"
        elif i == "1000":
            hex += "8"
        elif i == "1001":
            hex += "9"
        elif i == "1010":
            hex += "A"
        elif i == "1011":
            hex += "B"
        elif i == "1100":
            hex += "C"
        elif i == "1101":
            hex += "D"
        elif i == "1110":
            hex += "E"
        elif i == "1111":
            hex += "F"  

    return hex

#binario a octal
def bin2oct(bin):

    bin = bin[::-1]

    while True:
        if (len(bin)%3) != 0:
            bin += "0"
        else:
            break

    bin = bin[::-1]

    bina = []
    bin3 = ""

    cont = 0

    long = int(len(bin)/3)

    for i in range(0,long):
        for b in bin:
            bin3 += b
            cont += 1
            bin = bin.replace(b,"",1)
            if cont == 3:
                cont = 0
                break
        bina.append(bin3)
        bin3 = ""

    oct = ""

    for i in bina:

        if i == "000":
            oct += "0"
        elif i == "001":
            oct += "1"
        elif i == "010":
            oct += "2" 
        elif i == "011":
            oct += "3"
        elif i == "100":
            oct += "4"
        elif i == "101":
            oct += "5" 
        elif i == "110":
            oct += "6"
        elif i == "111":
            oct += "7"

    return int(oct)