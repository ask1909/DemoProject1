class Locators:
    """
    Class containing locators from different pages that are being accessed.
    """
    # FindHotel Locators

    popup_xpath = './/div[@class="autopop__wrap makeFlex column defaultCursor"]'
    login_menu_xpath = './/li[@class="makeFlex hrtlCenter font10 makeRelative lhUser userLoggedOut"]'
    city_label_xpath = './/label[@for="city"]'
    city_value_xpath = city_label_xpath + '/input'
    # city_textbox_xpath = './/div[@class="react-autosuggest__container react-autosuggest__container--open"]/input'
    city_textbox_xpath = city_label_xpath + '/following-sibling::div//child::input'
    suggestion_li_xpath = './/li[@id="react-autowhatever-1-section-0-item-0"]/div/div/div/p[1]'
    search_button_xpath = '.// button[ @ id = "hsw_search_button"]'
    rooms_guests_xpath = './/div[@class="hsw_inputBox roomGuests  "]'
    guests_number_xpath = './/ul[@class="guestCounter font12 darkText"][1]/li'
    children_number_xpath = './/ul[@class="guestCounter font12 darkText"][2]/li'
    apply_button_xpath = './/button[@class="primaryBtn btnApply"]'
    travel_for_xpath = './/div[@class="hsw_inputBox travelFor  "]'
    travel_reason_option_xpath = './/ul[@class="travelForPopup"]/li'
    autosearch_options_div_xpath = './/ul[@class="react-autosuggest__suggestions-list"]/li'
    autosearch_options_xpath = './/p[@class="locusLabel appendBottom5"]'
    autosearch_noopt_xpath = './/div[@class="cantFindYouText appendBottom20 noSuggesstions"]'
    guest_number_error_xpath = './/p[@class="redText font11"]'
    child_age_error_xpath = './/p[@class="redText font11 appendBottom10"]'
    selected_travel_reason = './/div[@class="font30 code latoBlack lineHeight36 blackText makeRelative"]/p'
    date_month_body_xpath = './/div[@class="DayPicker-Month"][1]//div[@class="DayPicker-Body"]'
    date_month_body_weeks_xpath = './/div[@class="DayPicker-Week"]'
    today_xpath = './/div[@class="DayPicker-Day DayPicker-Day--today"]'
    past_days_xpath = './/div[@class="DayPicker-Day DayPicker-Day--disabled"]'
    selected_start_day_xpath = './/div[@class="DayPicker-Day DayPicker-Day--start DayPicker-Day--selected"]'
    selected_end_day_xpath = './/div[@class="DayPicker-Day DayPicker-Day--end DayPicker-Day--selected"]'
    future_days_xpath = './/div[@class="DayPicker-Day"]'
    day_xpath = './/div[@role="gridcell"]'
    label_checkin = './/label[@for="checkin"]'
    checkout_header_xpath = './/span[@class="selectedDateField appendBottom8 pointer" and @data-cy="selectCheckOutDate"]'
    child_age_select_xpath = './/select[@class="ageSelectBox"]'
    prev_month_arrow_xpath = './/span[@class="DayPicker-NavButton DayPicker-NavButton--prev"]'
    next_month_arrow_xpath = './/span[@class="DayPicker-NavButton DayPicker-NavButton--next"]'
    current_month_xpath = './/div[@class="DayPicker-Caption"][1]//child::div'
    future_month_xpath = './/div[@class="DayPicker-Caption"]//child::div'
    search_result_end = './/p[@class="appendTop20 appendBottom20 font22 latoBlack blackText textCenter"]'

    # constants used in method FindHotel::check_past_day_click()
    elem_class_attrib = 'class'
    elem_disable_attrib = 'aria-disabled'
    elem_class_outside = 'outside'
    elem_class_disable = 'disable'
    elem_class_future_day = 'DayPicker-Day'
    elem_class_today = 'today'
    elem_class_day_start = 'Day--start'
    elem_class_day_end = 'Day--end'

    # Menu item XPath with name
    mmt_menu = {
        'My Trip': './/li[@class="makeFlex hrtlCenter lhMyTrips"]',
        '24X7 Support': './/li[@class="makeFlex hrtlCenter lhSupport"]',
        'Wallet': './/li[@class="makeFlex hrtlCenter lhMyWallet"]',
        'My Biz': './/li[@class="makeFlex perfectCenter makeRelative myBizIntro"]',
        'Login Account': './/li[@class="makeFlex hrtlCenter font10 makeRelative lhUser userLoggedOut"]',
        'Country': './/li[@class="makeFlex column font10 makeRelative"][1]',
        'Language': './/li[@class="makeFlex column font10 makeRelative whiteText"]',
        'Currency': './/li[@class="makeFlex column font10 makeRelative"][2]'
    }

    # Locators for Result page
    data_div_xpath = './/div[@class="infinite-scroll-component "]'
    hotels_detail_xpath = '//div[@class="makeFlex flexOne padding20 relative lftCol"]'
    # hotel_rate_details_xpath = './/div[@class="padding20 makeFlex column"]'
    hotel_rate_details_xpath = './/div[@class="priceDetails textRight"]'
    hotel_name_xpath = './/p[@itemprop="name"]/span[1]'
    hotel_rate_xpath = './/p[@id="hlistpg_hotel_shown_price"]'
    hotel_rating_score_xpath = './/span[@class="sprite mmtIcon"]//following-sibling::span'
    hotel_rating_count_xpath = './/span[@itemprop="reviewCount"]'
    # hotel_facilities_xpath = './/div[@class="appendTop10"]//child::div[@class="makeFlex persuasion "]//child::div'
    hotel_facilities_xpath = './/ul[@class="amenList darkText"]'
    # hotel_feature_xpath = './/div[@class="persuasion pc__inclusionsList"]'
    hotel_feature_xpath = hotel_facilities_xpath + '//following-sibling::p/span[2]'
    # result_count_xpath = './/div[@id="hlistpg_sortby_search"]//child::span[2]'
    hotel_feature2_xpath = './/ul[@class="includes"]'
