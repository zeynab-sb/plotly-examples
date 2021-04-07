import plotly.express as px
  
df = px.data.tips()
  
fig_1 = px.histogram(df, x="total_bill",
                   histnorm='probability density')
fig_1.show()

fig_2 = px.histogram(df, x="total_bill", histnorm='percent')
fig_2.show()
