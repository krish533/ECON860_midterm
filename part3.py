import pandas as pd
import numpy
import matplotlib.pyplot as plt



# # #part 3
df = pd.read_csv("/Users/krishnasharma/desktop/econ8060/midterm_1/part2_3/part2_dataset.csv")
# # #reporitng summary statistics
print(df)
print(df.describe())
print("--------------")


# ###  Check how many user  has zero follower  
df['zero_score1'] = (df['followers'] == 0)*1
print(df['zero_score1'].sum())

df['zero_score2'] = (df['following'] == 0)*1
print(df['zero_score2'].sum())


df['zero_score3'] = (df['public_repos'] == 0)*1
print(df['zero_score3'].sum())


#examining the correlation
follower=numpy.log(df['followers'].tolist())
following=numpy.log(df['following'].tolist())
public_repos=numpy.log(df['public_repos'].tolist())
count_starred=numpy.log(df['count_starred'].tolist())


#examining the correlation between follower and following
plt.scatter(follower, following)

plt.title("Figure1: follower and following")
plt.ylabel("followers")
plt.xlabel("following")
#plt.colorbar()
plt.savefig('figure1.png')
plt.show()

examing the correlation between public repos and follower
plt.scatter(public_repos, follower)

plt.title("Figure 2: followers and  public_repos")
plt.xlabel("followers")
plt.ylabel("public_repos")
#plt.colorbar()
plt.savefig('figure2.png')
plt.show()

#examining the correlation between follower and count_starred

#plt.scatter(count_starred,follower)

# plt.title("Figure 3: count_starred and followers")
# plt.xlabel("followers")
# plt.ylabel("count_starred")
# #plt.colorbar()
# plt.savefig('figure3.png')
# plt.show()
# print("done")

#examing all three variables under single plot
plt.scatter(following,follower,c=public_repos)
plt.title("Figure 3: count_starred , followers and public_repos")
plt.ylabel("followers")
plt.xlabel("following")
plt.colorbar()
plt.savefig('figure3.png')
plt.show()
print("done")