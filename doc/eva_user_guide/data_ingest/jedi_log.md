# JEDI log files ingest class
The Joint Effort for Data assimilation Integration (JEDI) data assimilation system uses the Object Oriented Prediction System (OOPS) at its core to handle most high level functionality. During the minimization of variational data assimilation, OOPS will write to a log file information that can be parsed and visualized. This class parses the logfile and reads the data into an eva-compatible format for use in transfomrs and plotting.

An example YAML file may look like the following:
``` yaml
datasets:
  - type: JediLog
    collection_name: jedi_log_test_rpcg
    jedi_log_to_parse: ./jedi_log.var_rpcg.txt
    data_to_parse:
      convergence: true
```

The above keys are defined as follows:

- `collection_name`: the name of the dataset that gets propagated throughout eva
- `type`: `JediLog` the class to parse an OOPS log
- `jedi_log_to_parse`: path to log file to parse
- `data_to_parse`: dictionary of options to parse
Currently supported types of data to parse are as follows:
    - `convergence`: `true` or `false`

Following the eva convention, datasets will be available to the transforms and plots sections like so:
`name::group::variable`
where:
- `name` is the `collection_name` defined in the YAML
- `group` is the type of data that is parsed (under the `data_to_parse` key)
- `variable` is the name of the variable that is parsed (see source code for details)
