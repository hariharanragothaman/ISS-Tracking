# ISS-Tracking
Using Open Notify API to track the International Space Station 


### Steps to use the ISSTracking tool:

##### Initial Setup
```
$ git clone git@github.com:hariharanragothaman/ISS-Tracking.git
$ cd ISS-Tracking
$ make vsetup
$ source ./venv/bin/activate
$ ./venv/pip install -r requirements.txt
```

##### Get the current ISS Location
```
$ python3.7 iss_tracking.py --current true

Sample Output:

$ python3.7 iss_tracking.py --current True
2020-02-05 00:42:58,906 - The ISS current location at 2020-02-05 00:42:58 is -29.0760 -88.1768
(venv)

```

#### Get Overhead Passing time of ISS, given lattitude, longitude and other details
```
$ python3.7 iss_tracking.py -passtime true --latitude <latitude> --longitude <longitude>

Sample Output:

$ python3.7 iss_tracking.py --passtime True --lattitude -27 --longitude -101
2020-02-05 00:43:34,722 - The ISS will be overhead -27 -101 at 2020-02-05 03:53:42 for 180 seconds
2020-02-05 00:43:34,725 - The ISS will be overhead -27 -101 at 2020-02-05 08:47:02 for 564 seconds
2020-02-05 00:43:34,727 - The ISS will be overhead -27 -101 at 2020-02-05 10:23:17 for 646 seconds
2020-02-05 00:43:34,729 - The ISS will be overhead -27 -101 at 2020-02-05 23:48:41 for 537 seconds
(venv)

```

#### Get Number of ppl in space
```
$ python3.7 iss_tracking.py --pplinspace true

Sample Output:

$ python3.7 iss_tracking.py --pplinspace true
2020-02-05 00:47:31,104 - The astronauts living in ISS are ['Christina Koch', 'Alexander Skvortsov', 'Luca Parmitano', 'Andrew Morgan', 'Oleg Skripochka', 'Jessica Meir']
(venv)

```
