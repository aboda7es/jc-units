#!/usr/bin/env python

import json
import re
import logging
from urllib import urlopen, urlencode


LOG = logging.getLogger(__name__)

api = 'http://www.calcatraz.com/calculator/api?'

def convert(query):
    query = 'c=' + urlencode(query)
    url = api + query
    LOG.debug('opening url: %s', url)
    text = urlopen(url).read().strip()
    value = text.split(' ')[0]
    value = float(value) if '.' in value else int(value)
    return value, text


# def convert_simple(value, src_units, dst_units):
#     in_str = '{}{}>{}'.format(value, src_units, dst_units)
#     return convert(in_str)


if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)-15s %(message)s',
                        level=logging.DEBUG)

    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument('query')
    args = parser.parse_args()
    print convert(args.query)
