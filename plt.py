# Project Phase 2
# Histograms and Correlations
import pandas as pd
import matplotlib.pyplot as plt


def hist():
    # part 1 # Use a histogram to plot at least three of the variables
    # read data from file and pick up attributes for histogram
    player_src_file = 'player_dst.csv'
    columns = ['Name', 'Pos', 'G', 'eFG%', 'TRB', 'AST', 'BLK', 'TOV', 'PF', 'PTS']
    df = pd.read_csv(player_src_file)
    df = df[columns]

    # create a data frame to save data after calculating mean
    df_plt = pd.DataFrame()

    # use player position to group the data
    # gp_col = 'Pos'
    position = ['C', 'PF', 'PG', 'SF', 'SG']

    # choose 7 attributes from data frame to plot 7 histograms
    for column in columns[3:10]:
        i = 0
        # calculate mean for each attribute of different position
        df_mean = df.groupby('Pos').mean()[column]
        # print(type(df_mean))
        # add mean to data frame prepared for plotting
        df_plt.insert(i, column, df_mean)
        # define the x-axis and y-axis
        plt.bar(x=position, height=df_plt[column])
        # histogram title
        plt.title('AVG ' + column + ' for different positions')
        # show histogram
        plt.show()
        i += 1


def scatter():
    # part 2 # use scatter plot to show the correlation between attributes #
    # to show the relation between season and player's mean salary
    # read salary dataset to data frame and choose 2 useful attributes
    salary_src_file = 'salary_dst.xlsx'
    salary_columns = ['Season', 'Salary']
    df_salary = pd.read_excel(salary_src_file)
    df_salary = df_salary[salary_columns]
    # print(df_salary)

    # group by 'season' to get average player's salary for a season
    salary_mean = df_salary.groupby('Season').mean()['Salary']
    # group by 'season' to get the number of records for this season
    salary_season_count = df_salary.groupby('Season').count()
    # create new data frame including season, avg_salary, record_count
    salary_mean_plt = pd.DataFrame()
    salary_mean_plt.insert(0, 'Season', salary_mean.index)
    salary_mean_plt.insert(1, 'Avg Salary', salary_mean.values)
    salary_mean_plt.insert(2, 'Record Count', salary_season_count.values)

    # use the scatter plot to show the relation between average salary and season
    plt.scatter(salary_mean_plt['Avg Salary'], salary_mean_plt['Season'], color='b')
    plt.title('Avg Salary and Season')
    plt.xlabel('Avg Salary')
    plt.ylabel('Season')
    plt.show()
    plt.clf()

    # use the scatter plot to show the relation between the number of records and season
    plt.scatter(salary_mean_plt['Record Count'], salary_mean_plt['Season'], color='b')
    plt.title('Record Count and Season')
    plt.xlabel('Record Count')
    plt.ylabel('Season')
    plt.show()
    plt.clf()


def main():
    # suppress the scientific notation
    pd.set_option('display.float_format', lambda x: '%.3f' % x)

    # part 1 # Use a histogram to plot at least three of the variables
    hist()

    # part 2 # use scatter plot to show the correlation between attributes #
    # to show the relation between season and player's mean salary
    scatter()


if __name__ == "__main__":
    main()
