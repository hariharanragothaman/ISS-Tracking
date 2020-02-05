import json
import argparse
import requests
import logging

class ISSTracking(object):
    """
    Python Wrapper Class to interact with OpenNotify API
    """
    def __init__(self):
        """
        :brief: Constructor of Class
        :param url: URL of the OpenNotify API
        """
        print("Entering the Constructor")

    def get_iss_location(self):
        """
        : brief: Getter function to get current ISS location
        :return: JSON payload response
        """
        iss_object = requests.get('http://api.open-notify.org/iss-now.json', auth=('user', 'pass'))
        response = iss_object.text
        response_dict = json.loads(response)
        print('The ISS current location at {} is {} {}'.format(response_dict["timestamp"],
                                                               response_dict["iss_position"]["latitude"],
                                                               response_dict["iss_position"]["longitude"]))
        return response

    def get_pass_times(self, latitude, longitude, altitude=None, number=None):
        """
        :brief: Function get overhead passing time of ISS
        :param latitude:   Latitude of the place to predict passes
        :param longitude:  Longitude of the place to predict passes
        :param altitude:   Altitude of the place to predict passes
        :param number:     Number of passes to return
        """
        iss_url = "http://api.open-notify.org/iss-pass.json?lat=" + latitude + "&lon=" + longitude
        iss_object = requests.get(iss_url)
        response = iss_object.text
        return response

if __name__ == "__main__":
    iss = ISSTracking()
    response = iss.get_iss_location()
    response_dict = json.loads(response)
    latitude = response_dict["iss_position"]["latitude"]
    longitude = response_dict["iss_position"]["longitude"]
    pass_times = iss.get_pass_times(latitude, longitude)
    print(pass_times)
