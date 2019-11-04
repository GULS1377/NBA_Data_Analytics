# Project Phase 2
# Basic Statistical Analysis and data cleaning insight
import numpy as np
import pandas as pd
from scipy import stats

salary_src_file = 'salary_src.csv'
salary_dst_file = 'salary_dst.xlsx'
player_src_file = 'player_src.csv'
player_dst_file = 'player_dst.csv'
player_career_src_file = 'player_career_src.csv'
player_career_dst_file = 'player_career_dst.xlsx'
player_normalization_dst_file = 'player_normalization_dst.csv'
player_career_normalization_dst_file = 'player_career_normalization_dst.csv'


# clean salary dataset
# remove '$' symbol
def salary_clean(df):
    df['Salary'] = df['Salary'].str.replace('$', '')
    # print(df['Salary'].head(20))
    df.to_excel(salary_dst_file, encoding='utf-8')


# the calculation of mean, median and std for selected attributes of data sets
def mean_median_std(df, columns, dataset_name):
    output_file = 'mean_median_std_' + dataset_name + '.txt'
    with open(output_file, 'w', newline='') as f:
        for column in columns:
            avg = df[column].astype(float).mean().round(2)
            f.write('avg of ' + column + ' is:' + str(avg) + '\n')
            median = df[column].astype(float).median().round(2)
            f.write('median of ' + column + ' is:' + str(median) + '\n')
            std = df[column].astype(float).std().round(2)
            f.write('std of ' + column + ' is:' + str(std) + '\n')
            f.write('-------\n')
        f.write('-------\n')


# normalize selected attributes on 2 dataset
# and export to 'xlsx' files for further analysis
# form 0, normalize player_career dataset
# form 1, normalize play_stats dataset
def normalization(df, columns, form):
    if form == 0:
        start = 1
        output_file = player_career_normalization_dst_file
    else:
        start = 4
        output_file = player_normalization_dst_file
    for column in columns[start:]:
        df[column] = stats.zscore(df[column])
    # print(df[columns].head(5))
    # print('-----')
    df.to_csv(output_file, columns=columns)


# if a player has more than 1 position, only use the 1st priority position
def player_stats_position_remove(df):
    df['Pos'] = df['Pos'].str.replace('-.*', '', regex=True)
    df.to_csv(player_dst_file)


# player_stats dataset clean
def player_stats_clean(df):
    # remove 2nd position
    player_stats_position_remove(df)

# equal-width binning on 'G' (Game Played) attribute into 5 class
def bin_data(df):
    class_type = pd.cut(np.array(df['G']), 5, labels=['Newbie', 'Sophomore', 'Senior', 'Experienced', 'Veteran'])
    df['Class'] = class_type
    df.to_excel(player_career_dst_file)


def main():
    # open salary dataset
    salary_attribute_name = ['Name', 'Season', 'Team', 'League', 'Salary']
    df_salary = pd.read_csv(salary_src_file, names=salary_attribute_name, delimiter=',')

    # open player_stats dataset
    player_attribute_name = ['Name', 'Season', 'Age', 'Tm',	'Lg', 'Pos', 'G', 'GS', 'MP', 'FG',
                             'FGA', 'FG%', '3P', '3PA',	'3P%', '2P', '2PA', '2P%', 'eFG%',
                             'FT', 'FTA', 'FT%', 'ORB', 'DRB', 'TRB', 'AST', 'STL', 'BLK',
                             'TOV', 'PF', 'PTS']
    df_player = pd.read_csv(player_src_file, names=player_attribute_name, delimiter=',')
    # print(df_player.head(20))

    # open player_career_stats dataset
    player_career_attribute_name = ['Name', 'Season', 'Lg', 'G', 'GS', 'MP', 'FG', 'FGA',
                                    'FG%', '3P', '3PA', '3P%', '2P', '2PA', '2P%',
                                    'eFG%', 'FT', 'FTA', 'FT%', 'ORB', 'DRB', 'TRB',
                                    'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS']
    df_player_career = pd.read_csv(player_career_src_file, names=player_career_attribute_name, delimiter=',')

    # remove $ symbol from salary dataset
    salary_clean(df_salary)

    # player stats data set clean
    player_stats_clean(df_player)

    # calculation of mean, median and std for selected attributes on 3 dataset
    mean_median_std(df_salary, ['Salary'], 'salary')
    mean_median_std(df_player, ['G', 'GS', 'MP', 'eFG%',
                                'ORB', 'DRB', 'TRB', 'AST',
                                'STL', 'BLK', 'TOV', 'PTS'], 'player')
    mean_median_std(df_player_career, ['G', 'GS', 'MP', 'eFG%',
                                       'ORB', 'DRB', 'TRB', 'AST',
                                       'STL', 'BLK', 'TOV', 'PTS'], 'player_career')

    # bin the player career stats dataset
    bin_data(df_player_career)

    # normalize 2 dataset: player_stats & player_career_stats
    normalization(df_player, ['Name', 'Season', 'Age', 'Pos', 'G', 'GS', 'MP', 'eFG%',
                              'ORB', 'DRB', 'TRB', 'AST', 'STL', 'BLK', 'TOV', 'PTS'], 1)

    normalization(df_player_career, ['Name', 'G', 'GS', 'MP', 'eFG%',
                                     'ORB', 'DRB', 'TRB', 'AST',
                                     'STL', 'BLK', 'TOV', 'PTS'], 0)


if __name__ == "__main__":
    main()
