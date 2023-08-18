# IODA observaton space (netCDF) ingest class
The Joint Effort for Data assimilation Integration (JEDI) data assimilation system has the ability to write out observation-space diagnostic files in the Interface for Observation Data Access (IODA) format. While IODA supports many file formats, one of the most common formats used to read and write IODA files is netCDF4. Using this class, eva can read in a netCDF4 formatted IODA observation or diagnostic file for computing statistics or plotting.

An example YAML file may look differently depending on if you are reading in a radiance IODA file or a conventional observation IODA file. For example, `channels` does not apply to conventional data but does to satellite radiance data.

``` yaml
datasets:
  - name: experiment
    type: IodaObsSpace
    filenames:
      - ./ioda_obs_space.amsua_n19.hofx.2020-12-14T210000Z.nc4
    channels: &channels 3,8
    # Note: channelNumber is automatically added to the output and should not
    # be listed below
    groups:
      - name: ObsValue
        variables: &variables [brightnessTemperature]
      - name: GsiHofXBc
      #- name: GsiEffectiveQC
      - name: hofx
      - name: EffectiveQC
      - name: MetaData
```

The above keys are defined as follows:
- `name`: the name of the dataset that gets propagated throughout eva
- `type`: `IodaObsSpace` the class to read in the IODA netCDF4 files
- `filenames`: the list of IODA files to read in
- `channels`: a parsable string list of channels to read in
- `groups`: a list of group names and list of variables to read in. IODA files are structured like a filesystem where groups are directories and variables are files within those directories.
    - `name`: the name of the group in the IODA file
    - `variables`: the list of variables to read from this group

Following the eva convention, datasets will be available to the transforms and plots sections like so:
`name::group::variable`
where:
- `name`=`name` defined in the YAML
- `group` is the `name` defined in the group list entry
- `variable` is the name of the variable specified in each of the appropriate lists in the group
