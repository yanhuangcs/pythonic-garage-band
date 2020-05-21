import json

import pytest

from pythonic_garage_band.garage_band import Musician, Guitarist, Bassist, Drummer, Band


BandData = {"Band Name": "Volcano",
            "Members": [Guitarist("Tom"), Drummer("Robert"), Bassist("Riley")]}


def test_abstract_musician():
    with pytest.raises(TypeError):
        Musician("?", "?")


def test_musician_get_instrument():
    assert Guitarist("Mystery").get_instrument() == "guitar"


def test_guitarist():
    jimi = Guitarist("Jimi Hendrix")
    assert jimi.name == "Jimi Hendrix"
    assert jimi.instrument == "guitar"
    assert jimi.play_solo() == "face melting guitar wailing"
    assert jimi.__repr__() == "This is Guitarist Jimi Hendrix"
    assert jimi.__str__() == "Guitarist Jimi Hendrix"


def test_bassist():
    jaco = Bassist("Jaco Pastorious")
    assert jaco.name == "Jaco Pastorious"
    assert jaco.instrument == "bass"
    assert jaco.play_solo() == "thump, thump"
    assert jaco.__repr__() == "This is Bassist Jaco Pastorious"
    assert jaco.__str__() == "Bassist Jaco Pastorious"


def test_drummer():
    sheila = Drummer("Sheila Escovedo")
    assert sheila.name == "Sheila Escovedo"
    assert sheila.instrument == "drums"
    assert sheila.play_solo() == "boom boom"
    assert sheila.__repr__() == "This is Drummer Sheila Escovedo"
    assert sheila.__str__() == "Drummer Sheila Escovedo"


def test_custom_solo_guitarist():
    jimi = Guitarist("Jimi Hendrix", "wonk wonk")
    assert jimi.name == "Jimi Hendrix"
    assert jimi.instrument == "guitar"
    assert jimi.play_solo() == "wonk wonk"


def test_band_str(some_band):
    assert some_band.__str__() == "Band Nirvana: This is not the last day."


def test_band_repr(some_band):
    assert some_band.__repr__() == "Band Nirvana: You rock."


def test_band_members():
    band = Band.create_from_data(BandData)
    assert band.name == "Volcano"
    assert len(band.members) == len(BandData["Members"])

    for member in band.members:
        assert isinstance(member, Musician)

    assert isinstance(band.members[0], Guitarist)
    assert isinstance(band.members[1], Drummer)
    assert isinstance(band.members[2], Bassist)

    assert band.members[0].name == "Tom"
    assert band.members[1].name == "Robert"
    assert band.members[2].name == "Riley"


def test_instruments(some_band):
    instruments = ["guitar", "bass", "drums"]
    for i, member in enumerate(some_band.members):
        assert member.instrument == instruments[i]


def test_individual_solo(some_band):
    for member in some_band.members:
        if member.instrument == "guitar":
            assert member.play_solo() == "face melting guitar wailing"
        elif member.instrument == "bass":
            assert member.play_solo() == "thump, thump"
        elif member.instrument == "drums":
            assert member.play_solo() == "boom boom"


def test_whole_band_play_solos(some_band):
    solos = some_band.play_solos()
    assert len(solos) == 3
    assert solos[0] == "face melting guitar wailing"
    assert solos[1] == "thump, thump"
    assert solos[2] == "boom boom"


def test_create_bands_from_file():
    with open('pythonic_garage_band/bands.json', 'r') as file:
        bands = json.loads(file.read())

    assert len(bands) == 1

    band = Band.create_from_data(bands[0])

    assert band.name == "Volcano"


@pytest.fixture
def some_band():
    nirvana = Band("Nirvana",
                   [Guitarist("Curt Kobain"), Bassist("Kris, Novoselic"), Drummer("Dave Grohl")])
    return nirvana


def check_equal(list1, list2):
    return len(list1) == len(list2) and sorted(list1) == sorted(list2)
