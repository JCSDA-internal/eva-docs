# Timing Class

The `Timing` class is a utility class in the EVA (Ensemble Verification and Analysis) system for managing timing profiling of EVA code.

## Class Initialization

The class is initialized without any arguments. The initialization process sets up a logger, records the start time, and initializes an empty dictionary to hold timers.

```python
timing = Timing()
```

## Methods

### start(timer_name: str)

This method starts a timer with the given name. If the timer does not exist, it is created and its count is set to zero. If the timer is already running, an error message is logged.

```python
timing.start('timer1')
```

### stop(timer_name: str)

This method stops a timer with the given name. If the timer does not exist or is not running, an error message is logged. The elapsed time is added to the total time of the timer.

```python
timing.stop('timer1')
```

### finalize()

This method finalizes the timing measurements and logs the results. It checks that no timer is still running, calculates the total time, the time per count, and the percentage of total time for each timer, and logs this information.

```python
timing.finalize()
```

## Example Usage
```python
timing = Timing()
timing.start('timer1')
<Code to be timed goes here>
timing.stop('timer1')
timing.finalize()
```
