import datetime


def read_file(path_to_table):
    """Reads csv file into dictionary.

    :type path_to_res_table: str
    :param path_to_res_table: path where to read data.

    :rtype: dict
    :return: data read from csv in dict format.
    """
    d = {}
    i = 0
    with open(path_to_table) as f:
        for line in f:
        #do not read header to dictionary
            if i == 0:
                pass
                i += 1
            else:
                try:
                    (key, val) = line.strip('\n').split(sep=',')
                    d[int(key)] = val
                except:
                    (val, key) = line.strip('\n').split(sep=',')
                    d[int(key)] = val
            i += 1
    print('{:%Y-%m-%d %H:%M:%S.%f}'.format(datetime.datetime.now()) + \
          ' Read ' + str(i) + ' lines from files ' + path_to_table + '.')
    return d


def join_and_write_res(table1, table2, path_to_res_table):
    """Perfoms SQL-like join and writes result to text file.

    :type table1: dict
    :param table1: first dictionary to join.

    :type table2: dict
    :param table2: second dictionary to join.

    :type path_to_res_table: str
    :param path_to_res_table: path where to write result.

    :rtype: nothing
    :return: nothing if successfull, otherwise - standard error.
    """
    print('{:%Y-%m-%d %H:%M:%S.%f}'.format(datetime.datetime.now()) + \
          ' started joining.')
    keys_a = set(table1.keys())
    keys_b = set(table2.keys())
    intersection = keys_a & keys_b
    res_table = []
    print('{:%Y-%m-%d %H:%M:%S.%f}'.format(datetime.datetime.now()) + \
          ' end joining.')

    with open(path_to_res_table, 'w') as f:
        f.write('t1_name,t2_name,id\n')
        for i in intersection:
            f.write(str(table1[i]) + ',' + \
                    str(table2[i]) + ',' + str(i) + '\n')
