# Documentation



## Contributing to Eva Docs

To contribute to the eva documentation website, create a branch with your changes, and then submit a pull request to the eva-docs repository: [https://github.com/JCSDA-internal/eva-docs](https://github.com/JCSDA-internal/eva-docs)


## Local Eva Docs Build

It may be useful to build the website locally to ensure that any changes are properly displayed on the website before submitting a pull request.

Creating a conda environment is recommended, but not required. The dependencies for nbsite tend to be tricky, and having a pre-existing environment with other package versions may cause the build to not work.

### Steps for locally building and viewing website:

NOTE: git-lfs needs to be installed to be able to clone notebooks from the eva-docs repository. If you make a self-contained environment, you may need to run `conda install git`, `conda install git-lfs`, and `git lfs install`. Then, reclone the eva-docs repository.

1. Clone eva and eva-docs directories
        - eva - https://github.com/JCSDA-internal/eva
        - eva-docs - https://github.com/JCSDA-internal/eva-docs
2. `cd eva-docs`
3. Set up dependencies for eva-docs
        - To do this in a self-contained environment (recommended):
                - `conda env create -f environment.yaml`
                - `conda activate eva-docs`
        - To add dependencies to current environment:
                - `pip install -r requirements-github.txt`
6. Install eva to run jupyter notebooks: `pip install ../eva`
7. Generate the .rst files for the jupyter notebooks: `nbsite generate-rst --org JCSDA-internal --project-name eva-docs --examples notebooks`
8. Create API docs with this command: `sphinx-apidoc -o doc/API/ ../eva/src`
9. API documentation setup: `python doc/api_setup.py doc/API/`
10. Build site: `nbsite build`
11. `cd builtdocs`
12. Run `python -m http.server 8000` to start local server
13. Type `localhost:8000` into a web browser to view the website



## API Docs

To contribute to the eva API documentation, create a branch in eva and write comments directly into the source code, making sure that they adhere to Google-standard docstrings. Then, submit a pull request to eva using this branch. Sphinx-based tools will autogenerate the comments into documentation for the website.
