
# DSRF Conformance Checker

THIS IS AN EXPERIMENTAL PACKAGE. DSRF PACKAGE HASN'T BEEN UPDATED SINCE 2020
## Overview

The DSRF Conformance Checker is a tool designed and prepared by DDEX. The oryginal tool verifies the conformance of a Digital Sales Report Format (DSRF) file using Perl. The application validates input files against a conformance profile using Google's `dsrf` library. We re-writed this Perl script using Python.

### Features
- Supports checking multiple DSRF files at once
- Validates files and ensures they conform to the profile
- Automatically removes log files upon completion
- Outputs results into a `.log` file for review

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/bravelab/mtl-ddex-flatfilevalidator.git
   cd mtl-ddex-flatfilevalidator
   ```

2. Install dependencies using Poetry:
   ```bash
   poetry install
   ```

3. Install required dependencies for handling `.proto` files:
   ```bash
   poetry add protobuf
   ```

4. Install the `dsrf` library:
   If you are pulling the DSRF library from GitHub:
   ```bash
   poetry add git+https://github.com/ddexnet/dsrf.git
   ```

5. Ensure `protoc` is installed for generating the required `*_pb2.py` files:
   ```bash
   brew install protobuf
   ```

## Usage

To run the DSRF conformance checker, use the following command:
```bash
poetry run dsrf-conf <file1> <file2> ...
```

### Example

```bash
poetry run dsrf-conf dsrf_file1.txt dsrf_file2.txt
```

The script will validate the input files and output the results to a log file located in the same directory as the input files.

## Development

### Generate Python code from .proto files

To generate Python code for protocol buffer files (if needed), run:
```bash
protoc --python_out=. *.proto
```

This will create the required `_pb2.py` files for use in the project.

## Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Make your changes
4. Push your changes to the branch (`git push origin feature-branch`)
5. Create a new Pull Request

## License

This project is licensed under the MIT License. See the LICENSE file for details.
