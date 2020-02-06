"""
Unit-test for ISS Tracking class
"""
from ..src.iss_tracking import ISSTracking

iss_object = ISSTracking()

def test_iss_location():
    location = iss_object.get_iss_location()
    assert location

def test_pass_time():
    latitiude = 20
    longitud e= 30
    pass_time = iss_object.get_pass_times()
    assert pass_time

def test_ppl_in_space():
    num_ppl_in_space = iss_object.get_ppl_in_space()
    assert num_ppl_in_space
