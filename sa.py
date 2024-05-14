import streamlit as st

# Table 1 data
table1_data = {
    "Index #": ["A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8", "A9", "A10",
                "A11", "A12", "A13", "A14", "A15", "A16", "A17", "A18", "A19", "A20"],
    "Value": [41, 18, 21, 63, 2, 53, 5, 57, 60, 93,
              28, 3, 90, 39, 80, 88, 49, 60, 26, 28]
}

# Table 1
st.write("Table 1")
st.table(table1_data)

# Calculate values for the processed table
alpha_value = table1_data["Value"][4] + table1_data["Value"][19]
beta_value = table1_data["Value"][14] / table1_data["Value"][6]
charlie_value = table1_data["Value"][12] * table1_data["Value"][11]

# Processed Table data
processed_table_data = {
    "Category": ["Alpha", "Beta", "Charlie"],
    "Value": [alpha_value, beta_value, charlie_value]
}

# Display Processed Table
st.write(" Processed of the Table")
st.table(processed_table_data)
