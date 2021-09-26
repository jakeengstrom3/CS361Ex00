f = open('Drivers.txt', 'r')
drivers = f.readlines()


def print_alph():
    sorted_list = []
    
    for curr_driver in drivers:
        if sorted_list == []:
            sorted_list.append(curr_driver)
        else :
            largest = True
            for sorted_driver in sorted_list:
                if get_driver_lname(curr_driver) < get_driver_lname(sorted_driver):
                    sorted_list.insert(sorted_list.index(sorted_driver), curr_driver)
                    largest = False
                    break
            if largest:
                sorted_list.append(curr_driver)

    print(sorted_list)

def print_num():
    sorted_list = []
    
    for curr_driver in drivers:
        if sorted_list == []:
            sorted_list.append(curr_driver)
        else :
            largest = True
            for sorted_driver in sorted_list:
                if get_driver_number(curr_driver) < get_driver_number(sorted_driver):
                    sorted_list.insert(sorted_list.index(sorted_driver), curr_driver)
                    largest = False
                    break
            if largest:
                sorted_list.append(curr_driver)
            
            
        
    print(sorted_list)

def getinput():
    str = input("Enter 'a' to sort alphebetically, or enter n to sort numerically\n")

    if str == "a":
        print_alph()
    elif str == "n":
        print_num()
    else:
        print("Please enter Valid Input\n")
        getinput()

def get_driver_number(driver):
    words = driver.split(' ')
    return int(words[2])

def get_driver_lname(driver):
    words = driver.split(' ')
    return words[1][0]

getinput()
