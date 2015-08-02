#-*-coding:utf-8 -*-
__author__ = 'hy'

from django import template
from datetime import datetime, timedelta, date
register = template.Library()

@register.filter
def pubdatefilfer(akey):
    # anow=datetime.now()
    # print type(key)
    # print(key)
    # print type(anow)
    # print anow
    #
    # return key
    key=akey.replace(tzinfo=None)
    timelist=['一年前','一月前','一周前','一天前','一小时前','一分钟前','刚刚']
    anow=datetime.now().replace(tzinfo=None)
    aweek=timedelta(weeks=1)
    # if anow>key:
    #     # return True
    if anow>key:
        if anow.year>key.year:
            return timelist[0]
        elif anow.month>key.month:
            return timelist[1]
        elif anow>key+aweek:
            return timelist[2]
        elif anow.date>key.date:
            return timelist[3]
        elif anow.hour>key.hour:
            return timelist[4]
        elif anow.minute>key.minute:
            return timelist[5]
        else:
            return timelist[6]
    else:
        return '你穿越啦! '

