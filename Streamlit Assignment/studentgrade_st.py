import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.express as px
from io import StringIO

# --------------------------------------------------
# Page Config
# --------------------------------------------------
st.set_page_config(
    page_title="Student Grade Management System",
    page_icon="🎓",
    layout="wide"
)

# --------------------------------------------------
# Custom Styling
# --------------------------------------------------
st.markdown("""
<style>
.main-title{
    text-align:center;
    color:#1E88E5;
    font-size:42px;
    font-weight:bold;
}
.metric-card{
    background-color:#f5f7fa;
    padding:15px;
    border-radius:12px;
    box-shadow:0px 2px 8px rgba(0,0,0,0.1);
}
</style>
""", unsafe_allow_html=True)

st.markdown(
    "<div class='main-title'>🎓 Student Grade Management System</div>",
    unsafe_allow_html=True
)

st.write("")

# --------------------------------------------------
# Grade Function
# --------------------------------------------------
def calculate_grade(avg):
    if avg >= 90:
        return "A+"
    elif avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 50:
        return "D"
    else:
        return "F"

# --------------------------------------------------
# Sidebar
# --------------------------------------------------
st.sidebar.header("⚙️ Student Entry")

num_students = st.sidebar.number_input(
    "Number of Students",
    min_value=1,
    max_value=50,
    value=5
)

students = []

for i in range(num_students):
    st.sidebar.subheader(f"Student {i+1}")

    name = st.sidebar.text_input(
        f"Name {i+1}",
        value=f"Student {i+1}"
    )

    math = st.sidebar.number_input(
        f"Math Marks ({i+1})",
        0, 100, 75,
        key=f"math{i}"
    )

    science = st.sidebar.number_input(
        f"Science Marks ({i+1})",
        0, 100, 70,
        key=f"sci{i}"
    )

    english = st.sidebar.number_input(
        f"English Marks ({i+1})",
        0, 100, 80,
        key=f"eng{i}"
    )

    avg = round((math + science + english) / 3, 2)
    grade = calculate_grade(avg)

    students.append([
        name,
        math,
        science,
        english,
        avg,
        grade
    ])

# --------------------------------------------------
# DataFrame
# --------------------------------------------------
df = pd.DataFrame(
    students,
    columns=[
        "Name",
        "Math",
        "Science",
        "English",
        "Average",
        "Grade"
    ]
)

# --------------------------------------------------
# KPIs
# --------------------------------------------------
overall_avg = round(df["Average"].mean(), 2)

topper_name = df.loc[
    df["Average"].idxmax(),
    "Name"
]

top_score = df["Average"].max()

pass_rate = round(
    (df["Grade"] != "F").sum()
    / len(df) * 100,
    1
)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "📊 Class Average",
        overall_avg
    )

with col2:
    st.metric(
        "🏆 Topper",
        topper_name
    )

with col3:
    st.metric(
        "✅ Pass Rate",
        f"{pass_rate}%"
    )

st.divider()

# --------------------------------------------------
# Student Results Table
# --------------------------------------------------
st.subheader("📋 Student Results")

st.dataframe(
    df,
    use_container_width=True,
    hide_index=True
)

# --------------------------------------------------
# Charts
# --------------------------------------------------
left, right = st.columns(2)

with left:
    st.subheader("📈 Average Score by Student")

    fig_bar = px.bar(
        df,
        x="Name",
        y="Average",
        color="Average",
        text="Average",
        color_continuous_scale="Blues"
    )

    fig_bar.update_layout(
        xaxis_title="Student",
        yaxis_title="Average Marks"
    )

    st.plotly_chart(
        fig_bar,
        use_container_width=True
    )

with right:
    st.subheader("🎯 Grade Distribution")

    grade_count = (
        df["Grade"]
        .value_counts()
        .reset_index()
    )

    grade_count.columns = [
        "Grade",
        "Count"
    ]

    fig_pie = px.pie(
        grade_count,
        names="Grade",
        values="Count",
        hole=0.5
    )

    st.plotly_chart(
        fig_pie,
        use_container_width=True
    )

# --------------------------------------------------
# Subject Analysis
# --------------------------------------------------
st.subheader("📚 Subject Performance")

subject_avg = pd.DataFrame({
    "Subject": ["Math", "Science", "English"],
    "Average Score": [
        df["Math"].mean(),
        df["Science"].mean(),
        df["English"].mean()
    ]
})

fig_subject = px.bar(
    subject_avg,
    x="Subject",
    y="Average Score",
    color="Average Score",
    text_auto=".2f",
    color_continuous_scale="Viridis"
)

st.plotly_chart(
    fig_subject,
    use_container_width=True
)

# --------------------------------------------------
# Student Report Card
# --------------------------------------------------
st.subheader("🎓 Individual Report Card")

selected_student = st.selectbox(
    "Choose Student",
    df["Name"]
)

student = df[df["Name"] == selected_student].iloc[0]

c1, c2, c3, c4 = st.columns(4)

c1.metric("Math", student["Math"])
c2.metric("Science", student["Science"])
c3.metric("English", student["English"])
c4.metric("Grade", student["Grade"])

# --------------------------------------------------
# CSV Download
# --------------------------------------------------
st.subheader("⬇️ Download Results")

csv = df.to_csv(index=False)

st.download_button(
    label="Download CSV",
    data=csv,
    file_name="student_grades.csv",
    mime="text/csv"
)

st.success("System Ready ✔️")