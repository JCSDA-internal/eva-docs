# Logger class

The Logger class in the eva package provides logging functionality for tasks. It allows for different levels of logging: INFO, TRACE, DEBUG, and ABORT.

## Initialization

The Logger class is initialized with a task_name which is a string representing the name of the task associated with the logger.

``` python
logger = Logger(task_name="MyTask")
```

## Logging Levels

The logger has four levels of logging: INFO, TRACE, DEBUG, and ABORT. By default, only INFO level logging is enabled. Other levels can be enabled by setting the corresponding environment variable to 1. For example, to enable TRACE level logging, you would set the LOG_TRACE environment variable to 1.

## Logging Methods

The Logger class provides the following methods for logging:

- `info(message: str)`: Logs an informational message.
- `trace(message: str)`: Logs a trace message.
- `debug(message: str)`: Logs a debug message.
- `abort(message: str)`: Logs an abort message and exits the program.

Each of these methods takes a string message as an argument, which is the message to be logged.

## send_message Method

The send_message(level: str, message: str) method is a general method for logging a message at a specified level. The level argument is a string representing the logging level, and message is the message to be logged.

```python
logger.send_message("INFO", "This is an informational message.")
```

This method is used internally by the `info`, `trace`, `debug`, and `abort` methods.
