import plotly.graph_objects as go

animals=['elderly people average time', 'normal people average time','average time of all','max time of all','min time of all', 'target1 time', 'target2 time','target3 time','target4 time']

fig = go.Figure(data=[
    go.Bar(name='1A', x=animals,
           y=[149.86777268885785, 80.90661410593758, 98.10895740615246, 201.05943159974342, 41.90069788631746,
              201.05943159974342, 186.69418143435564, 194.75466769210482, 194.69235075844935]),
    go.Bar(name='1B', x=animals,
           y=[154.31472688320747, 72.3733452271568, 92.813601839818, 199.2776749110113, 42.19475878906342,
              198.05756647597443, 98.5361291088928, 87.92504386133656, 98.03412212468199]),
    go.Bar(name='1C', x=animals,
           y=[  125.71154537721017,68.28935086571744, 82.61330254136493,149.97949549961695,42.67181122915116,
                143.07434578022733,143.57632298908183,146.27671375168768,149.97949549961695])
])
# Change the bar mode
fig.update_layout(barmode='group')
fig.update_layout(
    title_text='Comparison among Goup 1',
    yaxis_title="timestep",
    font=dict(size=35)  # Adjust the font size as desired
)
fig.show()
