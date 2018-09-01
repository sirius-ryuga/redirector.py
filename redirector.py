#!/usr/bin/env python
import re
import logging
import json
import sys
from datetime import datetime, date, time

logging.basicConfig(filename='/ext/redirector.log',level=logging.DEBUG)
     
def redirect(link_text):
    with open('/ext/list.json') as f:
        data = json.load(f)
        for key in data:
            result = re.search(key,link_text)
            if result!=None:
                return data.get(key)
    logging.info(datetime.now().strftime( "%Y.%m.%d %H:%M:%S") + " url - " + link_text)

def main():
    request  = sys.stdin.readline()
    while request:
        [ch_id,url,ipaddr,method,user]=request.split()
        logging.debug(datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ': ' + request +'\n')
	response  = ch_id + ' OK'
	redirection = redirect(url)
        if redirection:
            port = ''
            if url.endswith(':443'):
                port = ':443'
            response += ' rewrite-url="' + redirection + port + '"'
        response += '\n'
        sys.stdout.write(response)
        sys.stdout.flush()
        request = sys.stdin.readline()
    
if __name__ == '__main__':
    main()
