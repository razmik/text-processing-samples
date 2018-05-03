from os import listdir
from os.path import isfile, join, isdir
import re
import pandas as pd

root = "E:/Data/20Newsgroups/20news-18828-original"
csv_root = "E:/Data/20Newsgroups/20news-18828-original-csv"
json_root = "E:/Data/20Newsgroups/20news-18828-original-json"
txt_root = "E:/Data/20Newsgroups/20news-18828-original-txt"

unwanted_chars = "!\"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c"

data_list = []
for folder in [f for f in listdir(root) if isdir(join(root, f))]:
    category = folder
    print('processing', category)
    count = 0
    for file in [f for f in listdir(join(root, folder)) if isfile(join(join(root, folder), f))]:
        filename = join(join(root, folder), file)
        with open(filename, 'r') as fl:
            content = fl.read().lower()

            # Extract Sender and Subject
            c_from = re.search('from: (.*)\n', content).group(1).replace('>', '').replace('<', '')
            c_subject = re.sub(r'([^\s\w]|_)+', ' ', re.search('subject: (.*)\n', content).group(1))

            # Clean the body of text
            content = content.replace('from: '+c_from+'\n', ' ').replace('subject: '+c_subject+'\n', ' ').replace('>', ' ').replace('\n', ' ').replace('\n', ' ').replace('\t', ' ').replace('subject', ' ').replace('from', ' ')

            # Strip everything but spaces and alphanumeric
            content = re.sub(r'([^\s\w]|_)+', ' ', content)
            content = re.sub(r'\b\w{1,3}\b', ' ', content)

            # remove multiple dragging characters
            content = re.sub(' +', ' ', content)

            # Limit to 1000 words
            words = content.split(' ')
            if len(words) > 1000:
                content = " ".join(str(x) for x in words[:1000])
            content += " "

            data_list.append([file, c_from, c_subject, content, category])

            if count > 40:
                break
            count += 1

df = pd.DataFrame(data_list, columns=['id', 'from', 'subject', 'body', 'category'])

# Create csv
# df.to_csv(join(csv_root, '20news-18828.csv'), index=None)

# Create text file
df.to_csv(join(txt_root, "newsgroup_combined.txt"), header=False, columns=['body'], index=False, sep=' ', mode='a')

# # Create json objects
# for i in df.index:
#     df.loc[i].to_json(join(json_root, "row{}.json".format(i)))
