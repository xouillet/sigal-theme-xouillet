#! /usr/bin/python

import datetime
import jinja2


def date_reformat(value, format_to):
    return datetime.datetime.strptime(value, "%Y-%m-%d").strftime(format_to)


def is_pano(value):
    try:
        return value['xmpmeta']['RDF']['Description']['UsePanoramaViewer'] == "True"
    except jinja2.exceptions.UndefinedError:
        return False
    except KeyError:
        return False
