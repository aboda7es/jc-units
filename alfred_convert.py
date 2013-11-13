#!/usr/bin/env python
# coding=UTF-8

import cconvert as convert
import logging
import re
import jcalfred


LOG = logging.getLogger(__name__)


class Workflow(jcalfred.Workflow):
    def __init__(self):
        super(Workflow, self).__init__()
        #self.log_level = 'DEBUG'

    def _convert(self, query):
        try:
            value, text = convert.convert(query)
        except Exception, e:
            if e.message.startswith('Parse error in query'):
                return [jcalfred.Item('Waiting for input...')]
            else:
                try:
                    int(e.message)
                    return [jcalfred.Item('Waiting for input...')]
                except:
                    pass
            raise e

        return [jcalfred.Item(text, arg=str(value), valid=True,
                              subtitle='Action this item to copy %s to the '
                                       'clipboard' % value)]

    def tell_convert_simple(self, query):
        '''Perform a simple conversion query.'''
        LOG.debug('called with query "%s"', query)

        # match things like "1cm in ft"
        match = re.match('(?P<value>\d+(\.\d+)?)\s*(?P<src>[a-zA-Z]+)(\s+\w+)?'
                         '\s+(?P<dst>[a-zA-Z]+)', query.strip())

        if match:
            value = float(match.group('value'))
            src_units = match.group('src').lower()
            dst_units = match.group('dst').lower()
            query = '%s%s in %s' % (value, src_units, dst_units)
            return self._convert(query)

        return [jcalfred.Item('Waiting for input...')]


    # While Calcatraz supports freeform conversions, it is not as extensive as google
    # e.g. you cant multiply units. You can how ever add or substract unit or multiply
    # a unit and a number.
    #
    def tell_convert(self, query):
        '''Perform a general conversion query.'''
        LOG.debug('called with query "%s"', query)

        if len(query) == 0:
            return [
                jcalfred.Item('Perform a freeform conversion'),
            
                jcalfred.Item('Examples', subtitle='1cm * 1in,   '
                              '1cm + 1in  in mm,   7cm * 3 in inches'),
            ]
        else:
            return self._convert(query)


if __name__ == '__main__':
    from sys import argv
    ap = Workflow()
    getattr(ap, argv[1])(*argv[2:])
