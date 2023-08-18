# Accept where
 Applies a filtering transformation to data variables within the provided data collections. 
 It iterates over the specified collections, groups, and variables, and applies filtering 
 conditions as defined in the 'where' expression within the configuration.  The resulting 
 filtered variables are added to the data collections.

    Args:
        config (dict): A configuration dictionary containing transformation parameters.
        data_collections (DataCollections): An instance of the DataCollections class containing
                                            input data.

    Returns:
        None

    Raises:
        ValueError: If the 'where' expression format is incorrect.

This is an example of the config dictionary:

    Example:
        config = {
            'collections': [...],
            'groups': [...],
            'variables': [...],
            'new name': 'filtered_variable',
            'starting field': 'original_variable',
            'where': ['${collection}::${group}::${variable} >= 0.0']
        }
        
The configuration components are defined as:
  - `new name`: name of the resulting variable which will be added to `data collections`
  - `starting field`: original variable which will be filtered using the `where` condition
  - `where`: an arithmetic filter applied to the specified `variable`.  Note this could be the `original_variable` or a different variable in `data_collections`.


## Accept where filter for batch processing

To apply the accept where filter to a yaml for batch processing:

``` yaml
transforms:

  - transform: accept where
    new name: collection_name::new_group_name::${variable}
    starting field: collection_name::new_group_name::${variable}
    where:
      - collection_name::filter_group::${variable} == 0
    for:
      variable: *variables
```

`variables` are defined in `datasets` and are referenced in the `transform` filter. `where` is a conditional statement (<, >, ==, etc.) with the filter group of choice.


## Accept where filter for interactive processing

To apply the accept where filter during an eva interactive session:

        conditions = [filter_group == 0]
        EvaInteractive.accept_where(new_group_name, starting_field, conditions, collection_name)

The parameters for `accept_where` are
  - `new_group_name`: new name to label transformed group
  - `starting_field`: group in collection that will be transformed
  - `conditions`: a single conditional statement or list of conditional statements
  - `collection_name`: name of the collection that contains group to be transformed
