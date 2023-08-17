# Cubed sphere restart ingest class
The Finite Volume Cubed Sphere (FV3) atmospheric model writes out netCDF restart files on the native cubed sphere using FMS (Flexible Modeling System). Eva supports reading of the restart files written by FV3/FMS for plotting model states.

An example YAML file may look like the following:
```
datasets:
  - name: experiment
    type: CubedSphereRestart
    restart_filenames:
      - ./20210323.150000.sfc_data.tile1.nc
      - ./20210323.150000.sfc_data.tile2.nc
      - ./20210323.150000.sfc_data.tile3.nc
      - ./20210323.150000.sfc_data.tile4.nc
      - ./20210323.150000.sfc_data.tile5.nc
      - ./20210323.150000.sfc_data.tile6.nc
    orog_filenames:
      - ./C48_oro_data.tile1.nc
      - ./C48_oro_data.tile2.nc
      - ./C48_oro_data.tile3.nc
      - ./C48_oro_data.tile4.nc
      - ./C48_oro_data.tile5.nc
      - ./C48_oro_data.tile6.nc
    2d variables: [t2m]
    3d variables: []
    orography variables: [geolon, geolat]
```

The above keys are defined as follows:

- `name`: the name of the dataset that gets propagated throughout eva
- `type`: `CubedSphereRestart` to read in these FV3/FMS cubed sphere restart netCDF files 
- `restart_filenames`: a list of 6 (tile1-6 in order) netCDF restart files that you wish to read in
- `orog_filenames`: a list of 6 (tile1-6 in order) netCDF files containing the FV3 model orography/geometry
- `2d variables`: the list of two-dimensional variables from the files defined in `restart_filenames` that you wish to read in using eva
- `3d variables`: the list of three-dimensional variables from the files defined in `restart_filenames` that you wish to read in using eva
- `orography variables` the list specifying the [x, y] variable names that are used to plot datasets spatially on a map. These variables will be read in from the files defined in `orog_filenames`

Following the eva convention, datasets will be available to the transforms and plots sections like so:
`name::group::variable`
where:
- `name`=`name` defined in the YAML
- `group` is `FV3Orog` for `orography variables`, `FV3Vars2D` for `2d variables`, and `FV3Vars3D` for `3d variables`, respectively
- `variable` is the name of the variable specified in each of the appropriate lists
