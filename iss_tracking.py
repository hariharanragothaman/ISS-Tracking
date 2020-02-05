import time
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
        """

    def epoch_time_converter(self, epochtime):
        """
        :brief: Function to convert epoch time
        :return (str): time in string format
        """
        time_human_format = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(epochtime))
        return time_human_format

    def get_iss_location(self):
        """
        : brief: Getter function to get current ISS location
        :return: JSON payload response
        """
        iss_object = requests.get('http://api.open-notify.org/iss-now.json', auth=('user', 'pass'))
        response = iss_object.text
        response_dict = json.loads(response)
        time_stamp = self.epoch_time_converter(response_dict["timestamp"])
        print('The ISS current location at {} is {} {}'.format(time_stamp,
                                                               response_dict["iss_position"]["latitude"],
                                                               response_dict["iss_position"]["longitude"]))
        return response

    def get_pass_times(self, latitude, longitude, altitude=None, number=None):
        """
        :brief: Function get overhead passing time of ISS
        :param latitude:   Latitude of the place to predict passes  (degress)
        :param longitude:  Longitude of the place to predict passes (degrees)
        :param altitude:   Altitude of the place to predict passes  (metres)
        :param number:     Number of passes to return
        """
        iss_url = "http://api.open-notify.org/iss-pass.json?lat=" + latitude + "&lon=" + longitude
        iss_object = requests.get(iss_url)
        response = iss_object.text
        pass_times = json.loads(response)
        for res in pass_times["response"]:
            print('The ISS will be overhead {} {} at {} for {} seconds'.format(latitude,
                                                                       longitude,
                                                                       self.epoch_time_converter(res["risetime"]),
                                                                       res["duration"]))
        #"The ISS will be overhead {LAT, LONG} at {time} for {duration}”"
        return response

if __name__ == "__main__":
    iss = ISSTracking()
    """
    Function call to current ISS location
    """
    response = iss.get_iss_location()
    """
    Function call to get ISS Pass times
    """
    response_dict = json.loads(response)
    latitude = response_dict["iss_position"]["latitude"]
    longitude = response_dict["iss_position"]["longitude"]
    iss.get_pass_times(latitude, longitude)
