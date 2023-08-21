# Batch Plotting and Using EMCPy Backend for eva

In addition to the `datasets` and `transforms` section within the configuration YAMLs used within eva, there is a `graphics` section. This section is used to design the figures needed during analysis of your data using EMCPy's plotting backend. 

An example of a `graphics` section from a test configuration file for both a scatter plot and map scatter plot is shown below:

```
graphics:

  # Scatter plot
  # ------------

  # JEDI h(x) vs Observations
  - batch figure:
      variables: *variables
    figure:
      layout: [1,1]
      title: 'Observations vs. JEDI h(x) | Aircraft | ${variable_title}'
      output name: observation_scatter_plots/aircraft/${variable}/jedi_hofx_vs_obs_aircraft_${variable}.png
    plots:
      - add_xlabel: 'Observation Value'
        add_ylabel: 'JEDI h(x)'
        add_grid:
        add_legend:
          loc: 'upper left'
        layers:
        - type: Scatter
          x:
            variable: experiment::ObsValue::${variable}
          y:
            variable: experiment::hofx::${variable}
          markersize: 5
          color: 'black'
          label: 'JEDI h(x) versus obs (all obs)'
        - type: Scatter
          x:
            variable: experiment::ObsValue::${variable}
          y:
            variable: experiment::hofxPassedQc::${variable}
          markersize: 5
          color: 'red'
          label: 'JEDI h(x) versus obs (passed QC in JEDI)'

  # Map plot
  # ---------

  # Observations
  - batch figure:
      variables: *variables
    dynamic options:
      - type: vminvmaxcmap
        data variable: experiment::ObsValue::${variable}
    figure:
      figure size: [20,10]
      layout: [1,1]
      title: 'Observations | Aircraft | Obs Value'
      output name: map_plots/aircraft/${variable}/observations_aircraft_${variable}.png
    plots:
      - mapping:
          projection: plcarr
          domain: global
        add_map_features: ['coastline']
        add_colorbar:
          label: ObsValue
        add_grid:
        layers:
        - type: MapScatter
          longitude:
            variable: experiment::MetaData::longitude
          latitude:
            variable: experiment::MetaData::latitude
          data:
            variable: experiment::ObsValue::${variable}
          markersize: 2
          label: ObsValue
          colorbar: true
          cmap: ${dynamic_cmap}
          vmin: ${dynamic_vmin}
          vmax: ${dynamic_vmax}
            
```

## Batch Figure

Given the variables selected in the `datasets` section of the configuration yaml, the user can create batch figures for all variables selected. In this example, a scatter plot and map plot will be created for all the variables the user selected to be analyzed.

```
  - batch figure:
      variables: *variables
```

If the dataset included radiance data, the user could indicate specific channels and include them in the batch figure section to create plots for all variables and channels selected.

```
  - batch figure:
      variables: *variables
      channels: *channels
```

## EMCPy Design

EMCPy's declarative plotting design is separated into three sections: 
 * figure
 * plots
 * layers

Each section is responsible for different parts of the figure design which are explained below.

### Figure

This section is responsible for the high-level figure design such as the layout of subplots, the figure title, figure size, output filename and more. 

```
    figure:
      figure size: [20,10]
      layout: [1,1]
      title: 'Observations | Aircraft | Obs Value'
      output name: map_plots/aircraft/${variable}/observations_aircraft_${variable}.png
```

### Plots

This section adds individual plot features such as adding x and y labels, legends, colorbars, mapping information, grids, etc. These follow [matplotlib](https://matplotlib.org/stable/index.html) conventions and can include specific inputs that the matplotlib functions accept.

```
    plots:
      - add_xlabel: 'Observation Value'
        add_ylabel: 'JEDI h(x)'
        add_grid:
        add_legend:
          loc: 'upper left'
```
Above would add x and y labels, a grid, and a legend located in the upper left part of the subplot for a standard plot.

```
    plots:
      - mapping:
          projection: plcarr
          domain: global
        add_map_features: ['coastline']
        add_colorbar:
          label: ObsValue
        add_grid:
```
This would be an example of adding mapping information such as `projection` and `domain` when creating a map plot. `add_map_features` adds feature attributes which can be found on the [Cartopy website](https://scitools.org.uk/cartopy/docs/latest/reference/feature.html#feature-attributes).

### Layers

Within this section, the user will define the plot type, the input data (such as x and y for standard plots or latitude and longitude for map plots), and how the user would like to present that data. This includes design inputs such as color, labels, data limits, or the style of the lines or markers. 

```
        layers:
        - type: Scatter
          x:
            variable: experiment::ObsValue::${variable}
          y:
            variable: experiment::hofx::${variable}
          markersize: 5
          color: 'black'
          label: 'JEDI h(x) versus obs (all obs)'
        - type: Scatter
          x:
            variable: experiment::ObsValue::${variable}
          y:
            variable: experiment::hofxPassedQc::${variable}
          markersize: 5
          color: 'red'
          label: 'JEDI h(x) versus obs (passed QC in JEDI)'
```

The above example is plotting two layers of scatter plot data on a single subplot. The first layer compares experiment::ObsValue::${variable} as the x values and variable: experiment::hofx::${variable} as the y values using black dots and adding the appropriate label. The second layer uses different data in red and adds a label as well.

```
        - type: MapScatter
          longitude:
            variable: experiment::MetaData::longitude
          latitude:
            variable: experiment::MetaData::latitude
          data:
            variable: experiment::ObsValue::${variable}
          markersize: 2
          label: ObsValue
          colorbar: true
          cmap: ${dynamic_cmap}
          vmin: ${dynamic_vmin}
          vmax: ${dynamic_vmax}
```

This example plots scatter data on a map with longitude, latitude, and data inputs. It also includes a label and colorbar options. Eva also includes dynamic configuration options in its plotting tools for `cmap`, `vmin` and `vmax`.

## Examples

For more examples on how to use the graphics section within the configuration YAMLs and plotting options, there are test configuration files found on [eva's Github page](https://github.com/JCSDA-internal/eva/tree/develop/src/eva/tests/config).