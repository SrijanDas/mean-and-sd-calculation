import pandas as pd
import os


path = "D:\\project\\Saving_With_Months\\data"
path = os.path.abspath(path) + '\\'
files = os.listdir(path)

for file_name in files:
    df = pd.read_csv(path+str(file_name))
    month = []
    day = []
    for i in df['date']:
        month.append(i[3:])
        day.append(int(i[:2]))

    d = {'day': day, 'month': month, 'fav_count': df['Fav_count'], 'retweet_count': df['retweet_count'],
         'tweet_count': df['tweet_count']}

    df2 = pd.DataFrame(data=d)

    output_file = str(file_name).split(".")[0]

    output_path = f"D:\\project\\Saving_With_Months\\dataWithMonths\\{output_file}.csv"
    df2.to_csv(output_path, index=False)
    print(f"{output_file} was created successfully")
