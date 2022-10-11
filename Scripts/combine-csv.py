import os
import glob
import pandas as pd

os.chdir('C:/Users/karen/PycharmProjects/ycng228-project/.data')
extension = 'csv'
filenames = [i for i in glob.glob('*.{}'.format(extension))]

combined_pd = pd.concat([pd.read_csv(f) for f in filenames])

combined_pd.to_csv("_SP500_data_all.csv" , index=False , encoding='utf-8-sig')

print('Done!')


