# Import data from shared.py
from shared import df
import datetime
import plotly.express as px
from shiny import App, render, ui,reactive
from shinywidgets import render_plotly, output_widget, render_widget


# The contents of the first 'page' is a navset with two 'panels'.
page1 = ui.navset_card_underline(
    ui.nav_panel("Plot",output_widget("hist")),
    footer=ui.input_select(
        "var", 
        "Select variable", 
        choices=["China", "Japan"]
    ),
    title="Disaster Timeline",
)

app_ui = ui.page_navbar(
    ui.nav_spacer(),  # Push the navbar items to the right
    ui.nav_panel("Page 1", page1),
    ui.nav_panel("Page 2", "This is the second 'page'."),
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
        return df[df['Country']==input.var()].fillna('')


app = App(app_ui, server)
