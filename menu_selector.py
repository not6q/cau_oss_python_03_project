"""
menu_selector module: provides a  menu-selecting functionality
"""
import parking_spot_manager
import file_manager
def start_process(path):
    # initial load process using the file located on the path location
    str_list = file_manager.read_file(path)
    spots = parking_spot_manager.str_list_to_class_list(str_list)
    while True:
        print("---menu---")
        print("[1] print")
        print("[2] filter")
        print("[3] sort")
        print("[4] exit")
        select = int(input('type:'))
        if select == 1:
            # prints parking_spot instance's __str__'ed form
            parking_spot_manager.print_spots(spots)
        elif select == 2:
            print("---filter by---")
            print("[1] name")
            print("[2] city")
            print("[3] district")
            print("[4] ptype")
            print("[5] location")
            select = int(input('type:'))
            if select == 1:
                keyword = input('type name:')
                print("not implemented yet")
                # fill this block
            elif select == 2:
                keyword = input('type city:')
                print("not implemented yet")
                # fill this block
            elif select == 3:
                keyword = input('type district:')
                print("not implemented yet")
                # fill this block
            elif select == 4:
                keyword = input('type ptype:')
                print("not implemented yet")
                # fill this block
            elif select == 5:
                min_lat = float(input('type min lat:'))
                max_lat = float(input('type max lat:'))
                min_lon = float(input('type min long:'))
                max_lon = float(input('type max long:'))
                print("not implemented yet")
                # fill this block
            else:
                print("invalid input")
        elif select == 3:
            keywords = ['name', 'city', 'district', 'ptype', 'latitude', 'longitude']
            print("---sort by---")
            print(keywords)
            keyword = input('type keyword:')
            if keyword in keywords:
                print("not implemented yet")
                # fill this block
            else: print("invalid input")
        elif select == 4:
            # exits the program
            print("Exit")
            break
        else:
            print("invalid input")