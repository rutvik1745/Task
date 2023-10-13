import csv
# def main():
#     with open('data1.csv',newline='')as csv_file:
#         csv_read = csv.reader(csv_file,delimiter=',')


#         for row in csv_read:
#             print(row)
# if __name__ == '__main__':  
#     main()


with open('data1.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0

    for row in csv_reader:
        if line_count ==0:
            print(f'The column names are as follows: {",".join(row)}')
            line_count +=1

        print(f'\t{row["Name"]} lives in {row["Country"]} department and is {row["Age"]}years old.')
        line_count +=1
print(f'processed {line_count} line.')


import pandas as pd
df = pd.read_csv('data1.csv')

print(df)