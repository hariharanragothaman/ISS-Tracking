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
$ ./iss_tracking --current
```

#### Get Overhead Passing time of ISS, given lattitude, longitude and other details
```
$ ./iss_tracking -passtime <lattitude> <longitude>
```

#### Get Number of ppl in space
```
$ ./iss_tracking --pplinspace
```
