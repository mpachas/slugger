# coding: utf8

# FIXME: it'd be really nice to have some additional tests here
from slugger import Slugger


def test_simple_slug():
    s = Slugger('de', hanlang='ja')

    assert s.sluggify('Hellö & Wörld 漢字') == 'helloe-und-woerld-kanji'
    assert s.sluggify('And they lived happily ever after!') == \
        'and-they-lived-happily-ever-after'
