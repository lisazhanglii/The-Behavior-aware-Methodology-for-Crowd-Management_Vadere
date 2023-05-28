import plotly.graph_objects as go
animals=['elderly average time', 'non_elderly average time','all average','all max','all min', 'target1 time', 'target2 time','target3 time','target4 time']

fig = go.Figure(data=[
    go.Bar(name='mixed', x=animals, y=[ 71.03006618297509,55.87540326356676, 60.46494382062561,87.06156609471921,33.53230999216885,86.32714604306905,84.47645315428491, 86.09329480338532,86.05695909053276]),
    go.Bar(name='separated', x=animals, y=[ 84.24787463042958 ,56.629830420819765,  64.99386561452353,115.66457818734484,33.42727853570953, 115.00966581128039,79.29743705551918,65.5873104326152,78.0290610158351])
])
# Change the bar mode
fig.update_layout(barmode='group')
fig.update_layout(title_text='Comparison between Experiment 3 & Experiment 4')
fig.show()