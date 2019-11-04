# Project Phase 2
# Additional Part for CS Students
import pandas as pd
from sklearn.neighbors import LocalOutlierFactor


# run LOF to find outliers
def run_lof(k):
    # read player career stats file
    player_career_file = 'player_career_normalization_dst.csv'
    df_player = pd.read_csv(player_career_file)
    # print(df_player.head(10))

    # create LOF deduction instance
    clf = LocalOutlierFactor(n_neighbors=k, contamination=0.1)

    # choose attributes included in LOF calculation
    x = df_player.iloc[:, 5:]
    # print(x.head(10))

    # change data frame to 2D array
    x = x.values

    # run LOF
    y_pred = clf.fit_predict(x)
    # print(y_pred)

    # lof_scores = clf.negative_outlier_factor_
    # print(lof_scores)
    return y_pred

# using 3 different k-value and cross-check the result to determine the outlier
def lof():
    # 3 k-value for LOF
    lof_k = [200, 100, 50]
    # outlier list for the 3 LOF running
    outlier_list = [[], [], []]
    # run LOF with 3 different k-value
    for i, j in zip(lof_k, range(0, len(outlier_list))):
        outlier_list[j] = run_lof(i)

    # if one player appears in all 3 lof running
    # save his row number to outlier result
    outlier_result = []
    l = len(outlier_list[0])
    for i in range(0, l):
        if outlier_list[0][i] == outlier_list[1][i] == outlier_list[2][i] == -1:
            outlier_result.append(i)

    # export outlier to a txt file
    output_file = 'outlier_player_career_dataset.txt'
    with open(output_file, 'w', newline='') as f:
        f.write('the corresponding row number of file: player_career_normalization_dst.csv\n')
        f.write('number of outliers: ' + str(len(outlier_result)) + '\n')
        for item in outlier_result:
            f.write(str(item) + '\n')
    print(outlier_result)
    print(len(outlier_result))


def main():

    lof()


if __name__ == "__main__":
    main()
