from bokeh.plotting import figure, output_file , show , save,  ColumnDataSource
import pandas
from bokeh.models.tools import HoverTool
from bokeh.transform import factor_cmap
from bokeh.palettes import Reds8


df  = pandas.read_csv('cars.csv')

source = ColumnDataSource(df)

output_file('index.html')

car_list = source.data['Car'].tolist()

p = figure(
    y_range = car_list,
    plot_width = 750,
    plot_height = 650,
    title = 'Cars with Top Horsepower',
    x_axis_label = 'Horsepower',
    tools = "pan, box_select , zoom_in , zoom_out, save, reset",
   
)

p.hbar(
    y = 'Car',
    right = 'Horsepower',
    left = 0,
    height = 0.5,
    fill_color=factor_cmap(
      'Car',
      palette=Reds8,
      factors=car_list
    ),
    fill_alpha = 0.9,
    source = source,
    legend = 'Car'
)

p.legend.orientation = 'vertical'
p.legend.location = 'top_right'
p.legend.label_text_font_size = '10px'

hover = HoverTool()
hover.tooltips = """
    <div>
        <h3>@Car</h3>
        <div><strong>HP: </strong>@Horsepower</div>
        <div><strong>Price: </strong>@Price</div>
        <div> <img src = "@Image" alt = "" width = "200" /> </div> 
    </div>
"""

p.add_tools(hover)

save(p)