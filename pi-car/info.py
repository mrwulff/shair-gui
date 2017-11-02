# -*- coding: utf-8 -*-
import shairportdecoder.decoder

__author__ = 'luckydonald'

from luckydonaldUtils.logger import logging  # pip install luckydonald-utils
logger = logging.getLogger(__name__)

from shairportdecoder.decoder import Processor
from shairportdecoder.metadata import Infos
from shairportdecoder import decoder

import sys  # launch arguments
import random





def main(argv):
        if argv is None or not argv:
                argv = sys.argv[1:]
        if len(argv) > 0 and argv[0]:
                filename = argv[0]
        else:
                filename = "/tmp/shairport-sync-metadata"
        processor = Processor()
        processor.add_listener(event_processor)  # function `event_processor` defined bellow.
        processor.parse(filename)  # this will probably* run forever. (* If it doesn't crash, lol)

#end def main



def event_processor(event_type, info):


        #print random.randint(1,100)
        assert(isinstance(info, Infos))
        if event_type == decoder.META:
                
                aa=open('data.txt','w')
                bb=info.itemname+"###"
                cc=info.songartist+"###"
                dd=info.songalbum+"###"
                ee=str(info.playstate)+"###"
                aa.write(bb+cc+dd+ee)


# after all needed functions
if __name__ == "__main__":  # if this file is executed directly.
	main([])
