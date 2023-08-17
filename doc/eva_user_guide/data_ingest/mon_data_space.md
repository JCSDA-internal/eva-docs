# Monitor data space (NCEP legacy) ingest class
Mon_data_space enables eva to ingest legacy DA monitoring data and produce plots
similar to the legacy DA monitoring suite (https://github.com/NOAA-EMC/GSI-Monitor).

The specific yaml file components necessary to accomplish this are described below.
These example yaml files maybe be found in `eva/src/eva/tests/config`:
```
testMonDataSpaceHirs4Metop-A.yaml
testMonSummary.yaml
```

More complex yaml files can be found in the obs-monitor repository (https://github.com/NOAA-EMC/obs-monitor/blob/develop/parm/gfs).

Note this is still a work in progress.

## Specify mon_data_space
The dataset specification must include type MonDataSpace:
```
datasets:
  - name: experiment
    type: MonDataSpace
```
## Input control and data files
Both a control file and one or more data files are required.  The control file describes
the contents of the (Fortran) binary data file(s).  The dataset specification is thus:
```
datasets:
  - name: experiment
   type: MonDataSpace
   control_file:
     - ../data/time.hirs4_metop-a.ctl
   filenames:
     - ../data/time.hirs4_metop-a.2015051418.ieee_d
     - ../data/time.hirs4_metop-a.2015051500.ieee_d
```
When eva loads the data files, all the variables in the control file will be added to the dataset. 
Mon_data_space will also add a variable `cycle` to the dataset.  This contains the cycle time of all 
specified data files.  Additionally the variables `cycle` and `scan` (scan angle) will also be added
to the dataset if specified as dimensions in the control file.  
