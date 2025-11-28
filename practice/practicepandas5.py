import pandas as pd

# Sample DataFrames for merge, concat, and join
df1 = pd.DataFrame({
    'key': ['A', 'B', 'C', 'D'],
    'value1': [1, 2, 3, 4]
})

df2 = pd.DataFrame({
    'key': ['C', 'D', 'E', 'F'],
    'value2': [5, 6, 7, 8]
})

df3 = pd.DataFrame({
    'key': ['A', 'B', 'X', 'Y'],
    'value3': [9, 10, 11, 12]
})

df_concat1 = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
df_concat2 = pd.DataFrame({'col1': [5, 6], 'col2': [7, 8]})
df_concat3 = pd.DataFrame({'col3': [9, 10], 'col4': [11, 12]})


print("--- Original DataFrames ---")
print("df1:\n", df1)
print("\ndf2:\n", df2)
print("\ndf3:\n", df3)
print("\ndf_concat1:\n", df_concat1)
print("\ndf_concat2:\n", df_concat2)
print("\ndf_concat3:\n", df_concat3)

# 1. merge example (similar to SQL JOIN)
print("\n--- pd.merge() Examples ---")
# Inner merge (default)
merged_inner = pd.merge(df1, df2, on='key', how='inner')
print("Inner Merge (on 'key'):\n", merged_inner)

# Outer merge
merged_outer = pd.merge(df1, df2, on='key', how='outer')
print("\nOuter Merge (on 'key'):\n", merged_outer)

# Left merge
merged_left = pd.merge(df1, df2, on='key', how='left')
print("\nLeft Merge (on 'key'):\n", merged_left)

# Right merge
merged_right = pd.merge(df1, df2, on='key', how='right')
print("\nRight Merge (on 'key'):\n", merged_right)

# 2. concat example (stacking DataFrames)
print("\n--- pd.concat() Examples ---")
# Concat rows (axis=0, default)
concatenated_rows = pd.concat([df_concat1, df_concat2])
print("Concatenated Rows:\n", concatenated_rows)

# Concat columns (axis=1)
concatenated_cols = pd.concat([df_concat1, df_concat3], axis=1)
print("\nConcatenated Columns:\n", concatenated_cols)

# Concat with ignore_index=True
concatenated_rows_reset_index = pd.concat([df_concat1, df_concat2], ignore_index=True)
print("\nConcatenated Rows (ignore_index=True):\n", concatenated_rows_reset_index)

# 3. join example (joining by index, or by column if specified)
print("\n--- df.join() Examples ---")
# Set 'key' as index for df1 and df3 for join operation
df1_indexed = df1.set_index('key')
df3_indexed = df3.set_index('key')

# Left join on index (default for df.join())
joined_left = df1_indexed.join(df3_indexed, how='left')
print("Left Join (on index):\n", joined_left)

# Inner join on index
joined_inner = df1_indexed.join(df3_indexed, how='inner')
print("\nInner Join (on index):\n", joined_inner)

# Join on a column (similar to merge with left_on/right_on)
# Re-create df1_indexed to avoid modifying it further for clarity
df1_indexed_for_join_on_col = df1.set_index('key')
df2_for_join_on_col = df2.set_index('key')
joined_on_column = df1_indexed_for_join_on_col.join(df2_for_join_on_col, how='inner')
print("\nJoin on column (by setting index first):\n", joined_on_column)