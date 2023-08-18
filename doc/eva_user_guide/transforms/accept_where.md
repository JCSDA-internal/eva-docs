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
