# Config class

The `Config` class in the `eva` package is a utility class for managing configuration parameters. It extends the built-in `dict` class in Python, allowing it to store key-value pairs of configuration parameters.

## Initialization

The `Config` class is initialized with two parameters:

- `dict_or_yaml`: This can either be a dictionary containing configuration parameters or a string representing the path to a YAML file containing the configuration.
- `logger`: An instance of a logger to handle log messages.

If a dictionary is provided, it is directly used as the configuration. If a string is provided, it is treated as a path to a YAML file, and the configuration is loaded from this file.

## Methods

The `Config` class has one main method: `get(key, default=None, abort_on_failure=True)`. This method retrieves the value associated with a given key from the configuration. If the key is not found, it either returns a default value (if provided), or aborts the program (if `abort_on_failure` is set to `True`).

## Usage

Here's a basic usage example:

```yaml
logger = Logger()
config = Config({'param1': 'value1', 'param2': 'value2'}, logger)
value = config.get('param1')
```

In this example, a `Config` object is created with a dictionary of configuration parameters. The `get` method is then used to retrieve the value associated with the key `'param1'`.
