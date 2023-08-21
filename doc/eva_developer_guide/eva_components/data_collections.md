# Data collections class for holding data

Central to eva is the `DataCollections` class. This class specifies how data files read into eva must be stored. If each class that reads a certain data type were to define its own data structure it would not be possible to write generic code for executing transforms or plotting.

Data in eva is stored using `DataSets` in `Xarray`. An instance of eva may have multiple 'collections', which is to say that it has multiple `DataSets` in the `DataCollections` object. Each object of `DataSets` can be accessed using a string referring to the collection name. Each collection contains `DataArrays` which have common dimensions and possibly coordinates. Each instance of `DataArrays` in the collection is given a name that consists of a group and a variable. The full name is written as `group::variable`, separated by double colon. To access a variable using the method in the class users provide the complete name as `collection::group::variable`. The role of each class that performs an ingest is to read the file, convert the data to a `DataSets` object (or several objects) and then pass them to the `DataCollections`.

**Note:** When running in batch processing mode there is always only a single instance of `DataCollections`. When running interactively a user is free to create multiple objects from `DataCollections`, though it may not be advantageous to do so.

A data reading class can either create a new collection or append existing data in the object. The method in the class that is used to do this is `create_or_add_to_collection`. The method is passed a collection name, a collection (which is an object of `DataSets` created locally) and optionally a `concat_dimension`. If the collection name is not already in existence a new one is created and the collection passed in is shallow copied for later use. If the name is already in use then the `concat_dimension` is needed so the data can be properly combined. The passing of `concat_dimension` allows multiple files to be read into a single collection, for example if you want the data from multiple times in a single collection.

The function `display_collections` can be used to print out all the variables stored in all the collections.

### Methods

Below outlines the interfaces for the different methods within the class.

`create_or_add_to_collection(collection_name, collection, concat_dimension=None)`

This method creates a new collection or adds to an existing collection.

- collection_name (str): Name of the collection.
- collection (Dataset): The xarray Dataset to add or create from.
- concat_dimension (str, optional): Dimension along which to concatenate if adding to an existing collection.

`adjust_channel_dimension_name(channel_dimension_name)`

This method adjusts the name of the channel dimension in all collections.

- channel_dimension_name (str): New name for the channel dimension.

`adjust_location_dimension_name(location_dimension_name)`

This method adjusts the name of the location dimension in all collections.

- location_dimension_name (str): New name for the location dimension.

`add_variable_to_collection(collection_name, group_name, variable_name, variable)`

This method adds a new variable to a collection.

- collection_name (str): Name of the collection to add the variable to.
- group_name (str): Name of the group where the variable belongs.
- variable_name (str): Name of the variable.
- variable (DataArray): The xarray DataArray to add.

`get_variable_data_array(collection_name, group_name, variable_name, channels=None)`

This method retrieves a specific variable (as a DataArray) from a collection.

- collection_name (str): Name of the collection.
- group_name (str): Name of the group where the variable belongs.
- variable_name (str): Name of the variable.
- channels (int or listint], optional): Indices of channels to select.

`get_variable_data(collection_name, group_name, variable_name, channels=None)`

This method retrieves the data of a specific variable from a collection.

- collection_name (str): Name of the collection.
- group_name (str): Name of the group where the variable belongs.
- variable_name (str): Name of the variable.
- channels (int or list[int], optional): Indices of channels to select.

`validate_names()`

This method validates naming conventions for collections, groups, and variables.

`nan_float_values_outside_threshold(threshold, cgv_to_screen=None)`

This method sets values outside a threshold to NaN in selected collections, groups, and variables.

- threshold (float): Threshold value for screening.
- cgv_to_screen (str, optional): Collection, group, and variable to screen.

`display_collections()`

This method displays information about available collections, groups, and variables.
