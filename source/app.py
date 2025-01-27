# Import data from shared.py
from shared import df
import datetime
import plotly.express as px
from shiny import App, render, ui,reactive
from shinywidgets import render_plotly, output_widget, render_widget


# The contents of the first 'page' is a navset with two 'panels'.
page1 = ui.navset_card_underline(
    ui.nav_panel("Plot",output_widget("hist")),
    header=ui.layout_column_wrap(
        ui.input_selectize(
        "var", 
        "Select Countries", 
        choices=
        {'Southern Asia': {'Bangladesh': 'Bangladesh', 'Iran (Islamic Republic of)': 'Iran (Islamic Republic of)', 'India': 'India', 'Pakistan': 'Pakistan', 'Afghanistan': 'Afghanistan', 'Sri Lanka': 'Sri Lanka', 'Nepal': 'Nepal', 'Bhutan': 'Bhutan', 'Maldives': 'Maldives'}, 
        'Eastern Asia': {'China': 'China', 'Mongolia': 'Mongolia', 'Japan': 'Japan', 'Republic of Korea': 'Republic of Korea', 'China, Hong Kong Special Administrative Region': 'China, Hong Kong Special Administrative Region', 'Taiwan (Province of China)': 'Taiwan (Province of China)', "Democratic People's Republic of Korea": "Democratic People's Republic of Korea", 'China, Macao Special Administrative Region': 'China, Macao Special Administrative Region'}, 
        'South-eastern Asia': {'Indonesia': 'Indonesia', 'Philippines': 'Philippines', 'Viet Nam': 'Viet Nam', 'Thailand': 'Thailand', 'Malaysia': 'Malaysia', "Lao People's Democratic Republic": "Lao People's Democratic Republic", 'Cambodia': 'Cambodia', 'Singapore': 'Singapore', 'Myanmar': 'Myanmar', 'Timor-Leste': 'Timor-Leste'}, 
        'Western Asia': {'Israel': 'Israel', 'Jordan': 'Jordan', 'Türkiye': 'Türkiye', 'Saudi Arabia': 'Saudi Arabia', 'Cyprus': 'Cyprus', 'Bahrain': 'Bahrain', 'Yemen': 'Yemen', 'Iraq': 'Iraq', 'Azerbaijan': 'Azerbaijan', 'Georgia': 'Georgia', 'Lebanon': 'Lebanon', 'Syrian Arab Republic': 'Syrian Arab Republic', 'Armenia': 'Armenia', 'United Arab Emirates': 'United Arab Emirates', 'Oman': 'Oman', 'State of Palestine': 'State of Palestine', 'Qatar': 'Qatar', 'Kuwait': 'Kuwait'}, 
        'Central Asia': {'Kazakhstan': 'Kazakhstan', 'Kyrgyzstan': 'Kyrgyzstan', 'Tajikistan': 'Tajikistan', 'Turkmenistan': 'Turkmenistan', 'Uzbekistan': 'Uzbekistan'}},
        multiple=True,),
        #ui.input_date_range('range',"Select Date Range",min="2000-01-01", max="2025-01-01")
        ui.input_selectize(
            "type",
            "Select Disaster Group (Subgroup)",
            choices = 
            {'Natural':{'Biological':'Biological', 'Climatological':'Climatological', 'Geophysical':'Geophysical', 
                        'Hydrological':'Hydrological','Meteorological':'Meteorological'},
            'Technological':{'Industrial accident':'Industrial accident','Miscellaneous accident':'Miscellaneous accident', 'Transport':'Transport'}},
       multiple=True,),
       ui.input_selectize(
           'group',
           'Divide the timeline by?',
           choices=[]
    ),

    title="Disaster Timeline",
)
page2 = ui.navset_card_underline(
    title="Table",

)

app_ui = ui.page_navbar(
    ui.nav_spacer(),  # Push the navbar items to the right
    ui.nav_panel("Page 1", page1),
    ui.nav_panel("Page 2", page2),
    title="EM-Dat Dashboard",
)


def server(input, output, session):
    @render_widget
    def hist():
        return px.timeline(data(), 
                        x_start="Start Date", 
                        x_end="End Date", 
                        y='Country',
                        color="Disaster Subgroup",
                        opacity = 0.6,
                        hover_data = ['Start Date','End Date',
                                      "Disaster Group", "Disaster Subtype", 
                                      "Country",'Subregion','Location'])

    @reactive.calc
    def data():
        newdf = df[df['Country'].isin(input.var())].fillna('')
        newdf = newdf[newdf['Disaster Subgroup'].isin(input.type())]
        return newdf


app = App(app_ui, server)
