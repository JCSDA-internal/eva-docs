# Arithmetic

Applies arithmetic transformations to data variables within the provided data collections. 
It iterates over the specified collections, groups, and variables, and applies arithmetic 
expressions as defined in the 'equals' expression within the configuration. The resulting 
variables are added to the data collections.

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
            'new name': 'result_variable',
            'equals': '(${collection}::${group}::${var1} + ${collection}::${group}::${var2}) / 2'
        }

The configuration components are defined as:

  - `new name`: name of the resulting variable which will be added to `data_collections`
  - `equals`: the result of the arithmetic expression applied to the specified variables within `data_collections`
