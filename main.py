import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt 
import matplotlib.ticker as ticker
import numpy as np; np.random.seed(1)

#Base data
df = pd.read_csv('2.csv')


#Trimmed collumns useful data
dp = df.iloc[:, [1, 2, 4, 5, 6, 8, 9]]

#Converting to int
dp.astype({'Runtime': 'int32'}).dtypes

#sorting by int
dp.sort_values(by="Runtime")

#Check format
print(dp.head(10)) 




##########################
#runtime vs rating chart.#
##########################

sns.scatterplot(x="Runtime", y="IMDB_Rating", data=dp) 
plt.show()




##########################
#runtime vs rating chart.#
##########################


runList = dp["Runtime"].unique()

runRating = []
for run in runList:
    df1 = dp[dp["Runtime"] == run]
    
    tempList = []
    #count = df1["Runtime"].count()
    runs = df1["Runtime"].unique().tolist()
    runs = int(runs[0])
    #runs += f"({count})"
    tempList.append(runs)
    tempList.append(df1["IMDB_Rating"].mean())
    # print(df1["Runtime"].unique())
    # print(df1["IMDB_Rating"].mean())
    runRating.append(tempList)
    
runRating = pd.DataFrame.from_records(runRating)

runRating.columns = ["Runtime", "IMDB_Rating"]



# print(runRating) 


p = sns.scatterplot(x="Runtime", y="IMDB_Rating", data=runRating) 
plt.show()
##################################
#Average rating per Genre (MAX 2)#
##################################

# df1 = dp[dp["Genre"] == "Comedy, Romance"] 

# print(df1.head(10)) 
# print(df1["IMDB_Rating"].mean())

genreList = dp["Genre"].unique()

genreRating = []
for genre in genreList:
    df1 = dp[dp["Genre"] == genre]
    
    tempList = []
    count = df1["Genre"].count()
    genres = df1["Genre"].unique().tolist()
    genres = "".join(genres)
    if len(genres.split()) < 3:
        genres += f"({count})"
        tempList.append(genres)
        tempList.append(df1["IMDB_Rating"].mean())
        # print(df1["Genre"].unique())
        # print(df1["IMDB_Rating"].mean())
        genreRating.append(tempList)
    
genreRating = pd.DataFrame.from_records(genreRating)

genreRating.columns = ["Genre", "IMDB_Rating"]
genreRating = genreRating.sort_values(by=["IMDB_Rating"])


# print(genreRating) 


#sns.scatterplot(x="Genre", y="IMDB_Rating", data=genreRating) 
#graphGenreRation.set_xticklabels(graphGenreRation.get_xticklabels(),rotation = 90)
sns.set()
p = sns.scatterplot(x="Genre", y="IMDB_Rating", data=genreRating) 
locs, labels = plt.xticks()
plt.setp(labels, rotation=90, size=6)
p.set_xlabel("X-Axis", fontsize = 20)
p.set_ylabel("Y-Axis", fontsize = 20)
p.set_title("Plot", fontsize = 20)
plt.show()



##########################
#Metascore vs IMDB Rating#
##########################

sns.scatterplot(x="Meta_score", y="IMDB_Rating", data=dp) 
plt.show()



##########################
#Year vs IMDB Rating#
##########################

dp = dp.sort_values(by=["Released_Year"])
p = sns.scatterplot(x="Released_Year", y="IMDB_Rating", data=dp) 

locs, labels = plt.xticks()
plt.setp(labels, rotation=90, size=6)
p.set_xlabel("X-Axis", fontsize = 20)
p.set_ylabel("Y-Axis", fontsize = 20)
p.set_title("Plot", fontsize = 20)
plt.show()