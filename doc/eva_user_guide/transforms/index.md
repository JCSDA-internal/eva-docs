# Eva transform classes

This section descibes the various classes that eva provides for creating new variables from the variables read in the ingest classes.

In each case the transforms only have access to the `DataCollections` object and they can modify its contents only by adding new variables.
New variables may be created by:
  - filtering existing variables by data values
  - applying arithmetic manipulations to existing variables
  - generating statistics from a specific data dimension
  - selecting or slicing the data by time

Each transform is described in detail in its respective documentation page:

- [](accept_where)
- [](arithmetic)
- [](channel_stats)
- [](select_time)

```{toctree}
:titlesonly:
:hidden:
:maxdepth: 2

accept_where
arithmetic
channel_stats
select_time
```
