# Converter


Converter is a Python console application for convertation input csv-format file to parquet or back, get schema of parquet file or get help message.

## Installation

Converter requires [Python](https://www.python.org/downloads/)  v3.9+ to run.

Install the librarys and open cmd.
```sh
pip install pyarrow
pip install pandas 
```

```sh
cd converter
converter.py
```


## Features
There are four options of this command application:
--csv2parquet <src-filename> <dst-filename> : conversion mode from csv to parquet format
--parquet2csv <src-filename> <dst-filename> : conversion mode from parquet to csv format
--get-schema <filename> : getting a parquet file scheme
--help : display of help on its use

## Usage
```sh
--get-schema <.../salary.parquet>
''' returns:
ID: int64
  -- field metadata --
  PARQUET:field_id: '1'
Name: string
  -- field metadata --
  PARQUET:field_id: '2'
Salary: double
  -- field metadata --
  PARQUET:field_id: '3'
'''
```

```sh
--csv2parquet <.../salary.csv> <.../salary.parquet>
# go to <.../salary.parquet> and make sure the file is created
```

```sh
--parquet2csv <.../salary.parquet> <.../salary2.csv>
# go to <.../salary.csv> and make sure the file is created
```

```sh
--help
''' returns:
Usage: 
    --help                                          display this help and exit
    --csv2parquet <src-filename> <dst-filename>     converts csv-file from the file             path:(src-filename) to parquet-file with file path:(dst-filename); 
    --parquet2csv <src-filename> <dst-filename>     converts parquet-file from the file path:(src-filename) to csv-file with file path:(dst-filename)
                                                        it allows to enter a separator for data (',' by default) 
    --get-schema <filename>                         returns schema from parquet-file from the file path (filename) 
'''
```
You can also enter an incorrect command or filename, and application will display a corresponding message.

