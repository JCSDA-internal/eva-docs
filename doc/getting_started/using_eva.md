# Using Eva

Eva is provided with a fairly extensive set of tests and it is required that all data ingest and transform classes are tested in at least one test.

In order to get going with eva it is recommended that you first run the tests to ensure you have the installation and environment correct.

There are two kinds of complete system tests, application tests and notebook tests. These respectively test the batch and interactive processing techniques available in eva.

These tests can be run with:

```bash
eva_tests <test_type>
```

where `<test_type>` is replaced with either `application` or `notebook`.

The files that drive the YAML-based tests are all contained in `src/eva/tests/config` and the notebooks are contained in `src/eva/tests/notebooks`.

To get started with running eva using a YAML file it is recommended to pick a YAML file from the above tests directory that corresponds to the class you wish to use for reading and modify it to work with the appropriate data. Once a YAML has been constructed it can be run with

```bash
eva experiment.yaml
```

where `experiment.yaml` is replaced with the constructed YAML file.

It is not possible to run eva by passing it a notebook, though you can execute a notebook as a script using e.g. `nbconvert`. Notebooks are in a sense stand alone applications. You can open one of the test notebooks and modify it to a specific purpose and then run using JupyterHub or as a script.

