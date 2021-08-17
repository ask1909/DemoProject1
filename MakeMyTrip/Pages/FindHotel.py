from MakeMyTrip.Pages.WebPage import *
from MakeMyTrip.Resources.Locators import Locators
import time


class FindHotel(WebPage):
    popup_xpath = Locators.popup_xpath
    login_menu_xpath = Locators.login_menu_xpath
    city_label_xpath = Locators.city_label_xpath
    city_textbox_xpath = Locators.city_textbox_xpath
    city_value_xpath = Locators.city_value_xpath
    suggestion_li_xpath = Locators.suggestion_li_xpath
    search_button_xpath = Locators.search_button_xpath
    rooms_guests_xpath = Locators.rooms_guests_xpath
    guests_number_xpath = Locators.guests_number_xpath
    apply_button_xpath = Locators.apply_button_xpath
    travel_for_xpath = Locators.travel_for_xpath
    travel_reason_option_xpath = Locators.travel_reason_option_xpath
    autosearch_options_div_xpath = Locators.autosearch_options_div_xpath
    autosearch_options_xpath = Locators.autosearch_options_xpath
    autosearch_noopt_xpath = Locators.autosearch_noopt_xpath
    children_number_xpath = Locators.children_number_xpath
    guest_number_error_xpath = Locators.guest_number_error_xpath
    child_age_error_xpath = Locators.child_age_error_xpath
    selected_travel_reason = Locators.selected_travel_reason
    date_month_body_weeks_xpath = Locators.date_month_body_weeks_xpath
    date_month_body_xpath = Locators.date_month_body_xpath
    today_xpath = Locators.today_xpath
    day_xpath = Locators.day_xpath
    label_checkin = Locators.label_checkin
    past_days_xpath = Locators.past_days_xpath
    selected_start_day_xpath = Locators.selected_start_day_xpath
    # selected_end_day_xpath = Locators.selected_end_day_xpath
    future_days_xpath = Locators.future_days_xpath
    selected_end_day_xpath = Locators.selected_end_day_xpath
    checkout_header_xpath = Locators.checkout_header_xpath
    child_age_select_xpath = Locators.child_age_select_xpath
    prev_month_arrow_xpath = Locators.prev_month_arrow_xpath
    next_month_arrow_xpath = Locators.next_month_arrow_xpath
    current_month_xpath = Locators.current_month_xpath
    future_month_xpath = Locators.future_month_xpath
    elem_class_attrib = Locators.elem_class_attrib
    elem_disable_attrib = Locators.elem_disable_attrib
    elem_class_outside = Locators.elem_class_outside
    elem_class_disable = Locators.elem_class_disable
    elem_class_future_day = Locators.elem_class_future_day
    elem_class_today = Locators.elem_class_today
    elem_class_day_start = Locators.elem_class_day_start
    elem_class_day_end = Locators.elem_class_day_end

    def __init__(self, driver):
        WebPage.__init__(self, driver)
        self.elem_body = self.driver.find_element_by_tag_name('body')

    def close_login_popup(self):
        try:
            self.element_visible_loc(By.XPATH, FindHotel.popup_xpath)
        except TimeoutException:
            # print('Login pop up did not appear')
            pass
        else:
            login_dialog = self.element_clickable(By.XPATH, FindHotel.login_menu_xpath)
            login_dialog.click()
        return True

    def check_elem_visible_city_div(self):
        try:
            self.element_visible_loc(By.XPATH, FindHotel.city_label_xpath)
            return True
        except TimeoutException as e:
            print(e, ' Failed to find component for City/Hotel')
            return False

    def select_textbox(self):
        try:
            self.element_clickable(By.XPATH, FindHotel.city_label_xpath).click()
            return True
        except TimeoutException as e:
            print(e, 'Failed to access component for City/Hotel')
            return False

    def check_visibility_city_textbox(self):
        try:
            self.element_visible_loc(By.XPATH, FindHotel.city_textbox_xpath)
            return True
        except TimeoutException as e:
            print(e, 'Failed to find component textbox provided to enter city')
            return False

    def enter_city(self, city):
        char = ''
        try:
            for c in city:
                char = char + c
                self.element_clickable(By.XPATH, FindHotel.city_textbox_xpath).clear()
                self.element_clickable(By.XPATH, FindHotel.city_textbox_xpath).send_keys(char)
            return True
        except TimeoutException as e:
            print(e, 'Failed to access textbox provided for entering city')
            return False
        # try:
        #     elem_city_text = self.element_clickable(By.XPATH, FindHotel.city_textbox_xpath)
        # except Exception as e:
        #     print(e, 'Failed to find text field for city')
        #     return False
        # for c in city:
        #     try:
        #         elem_city_text.clear()
        #     except TimeoutException as e:
        #         print(e, 'Failed to clear text field')
        #         pass
        #     else:
        #         char = char + c
        #         elem_city_text.send_keys(char)
        # return True

    def check_autosearch_option(self):
        try:
            self.element_visible_loc(By.XPATH, FindHotel.autosearch_options_div_xpath)
            return True
        except TimeoutException as e:
            print(e, 'Failed to find auto-search options')
            return False
        finally:
            self.elem_body.send_keys(Keys.ESCAPE)

    def check_expected_option_available(self, city):
        self.select_textbox()
        self.enter_city(city)
        try:
            if self.wait.until(ec.presence_of_element_located((By.XPATH, FindHotel.autosearch_options_div_xpath))):
                expected_options = self.driver.find_elements_by_xpath(FindHotel.autosearch_options_div_xpath)
        except TimeoutException as e:
            print(e, 'Expected option not found in auto-searched list')
            return False
        else:
            for exp_opt in expected_options:
                if exp_opt.text.startswith(city):
                    exp_opt.click()
                    break
            return True
        finally:
            self.elem_body.send_keys(Keys.ESCAPE)

    def check_invalid_city_name(self, city):
        self.select_textbox()
        self.enter_city(city)
        try:
            self.element_visible_loc(By.XPATH, FindHotel.autosearch_noopt_xpath)
            return True
        except TimeoutException as e:
            print(e, 'Expected option (empty list) not displayed')
            return False
        finally:
            self.elem_body.send_keys(Keys.ESCAPE)

    def enter_room_guests_info(self):
        try:
            self.element_clickable(By.XPATH, FindHotel.rooms_guests_xpath).click()
            guests_number = self.driver.find_elements_by_xpath(FindHotel.guests_number_xpath)
            for gus_num in guests_number:
                if gus_num.text == '4':
                    gus_num.click()
                    break
            # self.element_clickable(By.XPATH, FindHotel.guests_number_xpath).click()
            self.element_clickable(By.XPATH, FindHotel.apply_button_xpath).click()
            return True
        except Exception as e:
            print('Failed to select room/guests options', e)
            return False

    def check_guest_selection_negative(self):
        self.element_clickable(By.XPATH, FindHotel.rooms_guests_xpath).click()
        guests_number = self.driver.find_elements_by_xpath(FindHotel.guests_number_xpath)
        guests_number[-1].click()
        try:
            children_number = self.driver.find_elements_by_xpath(FindHotel.children_number_xpath)
            children_number[-1].click()
            self.element_visible_loc(By.XPATH, FindHotel.guest_number_error_xpath)
            return True
        except TimeoutException as e:
            print(e, 'Failed to display error message')
            return False
        finally:
            self.elem_body.send_keys(Keys.ESCAPE)

    def check_guest_selection_child_age_selection_negative(self):
        self.element_clickable(By.XPATH, FindHotel.rooms_guests_xpath).click()
        children_number = self.driver.find_elements_by_xpath(FindHotel.children_number_xpath)
        children_number[1].click()
        try:
            self.element_clickable(By.XPATH, FindHotel.apply_button_xpath).click()
            self.element_visible_loc(By.XPATH, FindHotel.child_age_error_xpath)
            return True
        except TimeoutException as e:
            print(e, 'Failed to display error message for children age not selected')
            return False
        finally:
            self.elem_body.send_keys(Keys.ESCAPE)

    def check_child_age_dropdown_visible(self):
        self.element_clickable(By.XPATH, FindHotel.rooms_guests_xpath).click()
        children_number = self.driver.find_elements_by_xpath(FindHotel.children_number_xpath)
        children_number[1].click()
        try:
            self.wait.until(ec.visibility_of_element_located((By.XPATH, FindHotel.child_age_select_xpath)))
        except TimeoutException as e:
            print(e, 'Dropdown for child age selection not visible')
            return False
        else:
            self.elem_body.send_keys(Keys.ESCAPE)
            return True

    def select_travel_for_reason(self):
        try:
            self.element_clickable(By.XPATH, FindHotel.travel_for_xpath).click()
            travel_reasons = self.driver.find_elements_by_xpath(FindHotel.travel_reason_option_xpath)
            if travel_reasons[0].text == 'Work' and travel_reasons[1].text == 'Leisure':
                travel_reasons[1].click()
                return True
        except Exception as e:
            print('Failed to select reason of traveling', e)
            return False

    def cancel_travel_reason_change(self):
        prev_selected_reason = self.driver.find_element_by_xpath(FindHotel.selected_travel_reason).text
        self.element_clickable(By.XPATH, FindHotel.travel_for_xpath).click()
        self.elem_body.send_keys(Keys.ESCAPE)
        try:
            cur_selected_reason = self.driver.find_element_by_xpath(FindHotel.selected_travel_reason).text
            if prev_selected_reason == cur_selected_reason:
                return True
        except ValueError as e:
            print(e, 'Selected reason for travel changed')
            return False

    def check_past_day_click(self):
        result = True
        self.wait.until(ec.element_to_be_clickable((By.XPATH, FindHotel.label_checkin))).click()
        month = self.driver.find_element_by_xpath(FindHotel.date_month_body_xpath)
        days_of_month = month.find_elements_by_xpath(FindHotel.day_xpath)
        for day in days_of_month:
            elem_class = str(day.get_attribute(FindHotel.elem_class_attrib))
            elem_aria_disabled = str(day.get_attribute(FindHotel.elem_disable_attrib))
            outside_found = elem_class.find(FindHotel.elem_class_outside)
            if outside_found > 0:
                continue
            disabled_found = elem_class.find(FindHotel.elem_class_disable)
            if disabled_found > 0 and elem_aria_disabled == 'true':
                continue
            elif (elem_class == FindHotel.elem_class_future_day) and elem_aria_disabled == 'false':
                continue
            elif (elem_class.find(FindHotel.elem_class_today) > 0) and elem_aria_disabled == 'false':
                continue
            elif (elem_class.find(FindHotel.elem_class_day_start) > 0) and elem_aria_disabled == 'false':
                continue
            elif (elem_class.find(FindHotel.elem_class_day_end) > 0) and elem_aria_disabled == 'false':
                continue
            else:
                result = False
                break
        self.elem_body.send_keys(Keys.ESCAPE)
        return result

    def checkin_date_later_than_checkout_date(self):
        result = True
        self.wait.until(ec.element_to_be_clickable((By.XPATH, FindHotel.label_checkin))).click()
        days_of_month = self.driver.find_elements_by_xpath(FindHotel.day_xpath)
        for i in range(len(days_of_month)):
            elem_class = days_of_month[i].get_attribute(FindHotel.elem_class_attrib)
            # if elem_class == "DayPicker-Day DayPicker-Day--end DayPicker-Day--selected":
            if FindHotel.elem_class_day_end in elem_class:
                days_of_month[i+1].click()
                break
        checkout_heading = self.wait.until(ec.element_to_be_clickable((By.XPATH, FindHotel.checkout_header_xpath))).text
        if 'Select Checkout Date' != checkout_heading:
            result = False
        self.elem_body.send_keys(Keys.ESCAPE)
        return result

    def check_calendar_span(self):
        result = True
        self.wait.until(ec.element_to_be_clickable((By.XPATH, FindHotel.label_checkin))).click()
        try:
            self.wait.until(ec.visibility_of_element_located((By.XPATH, FindHotel.prev_month_arrow_xpath)))
        except TimeoutException:
            pass
        else:
            print('Allowed to access past months')
            result = False
            return result
        current_date = str(self.driver.find_element_by_xpath(FindHotel.current_month_xpath).text)
        current_month = current_date[:-4]
        current_year = int(current_date[-4:])
        try:
            while self.wait.until(ec.visibility_of_element_located((By.XPATH, FindHotel.next_month_arrow_xpath))):
                self.wait.until(ec.element_to_be_clickable((By.XPATH, FindHotel.next_month_arrow_xpath))).click()
        except TimeoutException:
            pass
        else:
            result = False
            return result
        future_dates = self.driver.find_elements_by_xpath(FindHotel.future_month_xpath)
        future_month = future_dates[1].text[:-4]
        future_year = int(future_dates[1].text[-4:])
        if future_year != (current_year + 1) or future_month != current_month:
            result = False
        self.elem_body.send_keys(Keys.ESCAPE)
        return result

    def check_element_active(self, menu_name):
        elem_xpath = Locators.mmt_menu[menu_name]
        try:
            self.wait.until(ec.visibility_of_element_located((By.XPATH, elem_xpath)))
        except TimeoutException as e:
            print(e, 'Menu item {} not visible'.format(menu_name))
            return False
        else:
            return True

    def search_hotel_in_amboli_for_3_adults_for_next_weekend(self, next_weekend, city):
        result = True
        cid_day = int((next_weekend.split(' '))[0])
        self.check_expected_option_available(city)
        self.wait.until(ec.element_to_be_clickable((By.XPATH, FindHotel.label_checkin))).click()
        days_of_month = self.driver.find_elements_by_xpath(FindHotel.future_days_xpath)
        for i in range(len(days_of_month)):
            if days_of_month[i].text == str(cid_day):
                try:
                    days_of_month[i].click()
                    days_of_month[i+2].click()
                except TimeoutException:
                    result = False
                else:
                    result = True
                finally:
                    break
        return result

    def click_search_button(self):
        try:
            self.element_clickable(By.XPATH, FindHotel.search_button_xpath).click()
            return True
        except Exception as e:
            print(e, 'Failed to click Search button')
            return False
