import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rcParams
import seaborn as sns
from collections import Counter
import os

df = pd.read_csv('netflix_titles.csv')
print("ข้อมูลทั้งหมด:", df.shape)
print("----------------------------------")

print(df.head())
print("----------------------------------")

print("\nข้อมูลเบื้องต้น:")
print(df.info())
print("----------------------------------")

print("\nMissing values:")
print(df.isnull().sum())
print("----------------------------------")

sns.set(style="whitegrid", palette="pastel")
plt.rcParams['figure.figsize'] = (10,5)
rcParams['font.family'] = 'Tahoma'
rcParams['axes.unicode_minus'] = False  

# --- จำนวนหนัง vs ซีรีส์ ---
type_count = df['type'].value_counts()

sns.barplot(x=type_count.index, y=type_count.values)
plt.title("จำนวนหนังและซีรีส์ใน Netflix")
plt.xlabel("ประเภท")
plt.ylabel("จำนวน")
plt.savefig('../visuals/type_count.png')
plt.show()

# --- ประเทศที่มีหนังมากที่สุด ---
country_data = df['country'].value_counts().head(10)

sns.barplot(y=country_data.index, x=country_data.values)
plt.title("10 ประเทศที่มีหนังมากที่สุดใน Netflix")
plt.xlabel("จำนวน")
plt.ylabel("ประเทศ")
plt.savefig('../visuals/top_countries.png')
plt.show()

# --- ประเภทหนังยอดนิยม (Genre) ---
genres = df['listed_in'].dropna().str.split(', ')
all_genres = [g for sublist in genres for g in sublist]
genre_count = Counter(all_genres).most_common(10)

sns.barplot(y=[g[0] for g in genre_count], x=[g[1] for g in genre_count])
plt.title("10 ประเภทหนังยอดนิยมใน Netflix")
plt.xlabel("จำนวน")
plt.ylabel("ประเภท")
plt.savefig('../visuals/top_genres.png')
plt.show()

# --- ประเภทเนื้อหายอดนิยมในแต่ละปี ---
trend_df = df.groupby(['release_year', 'type']).size().reset_index(name='count')

plt.figure(figsize=(10, 6))
sns.lineplot(data=trend_df, x='release_year', y='count', hue='type', marker='o')
plt.title('แนวโน้มจำนวนเนื้อหาในแต่ละปี (Movie vs TV Show)', fontsize=14)
plt.xlabel('ปีที่ออกฉาย', fontsize=12)
plt.ylabel('จำนวนรายการ', fontsize=12)
plt.legend(title='ประเภท')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()