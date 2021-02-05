#!/usr/bin/env python
# -*- coding utf-8 -*-
#
# Copyright 2016 Akshay Raj Gollahalli

import dns.resolver


def get_records(domain):
    """
    Get all the records associated to domain parameter.
    :param domain: 
    :return: 
    """
    ids = [
        'A',
        'NS',
        'MD',
        'MF',
        'CNAME',
        'SOA',
        'MB',
        'MG',
        'MR',
        'NULL',
        'WKS',
        'PTR',
        'HINFO',
        'MINFO',
        'MX',
        'TXT',
        'RP',
        'AFSDB',
        'X25',
        'ISDN',
        'RT',
        'NSAP',
        'NSAP-PTR',
        'SIG',
        'KEY',
        'PX',
        'GPOS',
        'AAAA',
        'LOC',
        'NXT',
        'SRV',
        'NAPTR',
        'KX',
        'CERT',
        'A6',
        'DNAME',
        'OPT',
        'APL',
        'DS',
        'SSHFP',
        'IPSECKEY',
        'RRSIG',
        'NSEC',
        'DNSKEY',
        'DHCID',
        'NSEC3',
        'NSEC3PARAM',
        'TLSA',
        'HIP',
        'CDS',
        'CDNSKEY',
        'CSYNC',
        'SPF',
        'UNSPEC',
        'EUI48',
        'EUI64',
        'TKEY',
        'TSIG',
        'IXFR',
        'AXFR',
        'MAILB',
        'MAILA',
        'ANY',
        'URI',
        'CAA',
        'TA',
        'DLV',
    ]
    
    for a in ids:
        try:
            answers = dns.resolver.query(domain, a)
            for rdata in answers:
                print(a, ':', rdata.to_text())
                return a
            
        except Exception as e:
            print(e)  # or pass
    return "NA"

if __name__ == '__main__':
    a = open("unique.txt", "r") # For checking DNS while other one runs
    b = open("valid.txt", "w") # For the shorter valid types
    c = open("invalid.txt", "w") # For the shorter invalid types
    lines = a.readlines()
    for line in lines:
        ans = get_records(line)
        if (ans == "NA"):
            c.write(line)
        else:
            b.write(line)
    a.close()
    b.close()
    c.close()
    
