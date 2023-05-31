import plotly.graph_objects as go

animals=['elderly average time', 'non_elderly average time','all average','all max','all min', 'target1 time', 'target2 time','target3 time','target4 time']

fig = go.Figure(data=[
    go.Bar(name='mixed', x=animals, y=[ 73.9025639123458,56.88612051916061,  62.03949525967702,111.96370257959995,14.629752366543476, 61.05731786403891,88.18202676174066, 111.30356232764966,89.46792732908112]),
    go.Bar(name='separated', x=animals, y=[56.565256856436186, 64.28523081025956 ,   61.94726171461348,86.771128133520124,18.99905687076192,85.70079559022237,82.83913592896161,86.18356943873427,82.04863510128722])
])
# Change the bar mode
fig.update_layout(barmode='group')
fig.update_layout(
    title_text='Comparison between Experiment 3 & Experiment 4',
    font=dict(size=35)  # Adjust the font size as desired
)
fig.show()