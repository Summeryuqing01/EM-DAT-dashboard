import plotly.express as px
from ipyleaflet import GeoJSON, Map, Marker  
from shiny import ui
import datetime
from shared import df


def data():
        newdf = df[df['Country'].isin(input.var())].fillna('')
        newdf = newdf[newdf['Disaster Subgroup'].isin(input.type())]
        return newdf

def select_year():
        newdf = df[df['Country']=='Indonesia'].fillna('')
        year = int(input.year())
        newdf = newdf[(newdf['Start Year']==year)|(newdf['End Year']==year)]
        return newdf

