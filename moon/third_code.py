def decode_morse(mourse_code):
    splited_code = mourse_code.split(" ")
    splited_code_nospace = [i for i in splited_code if i!=" "]
    print(splited_code_nospace)
    decoded_code = ""

    # wikipediaから探してきた変換表　というかifじゃなくて辞書でいい
    for i in splited_code_nospace:
        if "iI" == i:
            decoded_code = decoded_code + "A"
        elif "Iiii" == i:
            decoded_code = decoded_code + "B"
        elif "IiIi" == i:
            decoded_code = decoded_code + "C"
        elif "Iii" == i:
            decoded_code = decoded_code + "D"
        elif "i" == i:
            decoded_code = decoded_code + "E"
        elif "iiIi" == i:
            decoded_code = decoded_code + "F"
        elif "IIi" == i:
            decoded_code = decoded_code + "G"
        elif "iiii" == i:
            decoded_code = decoded_code + "H"
        elif "ii" == i:
            decoded_code = decoded_code + "I"
        elif "iIII" == i:
            decoded_code = decoded_code + "J"
        elif "IiI" == i:
            decoded_code = decoded_code + "K"
        elif "iIii" == i:
            decoded_code = decoded_code + "L"
        elif "II" == i:
            decoded_code = decoded_code + "M"
        elif "Ii" == i:
            decoded_code = decoded_code + "N"
        elif "III" == i:
            decoded_code = decoded_code + "O"
        elif "iIIi" == i:
            decoded_code = decoded_code + "P"
        elif "IIiI" == i:
            decoded_code = decoded_code + "Q"
        elif "iIi" == i:
            decoded_code = decoded_code + "R"
        elif "iii" == i:
            decoded_code = decoded_code + "S"
        elif "I" == i:
            decoded_code = decoded_code + "T"
        elif "iiI" == i:
            decoded_code = decoded_code + "U"
        elif "iiiI" == i:
            decoded_code = decoded_code + "V"
        elif "iII" == i:
            decoded_code = decoded_code + "W"
        elif "IiiI" == i:
            decoded_code = decoded_code + "X"
        elif "IiII" == i:
            decoded_code = decoded_code + "Y"
        elif "IIii" == i:
            decoded_code = decoded_code + "Z"
    
    return decoded_code

