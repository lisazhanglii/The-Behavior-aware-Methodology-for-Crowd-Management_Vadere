import plotly.graph_objects as go

animals=['elderly people average time', 'normal people average time','average time of all','max time of all','min time of all', 'target1 time', 'target2 time','target3 time','target4 time']

fig = go.Figure(data=[
    go.Bar(name='4A', x=animals, y=[137.03230744840354, 68.04305597649217 , 85.252407040652,261.3668453460374,1.0594571622532003,239.35395757953458,236.28997188045076 ,261.3668453460374, 246.2424737154024]),
    go.Bar(name='4B', x=animals, y=[ 116.9165926450688,34.34253025742681 ,  54.95573232188958,259.4059401244799, 1.0781913339526217,259.4059401244799,62.87637753836189,56.338716807042665,62.319244997079615]),
    go.Bar(name='4C', x=animals,
           y=[64.82852834072433, 34.83734100607229,42.32412785906913, 129.35047245316724, 1.0322978705517505,
              129.35047245316724, 123.74924442756108, 119.66809649325573, 121.73802355977817]),
])
# Change the bar mode
fig.update_layout(barmode='group')
fig.update_layout(
    title_text='Comparison among Goup 4',
    yaxis_title="timestep",
    font=dict(size=35)  # Adjust the font size as desired
)
fig.show()
