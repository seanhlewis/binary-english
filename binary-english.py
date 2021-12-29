# Simple Binary & English converter by Sean Lewis
# Uses Python's built-in methods

def bi2alpha():
    query = "search"
    while query != "":
        query = input("Please enter binary to translate: ")
        querylist = query.split()
        output = ""
        for i in querylist:
            # Converting to int with base 2
            try:
                working_query = int(i, 2)
            except:
                print("Please enter a valid binary value", end="")
                continue
            # Converting to character
            working_query = chr(working_query)
            # Adding character to output
            output += working_query
        print(output)
    back2main()

def alpha2bi():
    query = "search"
    while query != "":
        query = input("Please enter English to convert to binary: ")
        output = ""
        # Converting to list of unicodes
        querylist = list(map(ord, query))
        for i in querylist:
            # Formatting and adding binary to output
            output += format(i, '08b') + " "
        print(output)
    back2main()

def back2main():
    print("\n\n\n\n\n\n\n\n")
    main()

def main():
    choice = "selection"
    while choice != "":
        choice = input("Enter the number of program to run\n[1] Binary to English converter\n[2] English to Binary converter\n")
        options = {1 : bi2alpha, 2 : alpha2bi}
        try:
            options[int(choice)]()
        except:
            print("Please enter a valid number")
            continue
main()