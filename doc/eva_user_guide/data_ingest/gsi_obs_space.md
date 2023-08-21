# GSI observaton space (ncdiag) ingest class
The Gridpoint Statistical Interpolation (GSI) data assimilation software has the ability to write out observation-space diagnostic files in a netCDF format. This is used operationally in many National Weather Service modeling systems, including the Global Forecast System (GFS) starting with version 16. Eva can read in these GSI diagnostic files using this GsiObsSpace class described below.


## GSI observation space injest for batch processing

An example YAML file may look differently depending on if you are reading in a radiance diagnostic file or a conventional observation diagnostic file. 
For example, a conventional diagnostic YAML may look like:
``` yaml
datasets:
  - name: experiment
    type: GsiObsSpace
    variable: t
    filenames:
      - ./gsi_obs_space.conv_t_ges.2020092000.nc4
    groups:
      - name: GsiNcDiag
        variables: &variables [Obs_Minus_Forecast_adjusted,
                               Observation,
                               Latitude,
                               Longitude]
```
and a radiance diagnostic YAML may look like:
``` yaml
datasets:
  - name: experiment
    type: GsiObsSpace
    satellite: metop-a
    sensor: amsua
    filenames:
      - ./gsi_obs_space.amsua_metop-a_ges.2020092200.nc4
    channels: &channels 3,8
    groups:
      - name: GsiNcDiag
        # Note: channelNumber is automatically added to the output and should not
        # be listed as a variable
        variables: &variables [Obs_Minus_Forecast_adjusted,
                               Observation,
                               Latitude,
                               Longitude]
```

The above keys are defined as follows:
- `name`: the name of the dataset that gets propagated throughout eva
- `type`: `GsiObsSpace` the class to read in the GSI netCDF diagnostic files
- `variable` (conventional only): the type of conventional variable you are reading in (GSI diagnostic files are split by variable, like t or uv)
- `satellite` (radiance only): the name of the satellite platform in the diagnostic file
- `sensor` (radiance only): the name of the satellite sensor in the diagnostic file
- `filenames`: list of GSI netCDF diagnostic files to read in
- `channels` (radiance only): string list that is parsed of the channels you wish to read in
- `groups`
    - `name`: the name of the group that gets propagated throughout eva
    - `variables`: the list of variables that you wish to read into the above group

Note that groups is a list of groups. This allows for the user to better organize the input dataset and combine variables in a more logical way as they see fit, but for many uses, this will be a list of only one group defined.

Following the eva convention, datasets will be available to the transforms and plots sections like so:
`name::group::variable`
where:
- `name`=`name` defined in the YAML
- `group` is the `name` defined in the group list entry
- `variable` is the name of the variable specified in each of the appropriate lists in the group


## GSI observation space injest for interactive processing

To apply the gsi observation space injest class during an eva interactive, call the `load_collection()` with the gsi data space name:

        EvaInteractive.load_collection(collection_name, filenames, 'GsiObsSpace')

where
  * `collection_name` is a user-defined label for the loaded collection
  * `filenames` are the file(s) that are to be loaded into the data collection
  * `'GsiObsSpace'` selects the GSI observation injest class


