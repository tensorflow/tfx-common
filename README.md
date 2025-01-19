# TFX Basic Shared Libraries

[![Python](https://img.shields.io/badge/python%7C3.9%7C3.10%7C3.11-blue)](https://github.com/tensorflow/tfx-bsl)
[![PyPI](https://badge.fury.io/py/tfx-bsl.svg)](https://badge.fury.io/py/tfx-bsl)

TFX Basic Shared Libraries (`tfx_bsl`) contains libraries shared by many
[TensorFlow eXtended (TFX)](https://www.tensorflow.org/tfx) components.

__Only symbols exported by sub-modules under `tfx_bsl/public` are intended for
direct use by TFX users__, including by standalone TFX library (e.g. TFDV, TFMA,
TFT) users, TFX pipeline authors and TFX component authors. Those APIs will
become stable and follow semantic versioning once `tfx_bsl` goes beyond `1.0`.

APIs under other directories should be considered internal to TFX
(and therefore there is no backward or forward compatibility guarantee for
them).

Each minor version of a TFX library or TFX itself, if it needs to
depend on `tfx_bsl`, will depend on a specific minor version of it (e.g.
`tensorflow_data_validation` 0.14.\* will depend on, and only work with,
`tfx_bsl` 0.14.\*)

## Installing from PyPI

`tfx_bsl` is available as a [PyPI package](https://pypi.org/project/tfx-bsl/).

```bash
pip install tfx-bsl
```

### Nightly Packages

TFX-BSL also hosts nightly packages at https://pypi-nightly.tensorflow.org on
Google Cloud. To install the latest nightly package, please use the following
command:

```bash
pip install --extra-index-url https://pypi-nightly.tensorflow.org/simple tfx-bsl
```

This will install the nightly packages for the major dependencies of TFX-BSL
such as TensorFlow Metadata (TFMD).

However it is a dependency of many TFX components and usually as a user you
don't need to install it directly.

## Build with Docker

If you want to build a TFX component from the master branch, past the latest
release, you may also have to build the latest `tfx_bsl`, as that TFX component
might have depended on new features introduced past the latest `tfx_bsl`
release.

Building from Docker is the recommended way to build `tfx_bsl` under Linux,
and is continuously tested at Google.

### 1. Install Docker

Please first install [`docker`](https://docs.docker.com/install/) and
[`docker-compose`](https://docs.docker.com/compose/install/) by following the
directions.

### 2. Clone the `tfx_bsl` repository

```shell
git clone https://github.com/tensorflow/tfx-bsl
cd tfx-bsl
```

Note that these instructions will install the latest master branch of `tfx-bsl`.
If you want to install a specific branch (such as a release branch), pass
`-b <branchname>` to the `git clone` command.

### 3. Build the pip package

Then, run the following at the project root:

```bash
sudo docker-compose build manylinux2010
sudo docker-compose run -e PYTHON_VERSION=${PYTHON_VERSION} manylinux2010
```
where `PYTHON_VERSION` is one of `{39}`.

A wheel will be produced under `dist/`.

### 4. Install the pip package

```shell
pip install dist/*.whl
```

## Build from source

### 1. Prerequisites

#### Install NumPy

If NumPy is not installed on your system, install it now by following [these
directions](https://numpy.org/install/).

#### Install Bazel

If Bazel is not installed on your system, install it now by following [these
directions](https://bazel.build/versions/master/docs/install.html).


### 2. Clone the `tfx_bsl` repository

```shell
git clone https://github.com/tensorflow/tfx-bsl
cd tfx-bsl
```

Note that these instructions will install the latest master branch of `tfx_bsl`
If you want to install a specific branch (such as a release branch),
pass `-b <branchname>` to the `git clone` command.

### 3. Build the pip package

`tfx_bsl` wheel is Python version dependent -- to build the pip package that
works for a specific Python version, use that Python binary to run:
```shell
python setup.py bdist_wheel
```

You can find the generated `.whl` file in the `dist` subdirectory.

### 4. Install the pip package

```shell
pip install dist/*.whl
```

## Supported platforms

`tfx_bsl` is tested on the following 64-bit operating systems:

  * macOS 10.12.6 (Sierra) or later.
  * Ubuntu 20.04 or later.

## Compatible versions

The following table is the `tfx_bsl` package versions that are compatible with
each other. This is determined by our testing framework, but other *untested*
combinations may also work.

tfx-bsl                                                                         | apache-beam[gcp] | pyarrow  | tensorflow        | tensorflow-metadata | tensorflow-serving-api |
------------------------------------------------------------------------------- | -----------------| ---------|-------------------|---------------------|------------------------|
[GitHub master](https://github.com/tensorflow/tfx-bsl/blob/master/RELEASE.md)   | 2.59.0           | 10.0.1   | nightly (2.x)     | 1.16.1              | 2.16.1
[1.16.1](https://github.com/tensorflow/tfx-bsl/blob/v1.16.1/RELEASE.md)         | 2.59.0           | 10.0.1   | 2.16              | 1.16.1              | 2.16.1                |
[1.16.0](https://github.com/tensorflow/tfx-bsl/blob/v1.16.0/RELEASE.md)         | 2.59.0           | 10.0.1   | 2.16              | 1.16.0              | 2.16.1
[1.15.1](https://github.com/tensorflow/tfx-bsl/blob/v1.15.1/RELEASE.md)         | 2.47.0           | 10.0.0   | 2.15              | 1.15.0              | 2.15.1                 |
[1.15.0](https://github.com/tensorflow/tfx-bsl/blob/v1.15.0/RELEASE.md)         | 2.47.0           | 10.0.0   | 2.15              | 1.15.0              | 2.15.1                 |
[1.14.0](https://github.com/tensorflow/tfx-bsl/blob/v1.14.0/RELEASE.md)         | 2.47.0           | 10.0.0   | 2.13              | 1.14.0              | 2.13.0                 |
[1.13.0](https://github.com/tensorflow/tfx-bsl/blob/v1.13.0/RELEASE.md)         | 2.40.0           | 6.0.0    | 2.12              | 1.13.1              | 2.9.0                  |
[1.12.0](https://github.com/tensorflow/tfx-bsl/blob/v1.12.0/RELEASE.md)         | 2.40.0           | 6.0.0    | 2.11              | 1.12.0              | 2.9.0                  |
[1.11.0](https://github.com/tensorflow/tfx-bsl/blob/v1.11.0/RELEASE.md)         | 2.40.0           | 6.0.0    | 1.15 / 2.10       | 1.11.0              | 2.9.0                  |
[1.10.0](https://github.com/tensorflow/tfx-bsl/blob/v1.10.0/RELEASE.md)         | 2.40.0           | 6.0.0    | 1.15 / 2.9        | 1.10.0              | 2.9.0                  |
[1.9.0](https://github.com/tensorflow/tfx-bsl/blob/v1.9.0/RELEASE.md)           | 2.38.0           | 5.0.0    | 1.15 / 2.9        | 1.9.0               | 2.9.0                  |
[1.8.0](https://github.com/tensorflow/tfx-bsl/blob/v1.8.0/RELEASE.md)           | 2.38.0           | 5.0.0    | 1.15 / 2.8        | 1.8.0               | 2.8.0                  |
[1.7.0](https://github.com/tensorflow/tfx-bsl/blob/v1.7.0/RELEASE.md)           | 2.36.0           | 5.0.0    | 1.15 / 2.8        | 1.7.0               | 2.8.0                  |
[1.6.0](https://github.com/tensorflow/tfx-bsl/blob/v1.6.0/RELEASE.md)           | 2.35.0           | 5.0.0    | 1.15 / 2.7        | 1.6.0               | 2.7.0                  |
[1.5.0](https://github.com/tensorflow/tfx-bsl/blob/v1.4.0/RELEASE.md)           | 2.34.0           | 5.0.0    | 1.15 / 2.7        | 1.5.0               | 2.7.0                  |
[1.4.0](https://github.com/tensorflow/tfx-bsl/blob/v1.4.0/RELEASE.md)           | 2.31.0           | 5.0.0    | 1.15 / 2.6        | 1.4.0               | 2.6.0                  |
[1.3.0](https://github.com/tensorflow/tfx-bsl/blob/v1.3.0/RELEASE.md)           | 2.31.0           | 2.0.0    | 1.15 / 2.6        | 1.2.0               | 2.6.0                  |
[1.2.0](https://github.com/tensorflow/tfx-bsl/blob/v1.2.0/RELEASE.md)           | 2.31.0           | 2.0.0    | 1.15 / 2.5        | 1.2.0               | 2.5.1                  |
[1.1.0](https://github.com/tensorflow/tfx-bsl/blob/v1.1.0/RELEASE.md)           | 2.29.0           | 2.0.0    | 1.15 / 2.5        | 1.1.0               | 2.5.1                  |
[1.0.0](https://github.com/tensorflow/tfx-bsl/blob/v1.0.0/RELEASE.md)           | 2.29.0           | 2.0.0    | 1.15 / 2.5        | 1.0.0               | 2.5.1                  |
[0.30.0](https://github.com/tensorflow/tfx-bsl/blob/v0.30.0/RELEASE.md)         | 2.28.0           | 2.0.0    | 1.15 / 2.4        | 0.30.0              | 2.4.0                  |
[0.29.0](https://github.com/tensorflow/tfx-bsl/blob/v0.29.0/RELEASE.md)         | 2.28.0           | 2.0.0    | 1.15 / 2.4        | 0.29.0              | 2.4.0                  |
[0.28.0](https://github.com/tensorflow/tfx-bsl/blob/v0.28.0/RELEASE.md)         | 2.28.0           | 2.0.0    | 1.15 / 2.4        | 0.28.0              | 2.4.0                  |
[0.27.1](https://github.com/tensorflow/tfx-bsl/blob/v0.27.1/RELEASE.md)         | 2.27.0           | 2.0.0    | 1.15 / 2.4        | 0.27.0              | 2.4.0                  |
[0.27.0](https://github.com/tensorflow/tfx-bsl/blob/v0.27.0/RELEASE.md)         | 2.27.0           | 2.0.0    | 1.15 / 2.4        | 0.27.0              | 2.4.0                  |
[0.26.1](https://github.com/tensorflow/tfx-bsl/blob/v0.26.1/RELEASE.md)         | 2.25.0           | 0.17.0   | 1.15 / 2.3        | 0.27.0              | 2.3.0                  |
[0.26.0](https://github.com/tensorflow/tfx-bsl/blob/v0.26.0/RELEASE.md)         | 2.25.0           | 0.17.0   | 1.15 / 2.3        | 0.27.0              | 2.3.0                  |
