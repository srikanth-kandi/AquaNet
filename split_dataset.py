import pandas as pd
import json


def split_data_into_binary_and_single_word_answers(csv_file, split):
    csv_data = pd.read_csv(csv_file, encoding='latin1', usecols=['file_name', 'QuestionText', 'answer' ])

    csv_data['answer'] = csv_data['answer'].str.upper()

    select = ['YES', 'NO']
    data_single_word = csv_data[~csv_data['answer'].isin(select)]
    data_binary = csv_data[csv_data['answer'].isin(select)]

    with open('/content/AquaNet/dataset/metadata/single_word_{}.csv'.format(split), 'wb') as f:
        data_single_word.to_csv(f, index=False)
    
    with open('metadata\\binary_{}.csv'.format(split), 'wb') as f:
        data_binary.to_csv(f, index=False)


csv_file_train = '/content/AquaNet/dataset/metadata/clotho_aqa_train.csv'
csv_file_val = '/content/AquaNet/dataset/metadata/clotho_aqa_val.csv'
csv_file_test = '/content/AquaNet/dataset/metadata/clotho_aqa_test.csv'

split_data_into_binary_and_single_word_answers(csv_file_train, 'train')
split_data_into_binary_and_single_word_answers(csv_file_val, 'val')
split_data_into_binary_and_single_word_answers(csv_file_test, 'test')

# create word-index for single word answers
csv_file = '/content/AquaNet/dataset/metadata/single_word_train.csv'
csv_data = pd.read_csv(csv_file, encoding='latin1', usecols=['file_name', 'QuestionText', 'answer'])

csv_data['answer'] = csv_data['answer'].str.upper()

answers_set = set(list(csv_data['answer']))
answers_dict = dict(zip(answers_set, range(len(answers_set))))

with open("/content/AquaNet/dataset/metadata/output_classes.json", "w") as outfile:
    json.dump(answers_dict, outfile)
