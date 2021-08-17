from datetime import datetime, timedelta

today = datetime.now()


def get_current_time_stamp():
    return today.strftime('%d%m%Y_%H%M%S')


def get_next_weekend():
    global today
    today = today
    w_today = today.weekday()
    diff = (4 - w_today)
    if diff <= 0:
        diff = diff + 7
    cid = today + timedelta(days=diff)
    # cod = cid + timedelta(days=2)
    # weekend = (cid.strftime('%d %b %y'), cod.strftime('%d %b %y'))
    weekend = (cid.strftime('%d %b %y'))
    return weekend


def get_today_day():
    global today
    return str(today.strftime('%d'))
