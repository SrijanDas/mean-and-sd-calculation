import pandas as pd
import os

path = "D:\\project\\Saving_With_Months\\dataWithMonths"
path = os.path.abspath(path) + '\\'
files = os.listdir(path)

for file_name in files:
    df = pd.read_csv(path + str(file_name))

    unique_months = []
    for i in df['month']:
        if i not in unique_months:
            unique_months.append(i)

    mean_fav_count = []
    mean_retweet_count = []
    mean_tweet_count = []

    sd_fav = []
    sd_retweet = []
    sd_tweet = []
    month = []

    for i in unique_months:
        df2 = df.loc[df['month'] == i]
        df3 = df2.loc[df2['day'] > 15]
        df4 = df2.loc[df2['day'] <= 15]

        mean1 = df3.mean(axis=0)
        sd1 = df3.std(axis=0, skipna=True)
        mean_fav_count.append(mean1.fav_count)
        mean_retweet_count.append(mean1.retweet_count)
        mean_tweet_count.append(mean1.tweet_count)
        sd_fav.append(sd1.fav_count)
        sd_retweet.append(sd1.retweet_count)
        sd_tweet.append(sd1.tweet_count)
        month.append(f"{i} (>15)")

        mean2 = df4.mean(axis=0)
        sd2 = df4.std(axis=0, skipna=True)

        mean_fav_count.append(mean2.fav_count)
        mean_retweet_count.append(mean2.retweet_count)
        mean_tweet_count.append(mean2.tweet_count)
        sd_fav.append(sd2.fav_count)
        sd_retweet.append(sd2.retweet_count)
        sd_tweet.append(sd2.tweet_count)
        month.append(f"{i} (<=15)")

    d = {
        'month(days)': month,
        'mean_like': mean_fav_count,
        'sd_like': sd_fav,
        'mean_retweet': mean_retweet_count,
        'sd_retweet': sd_retweet,
        'mean_tweet': mean_tweet_count,
        'sd_tweet': sd_tweet,
    }

    df2 = pd.DataFrame(data=d)

    output_file = str(file_name).split(".")[0]

    output_path = f"D:\\project\\Saving_With_Months\\output\\{output_file}.csv"
    df2.to_csv(output_path, index=False)
    print(f"{output_file} was created successfully")
