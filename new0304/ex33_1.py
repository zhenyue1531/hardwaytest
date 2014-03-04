
def insert_list(begin, update,times):
	data = begin
	i = 0
	for i in range(0, times):
		numbers.append(data)
		i = i + 1
		data = data + update

numbers = []
insert_begin = int(raw_input("begin number?"))
insert_update = int(raw_input("update number?"))
insert_times = int(raw_input("run times?"))
insert_list(insert_begin, insert_update,insert_times)
print numbers	