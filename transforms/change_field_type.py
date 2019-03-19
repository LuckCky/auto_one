from .types_mapping import types_mapping


def change_field_type(data, column_name, new_type):
    for column in column_name:
        col_index = data[0].index(column)
        for line in data[1:]:
            try:
                if new_type == 'float':
                    line[col_index] = types_mapping[new_type](line[col_index].replace(',', '.'))
                else:
                    line[col_index] = types_mapping[new_type](line[col_index])
            except ValueError:
                data.pop(data.index(line))
                print(line)
    return data
