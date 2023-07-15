import plotly.graph_objects as go

animals=['elderly people average time', 'normal people average time','average time of all','max time of all','min time of all', 'target1 time', 'target2 time','target3 time','target4 time']

fig = go.Figure(data=[
    go.Bar(name='2A', x=animals, y=[ 153.38387280921125 ,83.75716800399508, 101.1255316384584,250.28557690493045,19.452932075223554,143.1199839253212,192.52659518771003,250.28557690493045,200.44294598899296]),
    go.Bar(name='2B', x=animals, y=[ 96.97298864313396,83.05952174561301, 86.53023249040915,139.87105382840673,46.01941123957316,139.87105382840673,104.51361717096081, 115.11970247143795,102.71549292826388]),
    go.Bar(name='2C', x=animals,
           y=[ 132.06174174079118,70.90393934516491, 86.15973744825584,203.54903103365007,19.249885981874648,
               89.50112690120778, 153.37605980427136,203.54903103365007,157.7323955120668])
])
# Change the bar mode
fig.update_layout(barmode='group')
fig.update_layout(
    title_text='Comparison among Goup 2',
    yaxis_title="timestep",
    font=dict(size=35)  # Adjust the font size as desired
)
fig.show()
