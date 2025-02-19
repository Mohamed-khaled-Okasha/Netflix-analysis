import pandas as pd

# تحميل البيانات
file_path = r"D:\one drive\OneDrive\Desktop\uneeq interen for netflix\netflix_titles.csv"
df = pd.read_csv(file_path)

# تعويض القيم المفقودة
df["director"] = df["director"].fillna("Unknown")
df["cast"] = df["cast"].fillna("Unknown")
df["country"] = df["country"].fillna(df["country"].mode()[0])
df["date_added"] = df["date_added"].fillna(df["date_added"].mode()[0])
df["rating"] = df["rating"].fillna(df["rating"].mode()[0])
df["duration"] = df["duration"].fillna(df["duration"].mode()[0])

# حفظ الملف بعد المعالجة
output_file = "netflix_titles_cleaned.csv"
df.to_csv(output_file, index=False)
print(f"تم حفظ الملف بعد تعويض القيم المفقودة باسم {output_file}")
