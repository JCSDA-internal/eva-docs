# Basic latitude-longitude netCDF ingest class
Eva has the ability to read in simple netCDF files on a latitude-longitude or Gaussian grid that contain two and three dimensional variables as well as the latitude and longitude values needed for plotting on a map. One example type of file that can be read in using this class is a netCDF Gaussian grid increment file produced by the Gridpoint Statistical Interpolation (GSI) data assimilation software.

An example YAML file may look like the following:
```
  - name: experiment
    type: LatLon
    group: increment
    filename: ./gdas.t00z.atminc.nc
    variables: [T_inc, lat, lon]
```

The above keys are defined as follows:
- `name`: the name of the dataset that gets propagated throughout eva
- `type`: `LatLon` to read in a Lat-Lon or Gaussian grid netCDF file
- `group`: the name of the group that gets propagated throughout eva
- `filename`: the path to the file you wish to read in
- `variables`: a list of all variables you wish to read in from `filename`

Following the eva convention, datasets will be available to the transforms and plots sections like so:
`name::group::variable`
where:
- `name`=`name` defined in the YAML
- `group`=`group` defined in the YAML
- `variable` is the name of the variable specified in the `variables` list
