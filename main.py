from bokeh.plotting import figure, output_file , show , ColumnDataSource
import pandas

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
    color = 'green',
    fill_alpha = 0.5,
    source = source
)

show(p)