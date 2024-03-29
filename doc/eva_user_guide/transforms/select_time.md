# Select time
 Selects and processes data variables for specified time cycles or a single time point.  It iterates 
 over the specified collections, groups, and variables, and selects data for the specified time period. If
 two time cycles are provided, it calculates the mean of a time slice; otherwise, it selects data
 for a single time point. The resulting processed variables are added to the data collections.

    Args:
        config (dict): A configuration dictionary containing transformation parameters.
        data_collections (DataCollections): An instance of the DataCollections class containing
                                            input data.

    Returns:
        None


This is an example of the config dictionary:

        config = {
            'collections': [...],
            'groups': [...],
            'variables': [...],
            'new name': 'time_selected_variable',
            'starting field': 'original_variable',
            'cycle': 'YYYYMMDDHH',
            # OR
            'start cycle': 'YYYYMMDDHH',
            'end cycle': 'YYYYMMDDHH'
        }

The configuration components are defined as:

  - `new name`: name of the resulting variable which will be added to `collections`
  - `starting field`: original variable which will be selected for a time point or averaged over a time slice
    
  - `cycle`: 10 digit cycle time for a single time point.

OR
  - `start cycle`: 10 digit cycle time for the first cycle of a time slice
  - `end cycle`: 10 digit cycle time for the last cycle of the time slice


## Select time filter for batch processing

To apply the select time filter to a yaml for batch processing:

``` yaml

transforms:

  - transform: select time
    new name: experiment::group::count1
    starting field: experiment::group::count
    cycle: 2015051418
    for:
      variable: [none]

```

In this example, `group` represents a group available for use in the data collection. No variables are referenced. Instead it is indicated in the starting field as `count`. A new variable called `count1` is created.


## Select time filter for interactive processing

The select time filter is currently unavailable for interactive processing.


