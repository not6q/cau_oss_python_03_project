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
                # filter by name option
                keyword = input('type name:')
                spots = parking_spot_manager.filter_by_name(spots, keyword)

            elif select == 2:
                # filter by city option
                keyword = input('type city:')
                spots = parking_spot_manager.filter_by_city(spots, keyword)

            elif select == 3:
                # filter by district option
                keyword = input('type district:')
                spots = parking_spot_manager.filter_by_district(spots, keyword)

            elif select == 4:
                # filter by ptype option
                keyword = input('type ptype:')
                spots = parking_spot_manager.filter_by_ptype(spots, keyword)
                
            elif select == 5:
                # filter by location option
                min_lat = float(input('type min lat:'))
                max_lat = float(input('type max lat:'))
                min_lon = float(input('type min long:'))
                max_lon = float(input('type max long:'))
                spots = parking_spot_manager.filter_by_location(spots, (min_lat, max_lat, min_lon, max_lon))

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