from io import BytesIO
from flask import Blueprint, render_template, send_file
from website import create_app
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import numpy as np
import pandas as pd
import networkx as nx
import nxviz as nv
import matplotlib.pyplot as plt
import math
import jinja2


app = create_app()
#my_loader = jinja2.ChoiceLoader([app.jinja_loader,jinja2.FileSystemLoader('/')])




if __name__ == '__main__':
    app.run(debug=True)
    
