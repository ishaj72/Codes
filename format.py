def print_formatted(number):
    a_width = len(bin(number)[2:])
    for i in range(1,number+1):
        dec = str(i)
        octa = (oct(i))[2:]
        hexa = ((hex(i))[2:]).upper()
        binary = (bin(i))[2:]
        print((dec).rjust(a_width),(octa).rjust(a_width),(hexa).rjust(a_width),(binary).rjust(a_width))
