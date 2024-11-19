import csv
import zipfile
import json

def main():
    parse_csv('visit_log__1_.csv')

def parse_csv(file_path : str):
    #archive = zipfile.ZipFile('purchase_log.zip', 'r')
    #log_file = archive.open('purchase_log.txt')
    result_list = []

    with open(file_path, 'r') as csv_file:
        reader = csv.reader(csv_file)
        with open('purchase_log.txt', 'r') as log_file:

            for row in reader:
                for json_row in log_file:
                    json_data = json.loads(json_row)
                    if json_data['user_id'] == row[0]:
                        result_list.append(f"{row},{json_data['category']}")



    with open('funnel.csv', 'w') as result_file:
        for row in result_list:
            result_file.write(row)

main()
