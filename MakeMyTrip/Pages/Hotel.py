from MakeMyTrip.Resources.Locators import Locators


class Hotel:
    hotel_name_xpath = Locators.hotel_name_xpath
    facilities_offered = Locators.hotel_facilities_xpath
    hotel_rate_xpath = Locators.hotel_rate_xpath

    def __init__(self, hotel_info, rate_info):
        self.hotel_name = hotel_info.find_element_by_xpath(Hotel.hotel_name_xpath).text
        self.facilities = hotel_info.find_elements_by_xpath(Hotel.facilities_offered)
        self.rate_offered = rate_info.find_element_by_xpath(Hotel.hotel_rate_xpath).text
        self.separated_facilities = None

    def get_separate_facilities(self):
        self.separated_facilities = []
        self.separated_facilities.append(self.facilities.pop(0).text)
        if len(self.facilities) > 0:
            facilities = self.facilities[0]
            for facility in str(facilities.text).split('\n'):
                self.separated_facilities.append(facility)

    def display_hotel_info(self):
        self.get_separate_facilities()
        print('Hotel Name: {}\t\tType: {}'.format(self.hotel_name, self.separated_facilities.pop(0)))
        print('Facilities available: ')
        if len(self.separated_facilities) == 0:
            print('No facilities mentioned')
        else:
            for facility in self.separated_facilities:
                print('- {}'.format(facility))
        print('Offer (per night): {}'.format(self.rate_offered))
        print('------------------------------------------')

    def check_facility_wifi(self):
        if len(self.separated_facilities) > 1 and 'Free Wi-Fi' in self.separated_facilities:
            print('Yes! Free Wi-Fi available at {}'.format(self.hotel_name))
        else:
            print('NO! Free Wi-Fi NOT available at {}'.format(self.hotel_name))
        print('')
