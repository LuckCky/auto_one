from .column_mapping import column_mapping


def convert_field_to_num(data, column):
    column_index = data[0].index(column)
    for line in data[1:]:
        line[column_index] = column_mapping[column][line[column_index]]
    return data
