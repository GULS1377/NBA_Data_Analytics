#  **Project Report** 

###  **1. Basic Statistical Analysis and data cleaning insight** 

#### 1.1 Mean, Median and standard  

| **Dataset**         | **Attributes used for calculating Mean, Median and  StD** |
| ------------------- | --------------------------------------------------------- |
| player_stats        | G, GS, MP, eFG%, ORB, DRB, TRB, AST, STL, BLK, TOV,  PTS  |
| player_career_stats | G, GS, MP, eFG%, ORB, DRB, TRB, AST, STL, BLK, TOV,  PTS  |
| Salary              | salary                                                    |

- player_stats 

  ![image-20191103212406137](C:\Users\Lu Sun\AppData\Roaming\Typora\typora-user-images\image-20191103212406137.png)

- player_career_stats  

  ![image-20191103212444702](C:\Users\Lu Sun\AppData\Roaming\Typora\typora-user-images\image-20191103212444702.png)

- Salary  

  ![image-20191103212500698](C:\Users\Lu Sun\AppData\Roaming\Typora\typora-user-images\image-20191103212500698.png)

#### 1.2 Data Normalization  

> In our data set ‘player stats’, we have 31 attributes varying in units and scales.
>
> eg: The attribute FG%(Field Goals Percentage) is a percentage number ranges from 0 to 1.
>
> The attribute PTS(Points Per Game) having the unit “points” and ranges from 0 to 37.1.
>
> If we use the raw data, the PTS having a larger scale will have more weight than others when doing analysis. So, to clear these in-balanced factors, we should normalize the data via z-score before using them. Data after being z-scored will have the same distribution as the original data.

#### 1.3 Data cleaning  

> Salary dataset: Remove the ‘$’ symbol on the ‘salary’ attribute.
>
> player_stats dataset: remove 2nd position on ‘Pos’ attribute.

#### 1.4 Binning data  

> The records in dataset ‘player_career_stats’ are binned into 5 bins. A clear attribute we can use to evaluate the importance of one player in the NBA is how many games he played. Influential players like Michael Jordan, Karl Malone, and Kobe Bryant all played more than 1,000 games in their careers.
>
> Intuitively, we can classify them via:
>
> | **Value (Game Played)**            | **Class**   |
> | ---------------------------------- | ----------- |
> | [0, 323)        approx.: 4 seasons | Newbie      |
> | [323, 645)      approx.: 8 seasons | Sophomore   |
> | [645, 967)     approx.: 12 seasons | Senior      |
> | [967, 1289)    approx.: 16 seasons | Experienced |
> | [1289, 1611)   approx.: 20 seasons | Veteran     |

#### 1.5 Additional Part for CS Students

>  Tying 3 different k-value: 200, 100 and 50. 
>
>  By cross-checking, 184 outliers are found.
>
> ![image-20191103213925428](C:\Users\Lu Sun\AppData\Roaming\Typora\typora-user-images\image-20191103213925428.png)

###  **2. Histograms and Correlations** 

#### 2.1 Histogram  

> In this part, we try to find the relation between the player’s position and their key indices of performance.
>
> a.   eFG% (Effective Field Goal Percentage)
>
> We are surprised to find that there is no relation between a players’ position and their eFG%. 
>
> b.   TRB (Total Rebounds Per Game)
>
> No surprise. Centers have the best performance followed by Power Forward. And Point Guard and Shooting Guard who mainly focus on outside of the paint area.
>
> c.   AST (Assistant Per Game)
>
> No surprise. Point Guards, the players leading the offense of games rank first.
>
> d.   BLK (Block Per Game)
>
> No surprise. Centers dominate the paint area.
>
> e.   TOV (Turnover Per Game)
>
> No surprise. Point Guards, players having the highest possession time of the ball, have a higher risk to make a mistake. 
>
> f.   PF (Personal Foul Per Game)
>
> No surprise. Centers and Power Forward who have a higher pressure on the defense incline to foul than others. 
>
> g.   PTS (Points Per Game)
>
> The order of PTS reflects the priorities of players’ role in games. No surprise.
>
> ![image-20191103215124153](C:\Users\Lu Sun\AppData\Roaming\Typora\typora-user-images\image-20191103215124153.png)
>
> ​                                                               Fig 2.1. Key indices of performance  

#### 2.2 Correlations  

> The table(Fig. 2.2) and two scatter plots show the correlation among ‘Season’, ‘Average Salary’ and ‘Record count for the season. From table and plots, we can find: 
>
> a.   Salary variation:
>
> In the following seasons, compared with last season, the average player’s salary decreased.
>
> 1985~1986, 1987-1988, 1990-91, 2006-07, 2009-10, 2010-11, 2011-12, 2012-13, 2014-15
>
> b.   Outliers:
>
> From the 1st scatter plot(Fig. 2.3), 1989-1990 looks like a crazy season that the average salary three times the last season’s. But actually, from the 2nd scatter plot(Fig. 2.4), data for 1989-90 season is an outlier, since this season only has 64 records that are far less than the number of records in other seasons and this season has 27 teams, so it does not make sense to have only 64 records.
>
> For the season 1986-87, the data is another outlier. That season has 23 teams in total. So, having 40-records is not close to accurate.
>
> Same for 1984-1985, 23 teams, 206 records. It’s clearly not valid data.
>
> c.   NBA economy recession:
>
> Reviewing the 1st scatter plot(Fig. 2.3), from 2009 to 2015, 5 seasons’ decreasing in a row shows the longest continuous recession of the NBA since 1984.
>
> ![image-20191103215227582](C:\Users\Lu Sun\AppData\Roaming\Typora\typora-user-images\image-20191103215227582.png)
>
> ​                                                      Fig 2.2 Season, Avg Salary and Record Count
>
> ![image-20191103215323024](C:\Users\Lu Sun\AppData\Roaming\Typora\typora-user-images\image-20191103215323024.png)
>
> ​                                                                   Fig 2.3 Avg Salary and Season
>
> ![image-20191103215340044](C:\Users\Lu Sun\AppData\Roaming\Typora\typora-user-images\image-20191103215340044.png)
>
> ​                                                               Fig 2.4 Record Count and Season  

###  3. Cluster Analysis

#### 3.1  Explain the finding of conducting three cluster analyses on our data

> We did clustering analysis on the subset of ‘player_career_stats_cleaned.csv’. Firstly, we dropped non-numeric columns such as ‘Name’, ‘Season’ and ‘lg’. Then, we dropped some other columns which makes no sense in the following clustering such as: FG% (Field goal percentage), 3PA (3-point field goal attempts per game), 3P% (3-point goal percentage), 2PA (2-point field goal attempts per game), 2P% (2-point field goal percentage) and eFG% (effective field goal percentage (This statistic adjusts for the fact that a 3-point field goal is worth one more point than a 2-point field goal).
>
> We used three clustering methods according to the material: Ward (hierarchical clustering method), K-means (partition clustering method) and DBSCAN clustering analysis. Besides, I show the results in pictures. Also, We manually selected the range of n.

-  Part Ⅰ: Hierarchical Clustering 

  > For the first part of hierarchical clustering, we choose Ward algorithm. I manually picked three clustering components such as 3, 5 and 7 to plot. As the pictures shows below.
  >
  > 1. When n = 3
  >
  >     ![img](https://lh5.googleusercontent.com/TzCJzA5fiZup9h_GgmjGPXeUpdNjPzgBMBeHv4wDolbBQiypjj1HoPS7rjzN75AVHfzMLFpcpCJZWD6frJ6C4mEFWxLeG3Ysz_VtEruDF5ZG8j4hJR-2DR_dbZco27-37cqYSHdj) 
  >
  > 2.  When n = 5 
  >
  >     ![img](https://lh5.googleusercontent.com/48RQhsf5RdYOS_TbRhVetn7Uih3M3EvwIToaRUECGL8sgQKgJ4AHTorRrF_aHCy-ctqvrR6EIdChMMNVcp2gSGcVR62DW-C-No4MzJfBhPnG-G6R1azxXGwSTIiuKpIJJv0SJPN_) 
  >
  > 3.  When n = 7 
  >
  >     ![img](https://lh3.googleusercontent.com/pC-8Ph1qMXXAgPYEuHyuoY3muaxwQE6ZgVU8UF3ckE9O6fGTRKfQPaf06p48GqroNyPtsVPIM2Ew1yTLiLUiIIYXOH4z92q9qR6fRhiaDib2pambZap9_DdUIzX0VgstE_Igs023) 

-  Part Ⅱ: K-Means Clustering 

  > 1. When n = 3 
  >
  >     ![img](https://lh5.googleusercontent.com/p5Ll_G3_e4dcRPZR4t_0SO6RqVjZMW-xIOKvw5qxiMkC5vlR3oMB90x2Ls4SCmPVPZHsaxXCTOp5qp-YSDM-3jYZhW2Jbl0dGKkgVi94kPIyGHx71G7oOG2quc0_bAGMAkpJfdp2) 
  >
  > 2.  When n = 5 
  >
  >     ![img](https://lh5.googleusercontent.com/xihSTD1cXjjXgh08g4GdneeAXS_oQDVIn64otxNYWbtxMajOJQW_XIJ9RE-EwLMUWGI3_sASAOqnDi7H8YQpSUw6H7P9kZVEz5MRKS9aPzvM0MF92RdC5IAGvXxusZgrhdLiiKtt) 
  >
  > 3.  When n = 7 
  >
  >     ![img](https://lh3.googleusercontent.com/BYKlsuRL6i_RS_2-7nahy2YYER5ExdxdcoT8tzoxwgKssVlahaLp6gUZj8RjRm585ahuoXu55CaXkfxRnIM2gCSX2vhmyqEm8-AgJy9GYSbIwVQWT46NDg4FTQd8WlBxLeg4EW5p) 

-  Part Ⅲ: DBSCAN Clustering 

  > 1.  When n = 3 
  >
  >     ![img](https://lh5.googleusercontent.com/2oRNJMup3CF627pVtHLFB_BuXxCPRv8rB1Q2_osNBqRGEB-7bMdK_mZnnJolWSVH0D6Zd4nmcV7PqqAxl2nrLgmyyOTXq1gB5Os8Yqal7W22Q-CT3YJVVhxFXes5L5OHDYnXXHW6) 
  >
  > 2.  When n = 5 
  >
  >     ![img](https://lh4.googleusercontent.com/j9wg2UrtmTRfDEIVv2YSORDL5JqshOCl_swVXEKw2NdTcApM3iElAO2mNJyzKHpmiWtlBbl98RwGWeS0Etq7Mmi2dc2W3lklkCXIIlMR2JnTbJ7YpM9jo8VkqcI4-cC5wcTbtwdS) 
  >
  > 3.  When n = 7 
  >
  >     ![img](https://lh4.googleusercontent.com/UQoLmD22gQ5WzZxwYlTRdjihFuvoAIq17i0MTS51S1hjoQWQq64_aRPhtaiVOCyIOKvyQXhRO8nR7OBY3ZWngX3pQQGyWH47QeRR3-dIpiDAF-Z_s2vGg23VOFUVwNV8kpiwA941) 

- Summary:

  > By observing those pictures, we can clearly find that the clustering results of Ward and K-Means are similarly to some degree. Both of them are tight and well-chunked. Compared to them, the result of dbscan looks kind of in an unclear grouping. Therefore, for this dataset, dbscan is not a good algorithm for clustering relatively.
  > After plotting, we used Silhouette score to measure the quality of different clustering results.
  >
  > |                   | N=3    | N=5   | N=7   |
  > | ----------------- | ------ | ----- | ----- |
  > | Ward  Algorithm   | 0.234  | 0.208 | 0.181 |
  > | K-Mean  Algorithm | 0.281  | 0.232 | 0.242 |
  > | DBSCAN  Algorithm | -0.233 | 0.154 | 0.173 |
  >
  > As the table shows and according to the silhouette score, K-Mean Algorithm, which is 0.281 when n = 3, is closer to 1, so it performs best.
  >
  > Hierarchical clustering is a bottom-up approach, merging similar categories to find more similar ones. K-means is to automatically find the most similar class, and then perform clustering operations. DBSCAN is a Density-Based Spatial Clustering method, from the principle of Clustering. The three methods are very similar, and this similarity is also reflected in the three-dimensional image, which can be verified from different n_components.

#### 3.2 Plot the clusters or if the dimensionality is too high, plot a PCA projection of the clusters. Does the plot give you additional insight about the clustering – explain

> We think 3D is better than 2D so we just keep 3D in order to get a better view. However, we still use pca(). For example, in the player_career_stats_cleaned.csv file, we have 20 dimensions, applying PCA and takes 7 hyperplanes. Then, we get 7 most relevant hyperplanes, so that when the dimensions are reduced, the dimensions are 7. 
>
> The plots are illustrated in the python program, and the plot does give more insight on the clustering. If only calculating the numbers, it is hard to find the best suitable clustering numbers. With plots, it is easier, as you can see the result. By calculating the Silhouette value, the work is much more easier, the higher Silhouette score, the more the better the clustering. For example, in this program, the highest Silhouette score is 0.281. Therefore, when clustering components = 3, it will attain the best clustering result. 

 ### **4. Association Rules / Frequent Itemset Mining Analysis** 

#### 4.1 For the part of association rules, what patterns are most frequent? Is this surprising? Explain your findings

>  We chose the subset of salary.csv. Then, we calculate the support in the python program, which means the frequent of each player occurs together (with others if possible) as a percentage in all records. So using Apriori algorithm can find the players who are mostly like to server in the same team among their careers. With lower percentage, the more likely to find players served in the same team. We chose three different support levels, they are 0.28, 0.25 and 0.125. 
>
>  When min_support_value = 0.25, it has five itemsets, and the most frequent patterns are (Jarrett Jack), (Juwan Howard),(Mike James), (Mike Wilks)and (Shaun Livingston). 
>
>  ![img](https://lh5.googleusercontent.com/LqDauKoSoAnUBLizk4wt0fF7YkopToQA3Wy2GqVXvWnbU6njWSUlQxf5M0MrTqNvi4WOB1BUxeyZinCgIL59da4gdKoWGBMQUnAlPH_-Bco-OEUnxm8B-DlLRlSg_5r9CgkIn3Dr) 
>
>  When min_support_value = 0.20, it has 55 itemsets. The 55 item sets are the most frequent itemsets when min_support_value = 0.20. 
>
>  ![img](https://lh6.googleusercontent.com/37q3OAMtZLk2obUpLKiYKKJ4HxPjqCFGeg0x43s9SiUVc7HvWjeTuauyBf1a8mKMxXWikgFn_vF0yk5oVAsiM6-peixI_2ZnsgybPXMutBFv3WN_gUXbXR8e58HJG1DV-lUNJglh) 
>
>  ![img](https://lh4.googleusercontent.com/ai6qdU0SrmT0kK_f6fKvZOSCrattuYKZ87RF4cexf1KMifwMtv81cwVr0jlaPfLqF7j2WJgToWi2DPYLZp7gXs6PYEAfpzAEbIDg5pEcdi8JYqzE9Qw_yIiqkXXJVCZTl53V6bsU) 
>
>  ![img](https://lh3.googleusercontent.com/8VJHS4KL7kI62uMaKIbnmV4jHgTCt_R_iddZw1ta4qz_IdGvKNtzYdTknw2kFG9wORHtLozJzbwOEGPxybnOxlcFmEGFpnijBGv0RA3_BlkA3-dylRUG9uGZIRUmCV1fpXT64h0_) 
>
>  When min_support_value = 0.125, it has 538 itemsets. Those 538 itemsets are the most frequent itemsets when min_support_value = 0.125. 

 ### **5. Hypothesis Testing & Classification** 

#### 5.1 Parametric statistical tests

#####          **Hypothesis Test**  

- **First hypothesis test**  

  > **whether prominent players and normal players have same field goal percentages.**  
  >
  > We want to know whether players whose career average points higher than 10 is statistically different from those are not in terms of career average field goal percentage. The reason behind for this test is we really want to know whether it is a fair or reasonable way to define a NBA player as a phenomenal player or not simply looking at their average points. It is possible NBA players average career points higher than 10 has lower points percentage, which means they got these many points by trying more field goals. Therefore, it is necessary to statistically examine whether these two kinds of players’ field goal percentage’s difference.  
  >
  > **Null hypothesis**: prominent NBA players (career average points per game higher than 10) and normal NBA players have the same Field Goal Percentages (H0) .
  >
  > **Alternative hypothesis**: prominent NVA players and normal NBA players have different Field Goal Percentages (H1).
  >
  > Our results are T-value: 10.59, P-value: 9.02*10^-26. This large T value and super small p value indicates our null hypothesis is false and these two kinds of NBA players are significantly different in terms of field goal percentage.

- **Second hypothesis test:**

  > **whether players from different positions have same career points.**  
  >
  > By doing this test, we could find out whether NBA players’ position would affect their points they get. It is not surprising to find out each position on basketball court has distinct role and responsibilities. However, the goal of the game of basketball is to put the ball into the basket, which means to “get points”. Therefore, it is worthwhile to find out whether some positions might more easier to have higher points than some others statistically.
  >
  > I use iteration to test each position (totally five), say first position x and second position y, so there are totally 10 tests.
  >
  > **Null hypothesis**: players of position x and player of position y have same average points.
  >
  > **Alternative hypothesis**: players of position x and player of position y have different average points.
  >
  > Result:  
  >
  > |      | C                                                    | SF                                                    | SG                                                    | PG                                                  | PF                                                  |
  > | ---- | ---------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- | --------------------------------------------------- | --------------------------------------------------- |
  > | C    |                                                      | (-4.399322660942447,  1.1894279318897957e-05, 1120.0) | (-4.109796009288748,  4.2275383204110836e-05, 1207.0) | (-3.542976493178241, 0.000411826056450884,  1127.0) | (-1.369763593521598, 0.17102375052395263,  1169.0)  |
  > | SF   | (4.399322660942447, 1.1894279318897957e-05,  1120.0) |                                                       | (0.33302684275074923, 0.7391711003229472,  1223.0)    | (1.1086384143189745, 0.2678194149985443,  1143.0)   | (3.220307994003003, 0.001315309596736067,  1185.0)  |
  > | SG   | (4.109796009288748, 4.2275383204110836e-05,  1207.0) | (-0.33302684275074923, 0.7391711003229472,  1223.0)   |                                                       | (0.7690293835810792, 0.44202350751126196,  1230.0)  | (2.912310791229858, 0.0036502702104930494,  1272.0) |
  > | PG   | (3.542976493178241, 0.000411826056450884,  1127.0)   | (-1.1086384143189745, 0.2678194149985443,  1143.0)    | (-0.7690293835810792, 0.44202350751126196,  1230.0)   |                                                     | (2.241396915772562, 0.025183827681914777,  1192.0)  |
  > | PF   | (1.369763593521598, 0.17102375052395263,  1169.0)    | (-3.220307994003003, 0.001315309596736067,  1185.0)   | (-2.912310791229858, 0.0036502702104930494,  1272.0)  | (-2.241396915772562, 0.025183827681914777,  1192.0) |                                                     |
  >
  > Here, C, SF, SG, PG, PF are five different positions. The three values in each cells are t-value, p-value and degree of freedoms. 
  >
  >  
  >
  > From above table, we can see:
  >
  > 1. center players reject null hypothesis with small forward, shooting guard and point guard players, but same with power forward players (t-value: -1.37, p-value: 0.17).
  >
  > 2. small forward players reject null hypothesis with center and power forward players, but accept null hypothesis with shooting guard (t-value: 0.33, p-value: 0.74)and point guard players (t-value: 1.11, p-value: 0.27).
  >
  > 3. shooting guard players reject null hypothesis with power forward players but accept with point guard players (t-value: -0.77, p-value: 0.44)
  >
  >  
  >
  > To conclude, the result shows that “smaller players” (point guard, shooting guard, small forward players) and “bigger players” (center, power forward players) have same career average points respectively, but they are different from each other. Therefore, we might divide whole NBA players into these two groups for further analysis.

- ##### Third hypothesis test  

  > We want to examine if it is true when a player is good at scoring, he will shoot more and get more points. We use linear regression to fit two features of players, which are career average points and career average field goal percentage.
  >
  >  
  >
  > **Null hypothesis**: There is a linear relationship between player’s career average points and field goal percentage.
  >
  > **Alternative hypothesis**: They do not have a linear relationship
  >
  > Result:
  >
  > ![image-20191104012718575](C:\Users\Lu Sun\AppData\Roaming\Typora\typora-user-images\image-20191104012718575.png)
  >
  > We may find the result indicating the null hypothesis does not hold, as the R-squared value is quite low. We can also see that P>|t| is way bigger than 0.05. Therefore, we may conclude that there is no linear relationship between these players’ career average points and their field goal percentage.

#### 5.2 Data driven predictive models

##### **Prediction task** for all models: 

>  Predict whether a NBA player is a good player based on his statistic such as FG, 2P and 3P.
>
> *A good player is the player with PTS > 10(Our definition).

##### Reason for choosing this prediction task:

> This task is reasonable and understandable to predict because a basketball player's PTS is the final result of his whole performance. Therefore, we take lots of his performance statistic into consideration and it will more likely lead us to correct prediction.

- ##### Decision tree

  **Reason for applying this method:**

  > 1. Decision tree is inexpensive to construct and extremely fast at classifying unknown records.
  > 2. There are some attributes which represent the similar feature like FG,FGA,FG%. And decision tree is robust to such situation.
  > 3. It always get comparable performance for classification problem on many simple data sets.

  **Applying process:**

  > 1. Preprocess data like making non-numeric categorical data numeric and normalize data with norms "l1".
  > 2. Initialize parameters and construct the classifier.
  > 3. Use cross-validation (num_folds=5, test_size = 0.20) and record ROC curve, confusion matrix and prediction accuracy.
  > 4. Analyze data and summarize.

  **Results:** 

  > - Accuracy: 
  >   - Cross-validation result with norm l1: DC: 0.934851
  >   - Accuracy on test dataset with norm l1: DC: 0.922689
  >
  > - confusion matrix: 
  >
  >   [[462  18]
  >    [ 23  92]]
  >
  > - ROC curve:
  >
  >   - ROC curve fpr:  [0., 0.03541667, 1.]
  >   - ROC curve tpr:  [0., 0.74782609, 1.]
  >   - ROC curve thresholds:  [2., 1., 0.]
  >   - ![image-20191103142433091](C:\Users\Lu Sun\AppData\Roaming\Typora\typora-user-images\image-20191103142433091.png)
  >
  > - AUC:  
  >
  >   0.8562047101449276

  **Analysis:**

  > First, we can see that the accuracies of cross-validation and test set are similar and all get about 92% accuracy. 
  >
  > Then as for confusion matrix and ROC curve results, we can see that the data points for ROC curve is far away from the ROC curve of random guessing. 
  >
  > And I add the AUC value to help evaluate the ROC curve and it is 0.8562047101449276 and really near 1. 
  >
  > In sum, the model does truly excellently for our prediction task.

- ##### A Lazy Learner Method(kNN)

  **Reason for applying this method:**

  > 1. kNN is lazy learner and there is no training period. Thus, as our dataset is not so large and k is proper, it costs little time.
  > 2.  It's easy to implement.

  **Applying process:**

  > 1. Preprocess data like making non-numeric categorical data numeric and normalize data with norms "l1".
  > 2. Initialize parameters and construct the classifier with n_neighbors=10.
  > 3. Use cross-validation (num_folds=5, test_size = 0.20) and record ROC curve, confusion matrix and prediction accuracy.
  > 4. Analyze data and summarize.

  **Results:** 

  > - Accuracy: 
  >
  >   - Cross-validation result with norm l1: kNN: 0.880624
  >   - Accuracy on test dataset with norm l1: kNN: 0.895798
  >
  > - confusion matrix: 
  >
  >   [[469  11]
  >    [ 51  64]]
  >
  > - ROC curve:
  >
  >   - ROC curve fpr:  [0., 0.02291667, 1.]
  >   - ROC curve tpr:  [0., 0.55652174, 1.]
  >   - ROC curve thresholds:  [2., 1., 0.]
  >   - ![image-20191103142543667](C:\Users\Lu Sun\AppData\Roaming\Typora\typora-user-images\image-20191103142543667.png)
  >
  > - AUC:  
  >
  >   0.766802536231884

  **Analysis:**

  > First, we can see that the accuracy of cross-validation is 88% and it's 90% on test set. It's due to the seed of random and maybe the features of data in test set fits the model better than the validation set in the training set.
  >
  > Then as for confusion matrix and ROC curve results, we can see that the data points for ROC curve is a little far from the ROC curve of random guessing. 
  >
  > And the ROC curve and it is 0.766802536231884 and it's not bad.
  >
  > In sum, the model does truly well for our prediction task.

- ##### Naïve Bayes

  **Reason for applying this method:**

  > 1. Independence assumption of Naïve Bayes may not hold for some attributes. Actually in our dataset, the statistic of NBA players always has some connection. For example, the 2P% and 3P% represents the per cent of your different shooting goals. And FG% is calculated from this 2 parameters. Thus, it's not wise to apply Naïve Bayes to this prediction task. However, I think the importance lies in check the knowledge we learn is correct and applying Naïve Bayes in such bad situation can help us learn deeply. Thus, we still apply Naïve Bayes to this prediction task.
  > 2.  Naïve Bayes is robust to isolated noise points.

  **Applying process:**

  > 1. Preprocess data like making non-numeric categorical data numeric and normalize data with norms "l1".
  > 2. Initialize parameters and construct the classifier with Gaussian NB.
  > 3. Use cross-validation (num_folds=5, test_size = 0.20) and record ROC curve, confusion matrix and prediction accuracy.
  > 4. Analyze data and summarize.

  **Results:** 

  > - Accuracy: 
  >
  >   - Cross-validation result with norm l1: NB: 0.448518
  >   - Accuracy on test dataset with norm l1: NB: 0.415126
  >
  > - confusion matrix: 
  >
  >   [[137 343]
  >    [  5 110]]
  >
  > - ROC curve:
  >
  >   - ROC curve fpr:  [0., 0.71458333, 1.]
  >   - ROC curve tpr:  [0., 0.95652174, 1.]
  >   - ROC curve thresholds:  [2., 1., 0.]
  >   - ![image-20191103143727460](C:\Users\Lu Sun\AppData\Roaming\Typora\typora-user-images\image-20191103143727460.png)
  >
  > - AUC:  
  >
  >   0.6209692028985507

  **Analysis:**

  > First, we can see that the accuracy of cross-validation is 44% and it's 41% on test set. It confirms our guess about the performance of Naïve Bayes on this prediction task as the attributes have connections between each other.
  >
  > Then as for confusion matrix and ROC curve results, we can see that the data points for ROC curve is really close from the ROC curve of random guessing. 
  >
  > And the ROC curve and it is 0.6209692028985507 and it's a little bad.
  >
  > In sum, the model does truly terribly for our prediction task.

- ##### SVM

  **Reason for applying this method:**

  > 1.  SVM works relatively well when there is clear margin of separation between classes. To some degree, I guess it should fit with the task better than kNN and worse than good classifiers like decision tree because it depends on clear margin of separation between classes but not entirely rely on independency like kNN. 
  > 2.   SVM is relatively memory efficient and is more effective in high dimensional spaces. And our dataset has about 28 dimensions and I think it fits this feature.

  **Applying process:**

  > 1. Preprocess data like making non-numeric categorical data numeric and normalize data with norms "l1".
  > 2. Initialize parameters and construct the classifier with SVC.
  > 3. Use cross-validation (num_folds=5, test_size = 0.20) and record ROC curve, confusion matrix and prediction accuracy.
  > 4. Analyze data and summarize.

  **Results:** 

  > - Accuracy: 
  >
  >   - Cross-validation result with norm l1: SVM: 0.797808
  >   - Accuracy on test dataset with norm l1: SVM: 0.811765
  >
  > - confusion matrix: 
  >
  >   [[480   0]
  >    [112   3]]
  >
  > - ROC curve:
  >
  >   - ROC curve fpr:  [0., 0., 1.]
  >   - ROC curve tpr:  [0., 0.02608696, 1.]
  >   - ROC curve thresholds:  [2., 1., 0.]
  >   - ![image-20191103144708938](C:\Users\Lu Sun\AppData\Roaming\Typora\typora-user-images\image-20191103144708938.png)
  >
  > - AUC:  
  >
  >   0.5130434782608696

  **Analysis:**

  > First, we can see that the accuracy of cross-validation is 80% and it's 81% on test set. It confirms our guess about the performance of SVM on this prediction task as it works better than kNN and worse than decision tree.
  >
  > Then as for confusion matrix and ROC curve results, we can see that the data points for ROC curve is really close from the ROC curve of random guessing. 
  >
  > And the ROC curve and it is 0.5130434782608696 and it's a little bad.
  >
  > However, based on its accuracy I think maybe there is some problems about the test data because for ROC curve thresholds[1], the fpr[1] is 0 and tpr[1] is 0.02608696. I think there is some problem about the distribution of test data as we get truly low TP and FN values with not bad accuracy.
  >
  > In sum, the model does not bad for our prediction task.

- ##### Random Forest

  **Reason for applying this method:**

  > 1.  Random Forest is the combination of lots of decision tree and the predictive performance can compete with the best supervised learning algorithms.
  > 2.  They provide a reliable feature importance estimate which is really proper for our prediction task because our definition of a good player is actually connected with PTS.

  **Applying process:**

  > 1. Preprocess data like making non-numeric categorical data numeric and normalize data with norms "l1".
  > 2. Initialize parameters and construct the classifier with n_estimators=100(tree numbers).
  > 3. Use cross-validation (num_folds=5, test_size = 0.20) and record ROC curve, confusion matrix and prediction accuracy.
  > 4. Analyze data and summarize.

  **Results:** 

  > - Accuracy: 
  >
  >   - Cross-validation result with norm l1: RF: 0.966369
  >   - Accuracy on test dataset with norm l1: RF: 0.961345
  >
  > - confusion matrix: 
  >
  >   [[475   5]
  >    [ 18  97]]
  >
  > - ROC curve:
  >
  >   - ROC curve fpr:  [0., 0.01041667., 1.]
  >   - ROC curve tpr:  [0., , 1.]
  >   - ROC curve thresholds:  [2., 1., 0.]
  >   - ![image-20191103150457783](C:\Users\Lu Sun\AppData\Roaming\Typora\typora-user-images\image-20191103150457783.png)
  >
  > - AUC:  
  >
  >   0.9165307971014492

  **Analysis:**

  > First, we can see that the accuracy of cross-validation is 96% and it's 96% on test set. It performs really excellently.
  >
  > Then as for confusion matrix and ROC curve results, we can see that the data points for ROC curve is really far away from the ROC curve of random guessing. 
  >
  > And the ROC curve and it is 0.9165307971014492 and it's so good.
  >
  > In sum, the model does best for our prediction task.

