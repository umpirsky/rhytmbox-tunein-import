Rhytmbox Tunein Import
======================

Script to import your radio stations from [TuneIn](http://tunein.com) into [Rhythmbox](https://wiki.gnome.org/Apps/Rhythmbox)

Installation
------------

```
git clone git@github.com:umpirsky/rhytmbox-tunein-import.git
```

Usage
-----

Backup `rhythmdb.xml` just for the case:
```
cp ~/.local/share/rhythmbox/rhythmdb.xml ~/.local/share/rhythmbox/rhythmdb.bak.xml
```

Now import stations by providing your TuneIn credentials:

```
python rhytmbox-tunein-import/import.py <username> <password>
```
