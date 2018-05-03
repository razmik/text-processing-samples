"""
dataset _ https://archive.ics.uci.edu/ml/datasets/Health+News+in+Twitter#
"""

from os import listdir
from os.path import isfile, join
import re
import pandas as pd

root = "data"
csv_root = ""
json_root = ""
txt_root = ""

unwanted_chars = "!\"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c"

data_list = []

for file in [f for f in listdir(root) if isfile(join(root, f))]:

    category = file.split('.')[0]
    print('processing', category)
    filename = join(root, file)

    # content_df = pd.read_csv(filename, sep='|')

    with open(filename, 'r', encoding="utf8", errors='ignore') as fl:
        content = fl.readlines()

    # print(category, 'done')
    # continue

    for row in content:

        re_tweet = row.split('|')

        if len(re_tweet) > 2:
            user, twt_time, tweet = re_tweet[0], re_tweet[1], re_tweet[2]
        else:
            continue

        data_list.append([user, twt_time, tweet, category])

df = pd.DataFrame(data_list, columns=['user_id', 'tweet_time', 'tweet', 'source'])

# Create csv
df.to_csv(join(csv_root, 'health_tweets.csv'), index=None)

# Create text file
df.to_csv(join(txt_root, "health_tweets.txt"), header=False, columns=['tweet'], index=False, sep=' ', mode='a')
