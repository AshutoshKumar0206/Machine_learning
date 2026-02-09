import pandas as pd
# print(pd.__version__)
# print(pd.read_csv('input.csv'))

#Series = A Pandas 1D Labeled array that can hold any data type, like a single column in a spreadsheet.

# data = [1, 2, 3]
# series = pd.Series(data, index = ["apartment1", "apartment2", "apartment3"])
# series.loc["apartment2"] = 202
# print(series.loc["apartment2"])#loc = location, write the index name and get the value
# print(series.iloc[1])#iloc to use index number in place of index name
# print(series[series < 200])

# calories = {"Day 1": 1750, "Day 2": 2100, "Day 3": 1700}
# cal = pd.Series(calories)
# cal.iloc[0] += 100
# print(cal.iloc[0:3:2])
# print(cal[cal>2000])


#DataFrames = A Tabular data structure with rows and columns
# data = {"Name":["SpongeBob", "Patrick", "Squidward"], 
#         "Age": [30, 35, 50]
#         }
# df = pd.DataFrame(data, index=["E1", "E2", "E3"])
# df["Job"] = ["Accountant", "Software", "Hardware"]
# new_row = pd.DataFrame([{"Name":"Tom", "Age":"45", "Job":"Doctor"}], index=["E4"])
# df = pd.concat([df, new_row])
# print(df.iloc[1])
# print(df)


# df = pd.read_csv("input.csv", index_col="Name")
# print(df.to_string())
# print(df.iloc[1].to_string())
# print(df[["Name", "Height", "Weight"]].to_string())

#Selection by rows
# print(df.loc["Charizard":"Blastoise", ["Height", "Weight"]].to_string())
# print(df.iloc[0:11:2, 0:5])

# pokemon = input("Enter a Pokemon name:")
# try:
#     print(df.loc[pokemon])
# except KeyError:
#     print(f"{pokemon} not found")  

df = pd.read_csv("input.csv")
# tall_pokemon = df[df["Height"] >= 2]
# heavy_pokemon = df[df["Weight"] >= 100]
# legendary_pokemon = df[df["Legendary"] == 1]
# fire_type = df[(df["Legendary"] == 0) & (df["Type1"] == "Fire")]
# print(fire_type)   

#Aggregate Functions = Reduces a set of values into a single numeric value, Often used with groupby() function
# print(df.mean(numeric_only=True))
# print(df.sum(numeric_only=True))
# print(df["Weight"].mean(numeric_only=True))

# group = df[df["Height"] > 1].groupby("Type2")["Height"].mean().sort_values(ascending=True)#this gives the pokemon with height >1 and then grouped by type2 find mean of heights and sort 
# print(group)

# Data Cleaning = process of fixing/removing: incomplete, incorrect, or irrelevant data.
#75% of work done with pandas is data cleaning
# df = df.drop(columns=["Legendary", "No"])#removing specific column from dataframe
# print(df)

#to drop missing data like nan
# df = df.dropna(subset=["Type2"]).to_string()#dropna = drop not available
# print(df)

# df = df.fillna({"Type2": "NoType"})
# print(df.to_string())

# df["Type1"] = df["Type1"].replace({"Grass":"Ghas Fhus", "Fire":"Aag Ka Tehelka", "Water":"Paniya ka Jalwa"})
# df = df.fillna({"Type2":"NoType"})
# print(df.to_string())


# df["Name"] = df["Name"].str.lower().str.contains("cubone")
# print(df.to_string())


# df["Legendary"] = df["Legendary"].astype(float)

#remove duplicate values
# print(df.to_string())
df = df.drop_duplicates()
df.reset_index(drop=True, inplace=True)
print(df.to_string())