import streamlit as st
st.title("✅ Bhopal Weapon Tracker App Launched Successfully")

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# Display settings
pd.set_option('display.max_columns', None)
sns.set(style='whitegrid')
df = pd.read_csv("C:\\Users\\amaan\\Downloads\\Bhopal_Weapon_License_Cleaned (1).csv")
# Show first few rows
df.head()
# Convert date columns to datetime
df['Issue_Date'] = pd.to_datetime(df['Issue_Date'])
df['Expiry_Date'] = pd.to_datetime(df['Expiry_Date'])
df['DOB'] = pd.to_datetime(df['DOB'])

# Check for missing values
df.isnull().sum()
# Total number of license holders
print("Total license holders:", df.shape[0])

# Weapons by area
print(df['Area'].value_counts())

# Status distribution
sns.countplot(data=df, x='Status', palette='Set2')
plt.title('Weapon Status Distribution')
plt.xticks(rotation=45)
plt.show()
plt.figure(figsize=(12,6))
sns.countplot(data=df, y='Area', order=df['Area'].value_counts().index, palette='coolwarm')
plt.title('Number of License Holders by Area')
plt.xlabel('Count')
plt.ylabel('Area')
plt.show()
# Today's date
today = pd.Timestamp.today()

# Licenses expiring within 30 days
expiring_soon = df[df['Expiry_Date'] < today + pd.Timedelta(days=30)]
print("Licenses expiring within 30 days:", expiring_soon.shape[0])

expiring_soon[['Name', 'License_No', 'Expiry_Date', 'Mobile']]
# Filter active weapons
active_weapons = df[df['Status'] == 'Active']
active_weapons[['Name', 'License_No', 'Area', 'Gun_Type', 'Mobile']]
sensitive_areas = ['TT Nagar', 'Jahangirabad', 'Ashoka Garden']

sensitive_active = df[(df['Area'].isin(sensitive_areas)) & (df['Status'] == 'Active')]
sensitive_active[['Name', 'Area', 'License_No', 'Mobile']]
# Save filtered list as Excel or CSV
expiring_soon.to_csv("weapons_expiring_soon.csv", index=False)
sensitive_active.to_excel("sensitive_area_weapons.xlsx", index=False)
# Save filtered list as Excel or CSV
expiring_soon.to_csv("weapons_expiring_soon.csv", index=False)
sensitive_active.to_excel("sensitive_area_weapons.xlsx", index=False)
