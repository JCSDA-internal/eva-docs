# Installing Eva

Eva is a Python package and is most easily installed using pip. The package can be cloned using:

```
git clone https://github.com/jcsda-internal/eva eva
```

This will clone the develop branch into a directory called eva.

---
**WARNING**

pip has to create directories where the package will be installed. Sometimes trouble can occur if
default permissions are too strict. If these issues occur try setting:

```
umask 022
```

---

On systems where sudo access is not permitted eva can be installed using:
```
cd eva
pip install --user .
```

To specify the path where eva gets installed supply the prefix argument:
```
cd eva
pip install --prefix=/path/to/install .
```
