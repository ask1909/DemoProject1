from MakeMyTrip.Resources.Driver import *
from ddt import ddt, data
from MakeMyTrip.Resources.Utilities import get_current_time_stamp, get_next_weekend
import HtmlTestRunner
import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
from MakeMyTrip.Pages.FindHotel import FindHotel
from MakeMyTrip.Pages.Result import Result


test_req = os.path.abspath('../Resources/TestConfig.json')
with open(test_req, 'r') as fp:
    test_data = json.load(fp)


@ddt
class SearchHotel(unittest.TestCase):
    url = test_data['url']
    city = test_data['city']
    invalid_city = test_data['invalid_city']

    @classmethod
    def setUpClass(cls):
        cls.driver = BDriver(SearchHotel.url)

    def setUp(self):
        self.find_hotel = FindHotel(self.driver)
        self.result = Result(self.driver)

    def test_01_element_city_visible(self):
        self.find_hotel.close_login_popup()
        self.assertTrue(self.find_hotel.check_elem_visible_city_div())

    def test_02_city_textbox_accessible(self):
        self.assertTrue(self.find_hotel.select_textbox())
        self.assertTrue(self.find_hotel.check_autosearch_option())

    @data('Amboli', 'blah'*5, 'Kanyakumari')
    def test_03_search_valid_city(self, city):
        self.assertTrue(self.find_hotel.check_expected_option_available(city))

    def test_04_search_invalid_city(self):
        self.assertTrue(self.find_hotel.check_invalid_city_name(SearchHotel.invalid_city))

    def test_05_guests_selection(self):
        self.assertTrue(self.find_hotel.enter_room_guests_info())

    def test_06_guest_selection_negative(self):
        self.assertTrue(self.find_hotel.check_guest_selection_negative())

    def test_07_checking_child_age_dropdown_visibility(self):
        self.assertTrue(self.find_hotel.check_child_age_dropdown_visible())

    def test_08_child_age_selection_negative(self):
        self.assertTrue(self.find_hotel.check_guest_selection_child_age_selection_negative())

    def test_09_select_travel_reason(self):
        self.assertTrue(self.find_hotel.select_travel_for_reason())

    def test_10_cancel_travel_reason_modification(self):
        self.assertTrue(self.find_hotel.cancel_travel_reason_change())

    def test_11_checkin_date_validate(self):
        self.assertTrue(self.find_hotel.check_past_day_click())

    def test_12_checkin_date_later_than_checkout_date(self):
        self.assertTrue(self.find_hotel.checkin_date_later_than_checkout_date())

    def test_13_longesst_future_date_supported(self):
        self.assertTrue(self.find_hotel.check_calendar_span())

    @data('My Trip', '24X7 Support', 'Wallet', 'My Biz', 'Login Account')
    def test_14_check_menu_item(self, menu_item):
        self.assertTrue(self.find_hotel.check_element_active(menu_item))

    def test_15_set_filter_criteria_for_hotel_search(self):
        checkin_date = get_next_weekend()
        file_name = test_data['output'] + 'Hotels_in_' + SearchHotel.city + '.json'
        self.assertTrue(self.find_hotel.search_hotel_in_amboli_for_3_adults_for_next_weekend(checkin_date, SearchHotel.city))
        self.assertTrue(self.find_hotel.click_search_button())
        self.assertTrue(self.result.create_hotel_json(file_name))

    def tearDown(self):
        ts = get_current_time_stamp()
        file_name = test_data['output'] + self.id().split('.')[-1] + ts + '.png'
        if hasattr(self, '_outcome'):
            result = self.defaultTestResult()
            self._feedErrorsToResult(result, self._outcome.errors)
            if len(result.failures) > 0:
                self.driver.save_screenshot(file_name)
                file_path = os.path.abspath(file_name).replace('\\', '/')
                print('Screenshot={}'.format(file_path))

    @classmethod
    def tearDownClass(cls):
        cls.driver.driver_close()


if __name__ == '__main__':
    template = test_data['template_path']
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=test_data['output'], report_title='MakeMyTrip Home Page Tests', template=template))
    # unittest.main()
