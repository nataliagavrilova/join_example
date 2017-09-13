import sys
import join

table1 = join.read_file(sys.argv[1])
table2 = join.read_file(sys.argv[2])
join.join_and_write_res(table1, table2, sys.argv[3])
