import csv
from pathlib import Path
from tokenize import Number

coinlist_file_path = Path(__file__).with_name('coinlist_data.csv')
# with p.open('r') as f:
#     print(f.read())

# creating a new csv file named SDtokens_5_months
sd_tokens_5_months_path = Path(__file__).with_name('sd_tokens_5_months.csv')
sd_tokens_5_months_file = sd_tokens_5_months_path.open('w')
sd_token_file_writer = csv.writer(sd_tokens_5_months_file)


coinlist_file = coinlist_file_path.open()
coinlist_data = csv.reader(coinlist_file)

header = next(coinlist_data)
# print(header
# ['email', 'Option 1', 'Option 1 SD$', 'SD-option 1', '20% of SD-Option 1', 'Wallet Address', 'Eth Terra', 'Confirmed?', 'Stader Remark', 'Duplicate Wallet Count'])
row_data = []
for rows in coinlist_data:
    row_data.append(rows)

# appending header to csv file
sd_token_header = ['email', 'Wallet Address', 'month1',
                   'month2', 'month3', 'month4', 'month5', 'total']
sd_token_file_writer.writerow(sd_token_header)

# print(sd_tokens_5_months_file.read())

# appending rows
for curr_row in row_data:
    temp_row = []
    temp_row.append(curr_row[0])
    temp_row.append(curr_row[5])
    monthly_reward = str(float(curr_row[3]) / 5)
    for j in range(5):
        temp_row.append(monthly_reward)
    temp_row.append(curr_row[3])
    # print(temp_row)
    sd_token_file_writer.writerow(temp_row)

# print(row_data)
