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



## Arithmetic filter for batch processing

To apply the arithmetic filter to a yaml for batch processing:

``` yaml
transforms:

  - transform: arithmetic
    new name: collection_name::new_group_name::${variable}
    equals: collection_name::curr_group_1::${variable}-collection_name::curr_group_2::${variable}
    for:
      variable: *variables

```

`variables` are defined in `datasets` and are referenced in the `transform` filter. `equals` is an arithmetic expression (+, -, /, *) with groups that can be found in the collection labeled `collection_name`.


## Arithmetic filter for interactive processing

To apply the arithmetic filter during an eva interactive session:

        expression = 'curr_group_1-curr_group_2'
        EvaInteractive.arithmetic(new_group_name, expression, collection_name)

The parameters for `arithmetic` are
  - `new_group_name`: new name to label transformed group
  - `expression`: arithmetic expression using groups currently in collection
  - `collection_name`: name of the collection that contains group to be transformed
