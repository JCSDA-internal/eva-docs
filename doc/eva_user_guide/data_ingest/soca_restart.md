# SOCA restart ingest class
The Sea-Ice Ocean Coupled Analysis (SOCA) data assimilation system uses netCDF restart files to read and write model states. This class can be used to read these SOCA netCDF restart files in to eva.


## SOCA restart injest for batch processing

An example YAML file may look like the following:
``` yaml
datasets:
  - name: experiment
    type: SocaRestart
    soca_filenames: ./ocn.3dvar_soca.an.2018-04-15T00:00:00Z.nc
    geometry_file: ./soca_gridspec.72x35x25.nc

    variables: [ave_ssh, Salt]
    coordinate variables: [lon, lat]
```

The above keys are defined as follows:

- `name`: the name of the dataset that gets propagated throughout eva
- `type`: `SocaRestart` to read in these SOCA compatible restart netCDF files 
- `soca_filenames`: path to SOCA restart file to read in
- `geometry_file`: path to SOCA geometry definition netCDF file to read in
- `variables`: list of variables to read in
- `coordinate variables`: list of [x, y] variables to read in for plotting

Following the eva convention, datasets will be available to the transforms and plots sections like so:
`name::group::variable`
where:
- `name`=`name` defined in the YAML
- `group` is `SOCAgrid` for `coordinate variables` and is `SOCAVars` for `variables` defined in the YAML
- `variable` is the name of the variable specified in each of the appropriate lists in the group


## SOCA restart injest for interactive processing

This injest class is not yet implemented for eva interactive.
