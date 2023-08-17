# Automated testing with GitHub Actions
When contributing to eva, a number of automated tests are performed by GitHub Actions to ensure that tests pass successfully, and that code and configuration files follow style conventions.

An overview of each GitHub Actions workflow is provided in the following subsections.

## Python coding norms
This workflow uses pycodestyle to ensure that all the python scripts added to eva are following the desired coding norms (generally the PEP8 convention).
The coding norm options are controlled by the `pycodestyle.cfg` file in the root directory of the repository.

Runs on push:
- to develop only

Runs on pull requests that are:
- opened
- synchronized
- reopened

## YAML coding norms
This workflow uses the `yaml-lint` GitHub action (ibiqlik/action-yamllint@v3) to ensure that the YAML that is added to the repository follows a desired convention. The specific checks/options for the YAML linter are controlled by the `.yamllint.yml` file in the root directory of the repository.

Runs on push:
- to develop only

Runs on pull requests that are:
- opened
- synchronized
- reopened

## Eva application tests
This workflow will build eva and all associated dependencies and run the suite of application tests defined in eva. Each test is automatically created whenever a properly formatted YAML file is added to `src/eva/tests/config`.  

Runs on push:
- to develop only

Runs on pull requests that are:
- opened
- synchronized
- reopened

## Eva notebook tests
This workflow will build eva and all associated dependencies and run the suite of Jupyter notebook tests defined in eva. Each test is automatically created whenever a Jupyter notebook file is added to `src/eva/tests/notebooks`.  

Runs on push:
- to develop only

Runs on pull requests that are:
- opened
- synchronized
- reopened

## Eva documentation dry run
Q for Akira/Dan, what exactly does this do???

Runs on pull requests that are:
- opened
- synchronized
- reopened
