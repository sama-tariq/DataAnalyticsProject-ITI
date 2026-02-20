import requests
import pandas as pd
import seaborn as sns

limit = 100
response = requests.get('https://dummyjson.com/users')
data = response.json()['users']

users= pd.DataFrame(data)
users.head()

users.to_csv('users.csv', index=False)

print("Shape: ", users.shape)

print(users['gender'].value_counts())
print(users['bloodGroup'].value_counts())
print(users['eyeColor'].value_counts())
print(users['company'].head())

print("Columns: ", users.columns.tolist())
print(users.dtypes)
print(users.isnull().sum())

users_temp = users.copy()
for col in users_temp.columns:
    users_temp[col] = users_temp[col].apply(lambda x: str(x) if isinstance(x, (dict, list)) else x)

print("Duplicated rows: ", users_temp.duplicated().sum())

print(users.describe())

users['country'] = users['address'].apply(lambda x: x.get('country', 'Unknown'))

users[['address', 'country']].head()

for col in ['age', 'height', 'weight']:
    if col in users.columns:
        users[col].fillna(users[col].mean(), inplace=True)

print("Average age:", users['age'].mean())
print("Average age by gender: ")
print(users.groupby('gender')['age'].mean())

print("Number of users per gender:")
print(users['gender'].value_counts())

users['city'] = users['address'].apply(lambda x: x.get('city') if isinstance(x, dict) else None)

top_cities = users['city'].value_counts().head(10)

print("Top 10 cities:")
print(top_cities)

if 'height' in users.columns and 'weight' in users.columns:
    print("Average height:", users['height'].mean())
    print("Average weight:", users['weight'].mean())