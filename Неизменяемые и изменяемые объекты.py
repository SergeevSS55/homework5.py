immutable_var = 1, 2, True, 'string', [1, 2, 3, 4]
print(immutable_var)

immutable_var_ = (1, 2, True, 'string', [1, 2, 3, 4])
immutable_var_ [4][2] = 77
print(immutable_var_)
#immutable_var_ [0] = 77 выдаст ошибку, поскольку характерный
# признаком кортежа является его неизменяемость, также к признакам можно отнести упорядочность
# и разнообразность типов
mutable_list = [1, 2, 3, True, 'string']
mutable_list.append('student')
mutable_list.extend('1234')
mutable_list.extend(['1234', 'orange'])
mutable_list[-1] = 'apple'.upper()
mutable_list.remove(1)
print('apple' in mutable_list, 'Shortlist: ' + str(mutable_list))