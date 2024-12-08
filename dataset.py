import csv

with open('dataset.csv', mode='r', newline='', encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file)
    
    with open('dataset.txt', mode='w', encoding='utf-8') as txt_file:
        for row in csv_reader:
            txt_file.write('\t'.join(row) + '\n')

print("CSV contents saved to output.txt with tab separation.")