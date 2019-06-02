#!/usr/bin/env python

import argparse
import sys
import os
import ssl
import datetime
from pprint import pprint as pp

def ssl_expires_in(entity, serial_number, remaining, buffer_days=14):
    # if the cert expires in less than two weeks, we should reissue it
    if remaining < datetime.timedelta(days=0):
        # cert has already expired - uhoh!
        print("Cert %s issued to '%s' expired %s days ago!" % (serial_number, entity, remaining.days))
    elif remaining < datetime.timedelta(days=buffer_days):
        # expires sooner than the buffer
        print("Cert %s issued to '%s' is nearly expired - %s more days" % (serial_number, entity, remaining.days))
    else:
        # everything is fine
        print("Cert %s issued to '%s' is valid for %s more days" % (serial_number, entity, remaining.days))

def main():
    ssl_date_fmt = r'%b %d %H:%M:%S %Y %Z'
    #cert_file_name = os.path.join(os.path.dirname(__file__), "testcert.pem")

    parser = argparse.ArgumentParser(description='Parse a certificate and show days left')
    parser.add_argument('-v', '--verbose', action='store_true', help='show full certificate')
    parser.add_argument('cert', nargs='+', help='certifcate file(s)')
    args = parser.parse_args()
    for cert_file_name in args.cert:
        try:
            cert_dict = ssl._ssl._test_decode_cert(cert_file_name)
	    serial = cert_dict['serialNumber']
	    subject = dict(x[0] for x in cert_dict['subject'])
            issued_to = subject['commonName']
	    time_left = datetime.datetime.strptime(cert_dict['notAfter'], ssl_date_fmt) - datetime.datetime.utcnow()
	    if args.verbose:
                pp(cert_dict)
	    ssl_expires_in(issued_to, serial, time_left)

        except Exception as e:
            print("Error decoding certificate: {:}".format(e))


if __name__ == "__main__":
#    print("Python {:s} on {:s}\n".format(sys.version, sys.platform))
    main()
