#1. IMPORTAMOS LIBRERÍAS NECESARIAS
import bokeh
from bokeh.plotting import figure, show

#2. IMPORTAMOS O CREAMOS DATOS
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
y1 = [5, 7, 10, 12, 15, 21, 22, 26, 20, 16, 11, 5]
y2 = [25, 16, 15, 12, 11, 8, 2, 3, 4, 17, 27, 3]
y3 = [5, 7, 10, 12, 15, 21, 22, 26, 20, 16, 11, 5]

#3. CREAMOS EL ENTORNO GRÁFICO
grafico = figure(title="GRÁFICO SOBRE EVOLUCIÓN DE TEMPERATURAS EN EL AÑO 2023", x_axis_label="x", y_axis_label="y")

#4. AÑADIMOS CONTENIDO
    # EN BARRAS HORIZONTALES VAN LAS TEMPERATURAS MEDIAS POR MES (Y1)
grafico.vbar(x=x, top=y1, legend_label="TEMPERATURA MEDIA", width=0.5, bottom=0, color="red")
    # EN LINEAS VAN LAS PRECIPITACIONES MEDIAS POR MES (Y1)
grafico.line(x, y2, legend_label="PRECIPITACIONES", color="blue", line_width=2)            
                        
#5. AJUSTE DE LA LEYENDA DEL GRÁFICO
grafico.legend.location = "top_left"
grafico.legend.title = "LEYENDA"
grafico.legend.label_text_font = "arial"
grafico.legend.label_text_font_style = "italic"
grafico.legend.label_text_color = "white"
grafico.legend.border_line_width = 2
grafico.legend.border_line_color = "red"
grafico.legend.border_line_alpha = 0.8
grafico.legend.background_fill_color = "red"
grafico.legend.background_fill_alpha = 0.2

#6. MOSTRAR EL GRÁFICO
show(grafico)
