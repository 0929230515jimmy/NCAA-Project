import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

st.set_page_config(layout="wide")

# Data
data1 = {
    "Pts_diff": range(-10, 11),
    "20:00": [0.176, 0.203, 0.233, 0.266, 0.302, 0.341, 0.382, 0.424, 0.468, 0.512, 0.556, 0.600, 0.641, 0.681, 0.718, 0.753, 0.784, 0.813, 0.838, 0.861, 0.881],
    "16:00": [0.156, 0.183, 0.213, 0.247, 0.284, 0.325, 0.368, 0.414, 0.461, 0.509, 0.557, 0.603, 0.648, 0.690, 0.730, 0.766, 0.798, 0.828, 0.853, 0.876, 0.895],
    "12:00": [0.117, 0.142, 0.172, 0.207, 0.247, 0.291, 0.340, 0.393, 0.448, 0.504, 0.561, 0.615, 0.667, 0.716, 0.759, 0.798, 0.832, 0.862, 0.887, 0.907, 0.925],
    "8:00": [0.078, 0.100, 0.127, 0.159, 0.198, 0.245, 0.297, 0.356, 0.419, 0.486, 0.552, 0.617, 0.678, 0.734, 0.783, 0.825, 0.860, 0.889, 0.913, 0.932, 0.947],
    "4:00": [0.031, 0.044, 0.062, 0.087, 0.122, 0.167, 0.225, 0.296, 0.378, 0.469, 0.561, 0.649, 0.728, 0.795, 0.849, 0.891, 0.922, 0.945, 0.961, 0.973, 0.981]
}

data2 = {
    "Pts_diff": range(-10, 11),
    "20:00": [0.419, 0.453, 0.487, 0.513, 0.537, 0.561, 0.585, 0.608, 0.621, 0.621, 0.620, 0.620, 0.620, 0.611, 0.589, 0.558, 0.532, 0.495, 0.452, 0.409, 0.368],
    "16:00": [0.368, 0.418, 0.469, 0.518, 0.565, 0.612, 0.657, 0.672, 0.676, 0.679, 0.680, 0.680, 0.677, 0.654, 0.632, 0.613, 0.572, 0.516, 0.459, 0.404, 0.351],
    "12:00": [0.311, 0.382, 0.455, 0.527, 0.598, 0.664, 0.725, 0.760, 0.763, 0.763, 0.762, 0.760, 0.736, 0.689, 0.630, 0.564, 0.496, 0.427, 0.362, 0.301, 0.246],
    "8:00": [0.213, 0.288, 0.377, 0.475, 0.575, 0.669, 0.752, 0.819, 0.871, 0.876, 0.859, 0.840, 0.812, 0.750, 0.676, 0.593, 0.503, 0.414, 0.330, 0.255, 0.193],
    "4:00": [0.043, 0.090, 0.182, 0.332, 0.526, 0.713, 0.847, 0.925, 0.965, 0.979, 0.981, 0.976, 0.952, 0.906, 0.825, 0.697, 0.529, 0.354, 0.211, 0.116, 0.060]
}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

# Streamlit UI
st.title("Winning Percentage/ Close Game Percentage")

# Selection for datasets
dataset_option = st.selectbox("Choose dataset:", ["Winning Percentage", "Winning Percentage & Close Game Percentage"])


# Slider for Pts_diff
st.markdown("""
    <style>
    .stSlider [data-baseweb=slider]{
        width: 50%;
    }
    </style>
    """,unsafe_allow_html=True)
pts_diff = st.slider("Select a point difference:", -10, 10, 0)

# Function to plot the data
def plot_data(df, pts_diff, dataset_name, y_label):
    row = df[df["Pts_diff"] == pts_diff]
    fig, ax = plt.subplots(figsize=(10, 6))  # Make the plot larger
    for column in ["20:00", "16:00", "12:00", "8:00", "4:00"]:
        ax.plot(df["Pts_diff"], df[column], label=column, linestyle='-')
        ax.scatter(pts_diff, row[column].values[0], s=150)
    ax.set_title(f'{dataset_name} vs Points Difference & Time')
    ax.set_xlabel('Points Difference (Based on Home Team)')
    ax.set_ylabel(y_label)
    ax.set_xticks([-10, -8, -6, -4, -2, 0, 2, 4, 6, 8, 10])
    #plt.axhline(y=0.5, color='black', linestyle='--')
    ax.legend()
    return fig, row

# Conditional display based on selection
if dataset_option == "Winning Percentage":
    fig1, row1 = plot_data(df1, pts_diff, "Winning Percentage", "Winning Percentage")
    col1, col2 = st.columns([3, 2])  # Make the plot column wider
    with col1:
        st.pyplot(fig1)
    with col2:
        st.write(f"Values for Points Difference is {pts_diff}:")
        st.dataframe(row1.T.reset_index(), use_container_width=True)

else:
    fig1, row1 = plot_data(df1, pts_diff, "Winning Percentage", "Winning Percentage")
    fig2, row2 = plot_data(df2, pts_diff, "Close Game Percentage", "Close Game Percentage")
    col1, col2 = st.columns(2)
    with col1:
        st.pyplot(fig1)
    with col2:
        st.pyplot(fig2)
    st.write(f"Values for Points Difference is {pts_diff}:")
    combined_data = pd.concat([row1.set_index('Pts_diff').T, row2.set_index('Pts_diff').T], axis=1, keys=["Winning Percentage", "Close Game Percentage"]).reset_index()
    st.dataframe(combined_data, use_container_width=True)