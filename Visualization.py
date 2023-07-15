import plotly.graph_objects as go

animals=['elderly people average time', 'normal people average time','average time of all','max time of all','min time of all', 'target1 time', 'target2 time','target3 time','target4 time']

fig = go.Figure(data=[
    go.Bar(name='3A', x=animals,
           y=[137.95825431845097, 70.45299131797083, 87.29216183900036, 263.18719871686767, 1.7573158401065287,
              263.18719871686767, 254.00911484491021, 227.02407388437624, 257.11459907907516]),
    go.Bar(name='3B', x=animals,
           y=[137.35171042699608, 32.96347692672582, 59.00309496787908, 262.28530690534507, 0.9983216485759147,
              262.28530690534507, 61.34306708182157, 62.58848713728867, 63.45084854144045]),
    go.Bar(name='3C', x=animals,
           y=[ 64.7064201753635, 33.483389316880775,41.27196634687646, 129.2925122975173,1.0869637129062302,
              122.33914170943808, 115.68436051983765, 129.2925122975173, 112.27147012648042])
])
# Change the bar mode
fig.update_layout(barmode='group')
fig.update_layout(
    title_text='Comparison among Goup 3',
    yaxis_title="timestep",
    font=dict(size=35)  # Adjust the font size as desired
)
fig.show()
