import plotly.graph_objects as go

animals=['elderly people average time', 'normal people average time','average time of all','max time of all','min time of all', 'target1 time', 'target2 time','target3 time','target4 time']

fig = go.Figure(data=[
    go.Bar(name='4A', x=animals,
           y=[140.7431154898377, 69.54633859948615,  87.30635631241317,258.2603547814365, 1.554266560091094,
              226.16314347416136,  233.01032349420956, 258.2603547814365,250.42990305321788]),
    go.Bar(name='4B', x=animals,
           y=[78.99595774047935, 41.838353565368735, 51.107308385278934, 131.56103903293, 1.0353771627344859,
              131.56103903293,122.0203000074482, 119.8394385383057, 115.76157615967657]),
    go.Bar(name='4C', x=animals,
           y=[ 91.17921684384936,58.28258703283709,  66.48864289178366,260.4503189153044,3.175513970026173,
                260.4503189153044, 93.22922969306381,60.26401245413363,90.32402532714433])
])
# Change the bar mode
fig.update_layout(barmode='group')
fig.update_layout(
    title_text='Comparison among Goup 4',
    yaxis_title="timestep",
    font=dict(size=35)  # Adjust the font size as desired
)
fig.show()
