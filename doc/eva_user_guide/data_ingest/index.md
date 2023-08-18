# Eva data ingest classes

This section descibed the various classes that exist for reading different data formats. 

Each of these classes read in data from different formats and place them in an xarray dataset for use in eva. 

The input datasets cover a wide variety of use cases including model gridded data, observation files, diagnostic output from data assimilation software, and parsing of log files. 

The specific usage of each class is detailed on its respective documentation page.

These classes include:
- [](cubed_sphere_restart)
- [](soca_restart)
- [](lat_lon)
- [](gsi_obs_space)
- [](ioda_obs_space)
- [](jedi_log)
- [](mon_data_space)


```{toctree}
:titlesonly:
:hidden:
:maxdepth: 2

cubed_sphere_restart
gsi_obs_space
ioda_obs_space
jedi_log
lat_lon
mon_data_space
soca_restart
```
