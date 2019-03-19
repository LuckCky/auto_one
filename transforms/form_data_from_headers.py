def form_data_from_headers(data, headers, separator):
    headers = headers.split(separator)
    indexes = []
    for header in headers:
        indexes.append(data[0].index(header))
    formed_data = [[] for _ in range(len(data))]
    for i in range(len(data)):
        for index in indexes:
            formed_data[i].append(data[i][index])
    return formed_data
