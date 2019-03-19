from transforms.change_field_type import change_field_type
from transforms.clean import clean
from transforms.convert_field_to_num import convert_field_to_num
from transforms.form_data_from_headers import form_data_from_headers
from transforms.one_hot_encode import one_hot_encode

transforms_mapping = {
    'change_field_type': change_field_type,
    'clean': clean,
    'convert_field_to_num': convert_field_to_num,
    'form_data_from_headers': form_data_from_headers,
    'one_hot_encode': one_hot_encode
}
