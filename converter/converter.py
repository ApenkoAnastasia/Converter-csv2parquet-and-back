import pyarrow.csv as pcv
import pyarrow.parquet as ppq
import pandas as pd

def get_schema(src_adress):
    '''Returns schema from parquet-file from filename.'''


    try: 
        file_schema = ppq.read_schema(src_adress)
    except (IOError, FileNotFoundError):
        print('Wrong src-filename. Cannot read csv-file. Enter [--help] to get access to the information about this console application.')
        exit()
    else:
        return file_schema
    
def transform_csv2parquet(src_adress, dst_adress):
    '''Converts csv-file from the src-filename to parquet-file to dst-filename.'''


    try: 
        table = pcv.read_csv(src_adress)
    except (IOError, FileNotFoundError):
        print('Wrong src-filename. Cannot read csv-file. Enter [--help] to get access to the information about this console application.')
        exit()
    else:
        try:
            ppq.write_table(table, dst_adress)
        except (IOError, FileNotFoundError):
            print('Wrong dst-filename. Cannot write dst-file. Enter [--help] to get access to the information about this console application.')
            exit()
        else:
            parquet_file = ppq.ParquetFile(dst_adress)
               
def transform_parquet2csv(src_adress, dst_adress, separator = ','):
    '''
    
    Converts parquet-file from src-filename to csv-file to dst-filename.

    It allows to enter a separator for data (',' by default). 
    
    '''

    try: 
        df = ppq.read_table(src_adress).to_pandas()
    except (IOError, FileNotFoundError):
        print('Wrong src-filename. Cannot read csv-file. Enter [--help] to get access to the information about this console application.')
        exit()
    else:
        try:
            df.to_csv(
                dst_adress,
                sep = separator,
                index = False,
                mode = 'w',
                line_terminator = '\n',
                encoding = 'utf-8')
        except (IOError, FileNotFoundError):
            print('Wrong dst-filename. Cannot write dst-file. Enter [--help] to get access to the information about this console application.')
            exit()

def get_help():
    '''Returns help message.'''


    helptext = ''' Usage: 
    --help                                          display this help and exit
    --csv2parquet <src-filename> <dst-filename>     converts csv-file from the file path:(src-filename) to parquet-file with file path:(dst-filename); 
    --parquet2csv <src-filename> <dst-filename>     converts parquet-file from the file path:(src-filename) to csv-file with file path:(dst-filename)
                                                        it allows to enter a separator for data (',' by default) 
    --get-schema <filename>                         returns schema from parquet-file from the file path (filename)           
    '''
    return helptext



if __name__ == "__main__":
    input_command = input('Enter command: ')
    if not input_command:
        print('Command is empty.Try again or enter [--help] to get access to the information about this console application.')
        raise Exception()
    else:
        input_command = input_command.split('<')
        if input_command[0].replace('--','').replace(' ','').lower() == 'csv2parquet':
            transform_csv2parquet(input_command[1].split('>')[0], input_command[2].split('>')[0])
        elif input_command[0].replace('--','').replace(' ','').lower() == 'parquet2csv':
            separator = input('Enter separator for csv-file: ')
            if not separator:
                transform_parquet2csv(input_command[1].split('>')[0], input_command[2].split('>')[0])
            else:
                transform_parquet2csv(input_command[1].split('>')[0], input_command[2].split('>')[0], separator)
        elif input_command[0].replace('--','').replace(' ','').lower() == 'get-schema':
            print(get_schema(input_command[1].split('>')[0]))
        elif input_command[0].replace('--','').replace(' ','').lower() == 'help':
            print(get_help())
        else:
            print('Wrong command. Enter [--help] to get access to the information about this console application.')

    