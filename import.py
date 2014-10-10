#!/usr/bin/python

import sys
import getpass
import urllib2
from xml.etree import ElementTree

if 3 != len(sys.argv):
    sys.exit('Please provide TuneIn username and password.')

path = '/home/' + getpass.getuser() + '/.local/share/rhythmbox/rhythmdb.xml'
url = 'http://opml.radiotime.com/Browse.ashx?c=presets&partnerId=k2YHnXyS&username=' + sys.argv[1] + '&password=' + sys.argv[2]

xml = urllib2.urlopen(url).read()

tree = ElementTree.fromstring(xml)
rhythmdb = ElementTree.parse(path)

for child in tree.find('body').findall('outline'):
    entry = ElementTree.Element('entry', {'type': 'iradio'})

    title = ElementTree.Element('title')
    if -1 == child.get('text').find('|'):
        title.text = child.get('text')
    else:
        title.text = child.get('text').split('|')[1].split('(')[0].strip()
    entry.append(title)
    genre = ElementTree.Element('genre')
    genre.text = 'TuneIn'
    entry.append(genre)
    location = ElementTree.Element('location')
    location.text = urllib2.urlopen(child.get('URL')).read().splitlines()[0]
    entry.append(location)

    rhythmdb.getroot().append(entry)

rhythmdb.write(path)
