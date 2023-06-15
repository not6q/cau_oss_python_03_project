"""
parking_spot module
"""
class parking_spot:
    # you have to implement 'constructor(생성자)' and 'get' method
    __item = {}
    def __str__(self):
        # formats a __item variable to be print()'ed
        item = self.__item
        s  = f"[{item['name']}({item['ptype']})] "
        s += f"{item['city']} {item['district']}"
        s += f"(lat:{item['latitude']}, long:{item['longitude']})"
        return s

    def __init__(self, name, city, district, ptype, longitude, latitude):
        """ A constructor; set the item properties for each parking_spot instance
        Args:
            name (str): name of the parking spot
            city (str): name of the city where the parking slot is located
            district (str): name of the district where the parking slot is located
            ptype (str): type of the parking spot
            longitude (float): longitude of the parking spot's location
            latitude (float): latitude of the parking spot's location
        """
        self.__item = {'name': name, 'city': city, 'district': district, \
                    'ptype': ptype, 'longitude': float(longitude), 'latitude': float(latitude)}

    def get(self, keyword='name'):
        """ getter; returns __item[keyword] if the key exists in the __item dictionary
        Args:
            keyword (str): dictionary's key
        Returns:
            str or float: dictionary's element value that matches to the key
        """
        return self.__item[keyword]

def str_list_to_class_list(str_list):
    """ Converts a list of CSV-formatted strings to a list of parking_spot instances
    Args:
        str_list (str[]): list of CSV-formatted strings.
    Returns:
        A list of parking_spot instances, generated from the given str_list.
    """
    inst_lists = []
    for i in str_list:
        i = i.split(',')
        inst_lists.append(parking_spot(i[1], i[2], i[3], i[4], i[5], i[6]))

    return inst_lists

def print_spots(spots):
    """ Print spots.
    Args:
        spots (parking_spot[]): list consisted of parking_spot instances.
    """
    print('---print elements(%d)---' % len(spots))
    for i in spots:
        print(i)

def filter_by_name(spots, name):
    """ Filters the list of parking_spot, by checking if the given name is included in the spot's name
        and returns new filtered list.
    Args:
        spots (parking_spot[]): list consisted of parking_spot instances.
        name (str): string to be used to filter
    Returns:
        parking_spot[]: list of filtered parking_spot.
    """
    return [i for i in spots if name in i.get('name')]

def filter_by_city(spots, city):
    """ Filters the list of parking_spot, by checking if the given city string is
        included in the spot's "city" field, and returns new filtered list.
    Args:
        spots (parking_spot[]): list consisted of parking_spot instances.
        city (str): string to be used to filter
    Returns:
        parking_spot[]: list of filtered parking_spot.
    """
    return [i for i in spots if city in i.get('city')]

def filter_by_district(spots, district):
    """ Filters the list of parking_spot, by checking if the given district string is
        included in the spot's "district" field, and returns new filtered list.
    Args:
        spots (parking_spot[]): list consisted of parking_spot instances.
        district (str): string to be used to filter
    Returns:
        parking_spot[]: list of filtered parking_spot.
    """
    return [i for i in spots if district in i.get('district')]

def filter_by_ptype(spots, ptype):
    """ Filters the list of parking_spot, by checking if the given ptype string is
        included in the spot's "ptype" field, and returns new filtered list.
    Args:
        spots (parking_spot[]): list consisted of parking_spot instances.
        ptype (str): string to be used to filter
    Returns:
        parking_spot[]: list of filtered parking_spot.
    """
    return [i for i in spots if ptype in i.get('ptype')]

def filter_by_location(spots, location):
    """ Filters the list of parking_spot, by checking if the parking_spot is located
        within the given lat/lon range
    Args:
        spots (parking_spot[]): list consisted of parking_spot instances.
        location (float[]): tuple consisted of min_lat, max_lat, min_lon, max_lon
    Returns:
        parking_spot[]: list of filtered parking_spot.
    """
    return [i for i in spots if i.get('latitude') > location[0] and i.get('latitude') < location[1] \
            and i.get('longitude') > location[2] and i.get('longitude') < location[3]]

# 각 단계별로 테스트 (테스트할때 주석해제 후 사용)
if __name__ == '__main__':
    print("Testing the module...")
    # version#2
    import file_manager
    str_list = file_manager.read_file("./input/free_parking_spot_seoul.csv")
    spots = str_list_to_class_list(str_list)
    print_spots(spots)

    # version#3
    spots = filter_by_district(spots, '동작')
    print_spots(spots)
    
    # version#4
    # spots = sort_by_keyword(spots, 'name')
    # print_spots(spots)