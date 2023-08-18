# Use of existing installs of eva on supported HPC platforms

## Hera
To load the maintained eva environment on Hera:
``` bash
module use /scratch1/NCEPDEV/da/python/opt/modulefiles/stack
module load hpc/1.2.0 miniconda3/4.6.14 eva/1.0.0
```

For any issues, please contact `cory.r.martin@noaa.gov`

## Orion
To load the maintained eva environment on Orion:

``` bash
module use /work2/noaa/da/python/opt/modulefiles/stack
module load hpc/1.2.0 miniconda3/4.6.14 eva/1.0.0
```

For any issues, please contact `cory.r.martin@noaa.gov`

## Discover
To load the maintained eva environment on Discover:

First, you need to use the modulefiles stack. You can do this by running the following command:

``` bash
module use -a /discover/nobackup/drholdaw/opt/modulefiles/core
```

Next, load the necessary modules. You can do this by running the following command:

``` bash
module load miniconda/py39_23.3.1 
module load eva
```

Please note that the version of eva loaded using these modules may vary and be updated from time to time.


