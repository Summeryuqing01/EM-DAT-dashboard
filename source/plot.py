import plotly.express as px
from ipyleaflet import GeoJSON, Map, Marker  

def timeline():
        return px.timeline(data(), 
                        x_start="Start Date", 
                        x_end="End Date", 
                        y=input.group(),
                        color=input.legend(),
                        opacity = 0.6,
                        hover_data = ['Start Date','End Date', 'Event Name',
                                      "Disaster Group", "Disaster Subtype", 
                                      "Country",'Subregion','Location'])

def country_timeline():
        return px.timeline(select_year(),
                            x_start="Start Date", 
                            x_end="End Date", 
                             y='DisNo.',
                            color='Disaster Subgroup',
                            opacity = 0.6,
                            hover_data = ['Start Date','End Date',
                            "Disaster Group", "Disaster Subtype", 
                            "Country",'Subregion','Location'])

def map():
        map = Map(center=(-20,120), zoom=3)
        return map