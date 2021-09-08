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
2020-02-05 01:37:38,485 - The ISS current location at 2020-02-05 01:37:37 is (47.4545,111.4462)
(venv)

```

#### Get Overhead Passing time of ISS, given lattitude, longitude and other details
```
$ python3.7 iss_tracking.py -passtime true --latitude <latitude> --longitude <longitude>

Sample Output:

$ python3.7 iss_tracking.py --passtime True --lattitude -27 --longitude -101 --number 4
2020-02-05 01:37:17,248 - The ISS will be overhead (-27,-101) at 2020-02-05 03:53:42 for 180 seconds
2020-02-05 01:37:17,250 - The ISS will be overhead (-27,-101) at 2020-02-05 08:47:02 for 564 seconds
2020-02-05 01:37:17,252 - The ISS will be overhead (-27,-101) at 2020-02-05 10:23:17 for 646 seconds
2020-02-05 01:37:17,254 - The ISS will be overhead (-27,-101) at 2020-02-05 23:48:41 for 537 seconds
(venv)

$ python3.7 iss_tracking.py --passtime True --lattitude -27 --longitude -101 --number 3
2020-02-05 01:37:06,988 - The ISS will be overhead (-27,-101) at 2020-02-05 03:53:42 for 180 seconds
2020-02-05 01:37:06,990 - The ISS will be overhead (-27,-101) at 2020-02-05 08:47:02 for 564 seconds
2020-02-05 01:37:06,993 - The ISS will be overhead (-27,-101) at 2020-02-05 10:23:17 for 646 seconds
(venv)

```

#### Get Number of ppl in space
```
$ python3.7 iss_tracking.py --pplinspace true

Sample Output:

$ python3.7 iss_tracking.py --pplinspace True
2020-02-05 01:37:54,520 - The astronauts living in ISS are ['Christina Koch', 'Alexander Skvortsov', 'Luca Parmitano', 'Andrew Morgan', 'Oleg Skripochka', 'Jessica Meir']
(venv)
```
