def near(string1, string2):
    if len(string1) -1 == len(string2) and string1[0] == string2[0]:
        for char in string2:
            if char in list(string1):
                print(True)
                break
            else:
                print(False)
                break
    else:
        print(False)

near("reset", "rest")
near("dragoon", "dragon")
near("eave", "leave")
near("sleet", "lets")
