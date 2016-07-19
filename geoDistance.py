#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib
from xml.etree.ElementTree import parse
from optparse import OptionParser
from pyproj import Geod

def adr2geo(adr):
    api = "http://www.geocoding.jp/api/?v=1.1&q=%s" % (urllib.quote(adr.encode('utf-8')))
    xml = parse(urllib.urlopen(api)).getroot()

    lat = xml.find('coordinate/lat').text
    lng = xml.find('coordinate/lng').text
    return (float(lat), float(lng))

def get_distance(start, goal):
    # pyprojを使って距離を求める
    q = Geod(ellps='WGS84')
    fa, ba, d = q.inv(start[1],start[0],goal[1],goal[0])
    return d

def cutdown(num):
    # 距離に単位をつけて返す
    val = int(round(num))
    if val < 1000:
        return '%sm' % val
    else:
        km = val * 0.001
        return '%sKm' % round(km, 1)

if __name__ == '__main__':
    usage = "usage: %prog 出発地点 到着地点"
    p = OptionParser(usage=usage)
    (options, args ) = p.parse_args()

    if len(args) != 2:
        p.error( "incorrect number of arguments" )

    fadr = args[0].decode('utf-8')
    fgeo = adr2geo(fadr)
    # print fgeo
    tadr = args[1].decode('utf-8')
    tgeo = adr2geo(tadr)
    # print tgeo

    distance = get_distance(fgeo,tgeo)
    dist_str = cutdown(distance)
    print u'%s から %s まで %s'%(fadr,tadr,dist_str)
