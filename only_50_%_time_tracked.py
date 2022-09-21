import os
from pathlib import Path
from tkinter import filedialog
import pandas as pd


data_root = filedialog.askdirectory()


for rootdir, dirs, files in os.walk(data_root):

    processed_root = rootdir +  "/tracks_processed/"
    for file in files:
        Path(rootdir + "/tracks_processed/").mkdir(parents=True, exist_ok=True)
        if file.endswith(".txt") == True:
            print(file)
            df = pd.read_csv(os.path.join(rootdir,file), delimiter="\t")
            df = df.rename(columns={"Track ": "Track"})
            df = df.set_index('Track')
            selected_columns = df[["#Frames", "time(s)", "Bends"]]
            df2 = selected_columns.copy()
            df2['BBPS'] = df['Bends'].div(df['time(s)'], axis=0)
            df2['BBPM'] = df2['BBPS'] * 60
            df2['-'] = ''
            df2['mean (BBPM)'] = df2['BBPM'].mean()
            df2['mean (BBPM)'] = df2['mean (BBPM)'].drop_duplicates()
            df2['SEM'] = df2['BBPM'].sem()
            df2['SEM'] = df2['SEM'].drop_duplicates()
            df2['n'] = len(df2['BBPM'])
            df2['n'] = df2['n'].drop_duplicates()

            # Get maximum time tracked and only keep
            # tracks that have been tracked 50% of the maximum time.
            column = df['time(s)']
            max_value = column.max()
            threshold_value = max_value * 0.5
            df3 = df2.copy()
            df3.drop(df3.loc[df3['time(s)'] <= threshold_value].index, inplace=True)
            df3['-'] = ''
            df3['mean (BBPM)'] = df3['BBPM'].mean()
            df3['mean (BBPM)'] = df3['mean (BBPM)'].drop_duplicates()
            df3['SEM'] = df3['BBPM'].sem()
            df3['SEM'] = df3['SEM'].drop_duplicates()
            df3['n'] = len(df3['BBPM'])
            df3['n'] = df3['n'].drop_duplicates()

            # Saving processed track file to new directory "tracks_processed"
            with pd.ExcelWriter(processed_root + file.rsplit('.', maxsplit=1)[0] + "_processed.xlsx") as writer:
                df3.to_excel(writer, sheet_name='>50%_tracked_swimming_cycles')
                df2.to_excel(writer, sheet_name='all_swimming_cycles')
                df.to_excel(writer, sheet_name='all_data')

            print("Saving processed tracks as " + file.rsplit('.', maxsplit=1)[0] + "_processed.xlsx ... Done!")
