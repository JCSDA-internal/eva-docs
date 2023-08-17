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

Developers can run this manually by running `python pycodestyle_run.py` in the root directory of the repository.

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

Developers can run these manually by running `eva_tests application` once eva is installed.

## Eva notebook tests
This workflow will build eva and all associated dependencies and run the suite of Jupyter notebook tests defined in eva. Each test is automatically created whenever a Jupyter notebook file is added to `src/eva/tests/notebooks`.  

Runs on push:
- to develop only

Runs on pull requests that are:
- opened
- synchronized
- reopened

Developers can run these manually by running `eva_tests notebook` once eva is installed.

## Eva documentation dry run
This workflow will ensure that the eva documentation (using a combination of sphinx and nbsite) still is generated properly. Note that this workflow does not publish the documentation anywhere and is only published when PRs are merged into eva.

Runs on pull requests that are:
- opened
- synchronized
- reopened


## Tips/Notes
Sometimes the automated tests will fail with seemingly no reason, or a reason unrelated to the opened PR. In this case, what generally happens is that the GitHub Actions runner that is used has changed, so the environment, or libraries/dependencies have changed. To verify this, it is advised to re-run a check that passed previously to see if it still passes or if it now fails. Then, check the log files to see if/how you can fix the problem, which is usually related to incompatibilities in version numbers of libraries/dependencies.
