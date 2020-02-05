"""
Python Utility to class for OpenNotify API to track the International Space Station

"""

import time
import json
import argparse
import logging

import requests

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

class ISSTracking:
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

    def handle_request(self, url):
        """
        Utility function for handling requests
        """
        iss_object = requests.get(url, auth=('user', 'pass'))
        response = iss_object.text
        return response

    def get_iss_location(self):
        """
        : brief: Getter function to get current ISS location
        :return: JSON payload response
        """
        iss_url = 'http://api.open-notify.org/iss-now.json'
        response = self.handle_request(iss_url)
        response_dict = json.loads(response)
        time_stamp = self.epoch_time_converter(response_dict["timestamp"])
        logging.info('The ISS current location at {} is ({},{})'.format(time_stamp,
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
        # SANITY CHECKS
        if abs(float(latitude)) > 80 or abs(float(longitude)) > 180:
            raise ValueError("Invalid Input: Please enter input of a valid range")
        if altitude is not None:
            if (int(altitude) < 0 or int(altitude) > 10000):
                raise ValueError("Invalid Input: Please enter input of a valid range")
        if number is not None:
            if int(number) < 0 or int(number) > 100:
                raise ValueError("Invalid Input: Please enter input of a valid range")

        iss_url = "http://api.open-notify.org/iss-pass.json?lat=" + latitude + "&lon=" + longitude
        response = self.handle_request(iss_url)
        pass_times = json.loads(response)
        for res in pass_times["response"]:
            logging.info('The ISS will be overhead ({},{}) at {} for {} seconds'.format(latitude,
                                                                                      longitude,
                                                                                      self.epoch_time_converter(res["risetime"]),
                                                                                      res["duration"]))
        return response

    def get_ppl_in_space(self):
        """
        :brief: Function to return number of ppl in space
        :return: JSON payload of response
        """
        iss_url = "http://api.open-notify.org/astros.json"
        response = self.handle_request(iss_url)
        ppl_in_space = json.loads(response)
        result_map = {}
        for res in ppl_in_space["people"]:
            if res["craft"] not in result_map:
                result_map[res["craft"]] = [res["name"]]
            else:
                result_map[res["craft"]].append(res["name"])
        for key, value in result_map.items():
            logging.info("The astronauts living in {} are {}".format(key, value))
        return response

def main():
    """
    :param arguments: argparse based arguments
    :return: None
    """
    parser =  argparse.ArgumentParser(description="International Space Station Tracking Tool")
    parser.add_argument("--current", help='Get the current position of ISS')
    parser.add_argument("--passtime", help='Get the passing time of ISS')
    parser.add_argument("--pplinspace", help='Get the numbe of ppl in space')
    parser.add_argument("--demo", help='Test functionality of the tool')

    parser.add_argument('--lattitude', action='store', type=str, help='Latitude in degrees')
    parser.add_argument('--longitude', action='store', type=str, help='Longitude in degrees')
    parser.add_argument('--altitude', action='store', type=str, help='Altitude')
    parser.add_argument('--number', action='store', type=str, help='number of entries in response')
    args = parser.parse_args()

    iss = ISSTracking()
    if args.current:
        # Driver code for getting ISS location
        response = iss.get_iss_location()
        response_dict = json.loads(response)

    if args.passtime:
        latitude = args.lattitude
        longitude = args.longitude
        # Driver code for getting ISS passing overhead time
        iss.get_pass_times(latitude, longitude)

    if args.pplinspace:
        # Driver code for getting number of ppl in space
        iss.get_ppl_in_space()

    if args.demo:
        response = iss.get_iss_location()
        response_dict = json.loads(response)
        latitude = response_dict["iss_position"]["latitude"]
        longitude = response_dict["iss_position"]["longitude"]
        iss.get_pass_times(latitude, longitude)
        iss.get_ppl_in_space()

if __name__ == "__main__":
    """
    TODO:  Enhancements
          2. number and altitude logic
          1. Write some unit-tests
          4. Write handle request function - scalable
    """
    main()
