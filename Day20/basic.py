import plotly.express as px
import pandas as pd

df = pd.DataFrame({
    "dept": ["IT", "HR", "IT"],
    "salary": [50000, 40000, 60000]
})

fig = px.bar(df, x="dept", y="salary")
fig.show()