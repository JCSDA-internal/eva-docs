# Logger class

The Logger class provides logging functionality for tasks. It allows for different levels of logging: `INFO`, `TRACE`, `DEBUG`, and `ABORT`.

## Initialization

The Logger class is initialized with a task_name which is a string representing the name of the task associated with the logger.

``` python
logger = Logger(task_name="MyTask")
```

## Logging Levels

The logger has four levels of logging: `INFO`, `TRACE`, `DEBUG`, and `ABORT`. By default, only `INFO` level logging is enabled. Other levels can be enabled by setting the corresponding environment variable to 1. For example, to enable `TRACE` level logging, you would set `export LOG_TRACE=1`.

## Logging Methods

The Logger class provides the following methods for logging:

- `logger.info(message: str)`: Logs an informational message.
- `logger.trace(message: str)`: Logs a trace message.
- `logger.debug(message: str)`: Logs a debug message.
- `logger.abort(message: str)`: Logs an abort message and exits the program.

Each of these methods takes a string message as an argument, which is the message to be logged.
