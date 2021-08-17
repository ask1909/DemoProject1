from MakeMyTrip.Pages.WebPage import *
from MakeMyTrip.Resources.Locators import Locators
import json


class Result(WebPage):
    data_div_xpath = Locators.data_div_xpath
    hotels_detail_xpath = Locators.hotels_detail_xpath
    hotel_rate_details_xpath = Locators.hotel_rate_details_xpath
    hotel_name_xpath = Locators.hotel_name_xpath
    hotel_rate_xpath = Locators.hotel_rate_xpath
    hotel_rating_score_xpath = Locators.hotel_rating_score_xpath
    hotel_rating_count_xpath = Locators.hotel_rating_count_xpath
    hotel_facilities_xpath = Locators.hotel_facilities_xpath
    search_result_end = Locators.search_result_end
    hotel_feature_xpath = Locators.hotel_feature_xpath
    hotel_feature2_xpath = Locators.hotel_feature2_xpath

    def __init__(self, driver):
        WebPage.__init__(self, driver)
        self.raw_data = None
        self.hotels_info = None
        self.hotels_rate = None

    def capture_raw_results(self):
        end_found = False
        while not end_found:
            try:
                elem = self.wait.until(ec.visibility_of_element_located((By.XPATH, Result.search_result_end)))
            except TimeoutException:
                self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
                continue
            else:
                break
        try:
            self.raw_data = self.presence_of_required_element(By.XPATH, Result.data_div_xpath)
            return True
        except Exception as e:
            print('Failed to capture all hotels details', e)
            return False

    def extract_hotels_info(self):
        try:
            self.hotels_info = self.raw_data.find_elements_by_xpath(Result.hotels_detail_xpath)
            return True
        except Exception as e:
            print('Failed to capture hotel details', e)
            return False

    def extract_hotels_rate(self):
        try:
            self.hotels_rate = self.raw_data.find_elements_by_xpath(Result.hotel_rate_details_xpath)
            return True
        except Exception as e:
            print('Failed to extract hotel rate details', e)
            return False

    def create_hotel_json(self, file_name):
        result = True
        hotels_list = []
        self.capture_raw_results()
        self.extract_hotels_info()
        self.extract_hotels_rate()
        for hotel, rate in zip(self.hotels_info, self.hotels_rate):
            dir_hotel = {}
            try:
                hotel_name = hotel.find_element_by_xpath(Result.hotel_name_xpath)
            except Exception as e:
                dir_hotel['Name'] = 'Not Available'
                pass
            else:
                dir_hotel['Name'] = hotel_name.text

            try:
                hotel_rating = hotel.find_element_by_xpath(Result.hotel_rating_score_xpath)
            except Exception as e:
                dir_hotel['Rating'] = 'Not Available'
                pass
            else:
                dir_hotel['Rating'] = hotel_rating.text

            try:
                hotel_rating_count = hotel.find_element_by_xpath(Result.hotel_rating_count_xpath)
            except Exception as e:
                dir_hotel['Rating Count'] = 'Not Available'
                pass
            else:
                dir_hotel['Rating Count'] = hotel_rating_count.text

            try:
                hotel_facility = hotel.find_element_by_xpath(Result.hotel_facilities_xpath)
            except Exception as e:
                dir_hotel['Facilities'] = 'Not Available'
                pass
            else:
                hotel_facility = str(hotel_facility.text)
                if '\n' in hotel_facility:
                    hotel_facility = hotel_facility.replace('\n', ', ')
                dir_hotel['Facilities'] = hotel_facility

            try:
                hotel_feature = hotel.find_element_by_xpath(Result.hotel_feature_xpath)
            except Exception as e:
                dir_hotel['Features'] = None
                pass
            else:
                dir_hotel['Features'] = hotel_feature.text

            try:
                hotel_feature2 = rate.find_element_by_xpath(Result.hotel_feature2_xpath)
            except Exception as e:
                if dir_hotel['Features'] is None:
                    dir_hotel['Features'] = 'Not available'
                else:
                    pass
            else:
                hotel_feature2 = str(hotel_feature2.text)
                if '\n' in hotel_feature2:
                    hotel_feature2 = hotel_feature2.replace('\n', '')
                if dir_hotel['Features'] is None:
                    dir_hotel['Features'] = hotel_feature2
                else:
                    dir_hotel['Features'] = dir_hotel['Features'] + ', ' + hotel_feature2

            try:
                hotel_offer = rate.find_element_by_xpath(Result.hotel_rate_xpath)
            except Exception as e:
                dir_hotel['Offered Charges'] = 'Not Available'
                pass
            else:
                hotel_offer = str(hotel_offer.text)
                if '\u20b9' in hotel_offer:
                    hotel_offer = hotel_offer.replace('\u20b9', 'Rs.')
                dir_hotel['Offered Charges'] = hotel_offer

            hotels_list.append(dir_hotel)
            del hotel
        if len(hotels_list) < 1:
            result = False
        else:
            with open(file_name, 'w') as fp:
                json.dump(hotels_list, fp, indent=4)
            result = True
        return result
