#! /usr/bin/python

import datetime
import locale

def date_reformat(value, format_to):
    return datetime.datetime.strptime(value, '%Y-%m-%d').strftime(format_to)
