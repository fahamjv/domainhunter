#!/usr/bin/env python3
import argparse
import requests
import csv
import time
import os
import re
from os.path import join, dirname
from dotenv import load_dotenv
import datetime

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
PROXYURL = os.environ.get("PROXYURL")
SLEEPTIME = os.environ.get("SLEEPTIME")


def is_valid_file(parser, arg):
    if not os.path.exists(arg):
        parser.error("The file %s does not exist!" % arg)
    else:
        return open(arg, 'r')


def send_request(domain):
    if PROXYURL:
        url = "%shttp://whois.nic.ir/?name=%s" % (PROXYURL, domain)
    else:
        url = "http://whois.nic.ir/?name=%s" % domain

    return requests.get(url).text


def is_domain_available(domain):
    try:
        response = send_request(domain)

        if "ERROR:101: no entries found" in response:
            return True
        else:
            return False
    except:
        return None


def is_domain_valid(domain):
    regex = "^((?!-)[A-Za-z0-9-]" + "{1,63}(?<!-)\\.)" + "ir$"
    p = re.compile(regex)

    if(re.search(p, domain)):
        return True
    else:
        return False


def save_result(domain, is_domain_available, filename):
    filename = filename if filename else "out.csv"
    f = open(filename, 'a')
    headers = ['domain', 'is_domain_available', 'datetime']
    writer = csv.DictWriter(f, delimiter=',', lineterminator='\n',fieldnames=headers)

    if f.tell() == 0:
        writer.writeheader()

    writer.writerow({
        'domain': domain,
        'is_domain_available': is_domain_available,
        'datetime': datetime.datetime.now()
    })

    print("saved %s status." % domain)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', dest="csvfile_in", metavar="",
        type=lambda x: is_valid_file(parser, x), help='Input the CSV file that contains domains', required=True)
    parser.add_argument('-o', '--output', dest="csvfile_out", metavar="", help='Output the results into a CSV file')
    args = parser.parse_args()

    reader = csv.reader(args.csvfile_in)

    for row in reader:
        try:
            domain = row[0]
            if not is_domain_valid(domain):
                print("the %s domain is not valid." % domain)
                continue

            save_result(domain, is_domain_available(domain), filename=args.csvfile_out)

            if SLEEPTIME:
                time.sleep(int(SLEEPTIME))

        except Exception as e:
            print("the %s domain is not valid." % row, e)
