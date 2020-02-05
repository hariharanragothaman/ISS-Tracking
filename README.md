# ISS-Tracking
Using Open Notify API to track the International Space Station 


### Steps to use the ISSTracking tool:

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
