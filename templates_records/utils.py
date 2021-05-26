from datetime import datetime

def generate_csv_name(fields, request) -> str:
    filename = ""
    if "id" in fields:
        filename += str(request.user.id) + "_"
    if "username" in fields:
        filename += request.user.username + "_"
    filename += datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    return filename + ".csv"

def change_phone(record, record_fields):
    record = list(record)
    print(record)
    print(record_fields)
    if "phone" in record_fields:
        for field in record:
            try:
                if field.isdigit():
                    record[record.index(field)] = field[:-3] + '***'
            except AttributeError:
                continue
    return record