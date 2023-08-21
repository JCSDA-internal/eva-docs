# Channel statistics
Calculates statistical measures for specified channel data variables within the provided data
collections.  It iterates over the specified collections, groups, and variables, and
calculates statistical measures as defined in the 'statistic list' expressions within the
configuration. The resulting variables are added to the data collections.

    Args:
        config (dict): A configuration dictionary containing transformation parameters.
        data_collections (DataCollections): An instance of the DataCollections class containing
        input data.

    Returns:
        None

This is an example of the config dictionary:

    Example:
        config = {
            'collections': [...],
            'groups': [...],
            'variables': [...],
            'variable_name': 'data_variable',
            'statistic list': ['Mean', 'Std', 'Count'],
            'statistic_dimension': 'Location'
        }

The configuration components are defined as:

  - `variable_name`: specific variable to which the transform will be applied
  - `statistic list`: list of statistics to be calculated and added to `collections`
    - If unspecified the default is ` ['Mean', 'Std', 'Count', 'Median', 'Min', 'Max']`
  - `statistic_dimension`: channel statistical dimension name


## Channel statistics filter for batch processing

To apply the channel statistics filter to a yaml for batch processing:

``` yaml

transforms:

  - transform: channel_stats
    variable_name: experiment::group::${variable}
    for:
      variable: *variables

```

Where `group` is a group available for use in the data collection.


## Channel statistics filter for interactive processing

The channel statistics filter is currently unavailable for interactive processing.



