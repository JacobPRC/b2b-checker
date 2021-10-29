def list_lower(arr):
    try:
        return (map(lambda guest: guest.lower(), arr))
    except:
        print("Looks like your list contains non string values. Please update before trying again")


def b2b_checker(list1, list2):
    b2b_guests = []
    lowered_list1 = list_lower(list1)
    lowered_list2 = list_lower(list2)

    for name in lowered_list1:
        name.lower()
        if name in lowered_list2:
            b2b_guests.append(name)

    if b2b_guests == []:
        return print("There are no B2Bs tonight")

    print("Here are your b2bs", b2b_guests)


b2b_checker(["Jcob", "alleya", "Taylor"], ["alanna", "jaCOb", "Taelor"])
