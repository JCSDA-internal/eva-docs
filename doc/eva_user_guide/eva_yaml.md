# Eva and yaml files

Eva uses YAML formatted files to direct data load, data transformation, and 
plot generation.  YAML is a human-readable data-serialization language.  It is 
written with a .yml or .yaml (preferred) file extension.  Much like python, 
indentation is critical in yaml.

Eva contains examples of working YAML input files at `eva/src/eva/tests/config`.  

## YAML general notes
In YAML the `#` character proceeds comments.  

Keys are identified by a following colon `mykey:`, and are followed by their corresponding value (which may be a single item, 
other keys, lists, etc.).  

List members are denoted by a leading dash and space `- mylist`, with one list member per line.  Lists can also be 
specified by square brackets with each entry separated by a coma `[item1, item2]`.

Indentation is critical in YAML, as it defnies relationships between elements.  

## Eva's requirements for input
Eva expects to find two top level keys `datasets:` and `graphics:` in an input YAML file.  (Top level here means no indentation in the line.)
Additionally a third top level key `transforms:` may be specified as well.

```
datasets:
  - name: experiment
    type: IodaObsSpace
    filenames:
      - ${data_input_path}/ioda_obs_space.aircraft.hofx.2020-12-14T210000Z.nc4
    groups:
      - name: ObsValue
        variables: &variables [airTemperature, windEastward]
```

The value of the `type:` key above must reference a specific data ingest class.  Note that the specification in the YAML file is in camel case (CamelCase), while the
corresponding data ingest class will be in snake case (snake_case).  See https://github.com/JCSDA-internal/eva-docs/tree/develop/doc/eva_user_guide/data_ingest 
for the available ingest classes.


### Anchors and aliases

Anchors and aliases are YAML constructs that allow for reduced repeating syntax and extending
existing data nodes. Anchors `&` can be placed on a yaml component to mark a list or a multi-line section. 
An alias `*` can then call that anchor later in the document to reference the anchor contents.

Eva extends this construct.  Consider this example transform:

```
transforms:
  # Generate omb for GSI
  - transform: arithmetic
    new name: experiment::ObsValueMinusGsiHofXBc::${variable}
    equals: experiment::ObsValue::${variable}-experiment::GsiHofXBc::${variable}
    for:
      variable: *variables
```
Here variable is specified as the alias *variables.  This means that all variables specified by the preceeding variables anchor 
`variables: &variables [airTemperature, windEastward]` will be applied here.  The transform will step through the variables 
plugging them, one at a time, into the transform where `${variable}` is specified.

This same mechanism may be applied to the plots in `graphics:` as well.
