<h3 align="center">
    <a href="https://github.com/umpirsky">
        <img src="https://farm2.staticflickr.com/1709/25098526884_ae4d50465f_o_d.png" />
    </a>
</h3>
<p align="center">
  <a href="https://github.com/umpirsky/Symfony-Upgrade-Fixer">symfony upgrade fixer</a> &bull;
  <a href="https://github.com/umpirsky/Twig-Gettext-Extractor">twig gettext extractor</a> &bull;
  <a href="https://github.com/umpirsky/wisdom">wisdom</a> &bull;
  <a href="https://github.com/umpirsky/centipede">centipede</a> &bull;
  <a href="https://github.com/umpirsky/PermissionsHandler">permissions handler</a> &bull;
  <a href="https://github.com/umpirsky/Extraload">extraload</a> &bull;
  <a href="https://github.com/umpirsky/Gravatar">gravatar</a> &bull;
  <a href="https://github.com/umpirsky/locurro">locurro</a> &bull;
  <a href="https://github.com/umpirsky/country-list">country list</a> &bull;
  <a href="https://github.com/umpirsky/Transliterator">transliterator</a>
</p>

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
