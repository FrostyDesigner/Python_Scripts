from motion_capture import df
from bokeh.plotting import figure, show, output_file
from bokeh.models import HoverTool, ColumnDataSource

#convert start and end columns to strings for easy reading
df["Start_string"]=df["Start"].dt.strftime("%Y-%m-%d %H:%M:%S")
df["End_string"]=df["End"].dt.strftime("%Y-%m-%d %H:%M:%S")
 
cds=ColumnDataSource(df)

#commented because "responsive" does not work
#p=figure(x_axis_type='datetime', height=100, width=500, responsive=True, title="Motion Graph")
p=figure(x_axis_type='datetime', height=200, width=500, title="Motion Graph")
#remove ticks on y axis
p.yaxis.minor_tick_line_color=None
#remove grid lines from y grid
p.ygrid[0].ticker.desired_num_ticks=1

#instantiate hover tool
hover=HoverTool(tooltips=[("Start", "@Start_string"),("End", "@End_string")])
p.add_tools(hover)

#create the quad using left, right, up, down
#q=p.quad(left=df["Start"], right=df["End"], bottom=0, top=1, color="green")
#notice the source is cds (ColumnDataSource) - if you use a source the dataframe is not necessary
q=p.quad(left="Start", right="End", bottom=0, top=1, color="green", source=cds)

output_file("Graph.html")
show(p)