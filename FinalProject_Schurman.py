"""
Class: CS230--Section 004 
Name: Celia Schurman
Description: (Final Project - Skyscrapers)
I pledge that I have completed the programming assignment independently. 
I have not copied the code from a student or any source.
I have not given my code to any student.
"""
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import pydeck as pdk


st.title('Welcome to My CS 230 Final Project!')
st.header('The 100 Tallest Skyscrapers')
st.write('by Celia Schurman')
st.write('-' * 100)

st.sidebar.header('User Options')


df = pd.read_csv('Skyscrapers_2021.csv', header=0, names=["Rank", "Name", "City", "Address", "latitude",
                                                              "longitude", "Year Completed", "Height",
                                                              "Meters", "Feet", "Floors", "Materials",
                                                              "Function", "Link"])

df2 = df[["Rank", "Name", "City", 'latitude', 'longitude', 'Year Completed', 'Meters', 'Feet', 'Floors', 'Materials', 'Function']]

#need to remove the string elements from the columns for feet and meters
def convertingnums(df2):
    dfnew1 = df2.copy()
    dfnew1['Feet'] = dfnew1['Feet'].str.replace(' ft', '').str.replace(',', '').astype(float)

    dfnew2 = dfnew1.copy()
    dfnew2['Year Completed'] = dfnew2['Year Completed'].astype(int)

    dfnew = dfnew2.copy()
    dfnew['Meters'] = dfnew['Meters'].str.replace(' m', '').astype(float)

    return dfnew


dfnew = convertingnums(df2)

dfnew.at[70, 'Floors'] = 74 #fixing this one N/A value, obtained 74 value online

#simple map of all locations
dfmap = dfnew[['Name', 'latitude', 'longitude']]

st.subheader('Locations of Tallest Skyscrapers')
st.map(dfmap)
st.write('-' * 100)


#function to determine the 5 cities with the most skyscrapers on the list
def cityfunc(dfnew):
    citylist = sorted([city for city in dfnew["City"]])

    keys = []
    for city in citylist:
        if city not in keys:
            keys.append(city)

    citydict = dict.fromkeys(keys, 0)

    for city in keys:
        citycount = citylist.count(city)
        citydict[city] = citycount

    sorted_values = sorted(citydict.values(), key=int, reverse=True) # Sort the values
    sorted_dict = {}

    for i in sorted_values:
        for k in citydict.keys():
            if citydict[k] == i:
                sorted_dict[k] = citydict[k]

    sortedkeys = list(sorted_dict.keys())

    top5cities = [sortedkeys[x] for x in range(5)]

    return top5cities


top5cities = cityfunc(dfnew)



#df3 = df2[df2['City'].isin(top5cities)]
#print(df3)


dfcity0 = dfnew.loc[dfnew['City'] == top5cities[0]]

dfcity1 = dfnew.loc[dfnew['City'] == top5cities[1]]

dfcity2 = dfnew.loc[dfnew['City'] == top5cities[2]]

dfcity3 = dfnew.loc[dfnew['City'] == top5cities[3]]

dfcity4 = dfnew.loc[dfnew['City'] == top5cities[4]]


st.subheader('3D Map of Top 5 Cities')
city = st.sidebar.radio('Choose a city to view on the 3D map: ', (top5cities))
st.sidebar.write('-' * 50)

if city == 'Dubai':
    st.write(f'You selected {city}')
    st.write(f'Of the tallest 100 skyscrapers, {dfnew["City"].value_counts()[city]} are in {city}')
    #making a 3d map
    # setup default view box
    view = pdk.data_utils.compute_view(dfcity0[["longitude", "latitude"]])
    view.pitch = 70
    # create mapping from population to color
    plasma = cm = plt.get_cmap('plasma')
    cNorm = colors.Normalize(vmin=dfnew["Feet"].min(), vmax=dfcity0["Feet"].max())
    scalarMap = plt.cm.ScalarMappable(norm=cNorm, cmap=plasma)
    dfcity0["color"] = dfcity0.apply(lambda row: scalarMap.to_rgba(row["Feet"]), axis=1)

    # create column layer in pydeck
    column_layer = pdk.Layer(
        "ColumnLayer",
        data=dfcity0,
        get_position=["longitude", "latitude"],
        get_elevation="Feet",
        elevation_scale=1,
        radius=60,
        pickable=True,
        get_fill_color="[255]",
        auto_highlight=True,
    )
    # add tooltip
    tooltip = {
        "html": "",
        "style": {"background": "grey", "color": "white", "font-family": '"Helvetica Neue", Arial', "z-index": "10000"},
    }
    mappy = pdk.Deck(column_layer, initial_view_state=view, tooltip=tooltip)
    st.pydeck_chart(mappy)

elif city == 'New York City':
    st.write(f'You selected {city}')
    st.write(f'Of the tallest 100 skyscrapers, {dfnew["City"].value_counts()[city]} are in {city}')
    #making a 3d map
    # setup default view box
    view = pdk.data_utils.compute_view(dfcity1[["longitude", "latitude"]])
    view.pitch = 70
    # create mapping from population to color
    plasma = cm = plt.get_cmap('plasma')
    cNorm = colors.Normalize(vmin=dfnew["Feet"].min(), vmax=dfcity1["Feet"].max())
    scalarMap = plt.cm.ScalarMappable(norm=cNorm, cmap=plasma)
    dfcity1["color"] = dfcity1.apply(lambda row: scalarMap.to_rgba(row["Feet"]), axis=1)

    # create column layer in pydeck
    column_layer = pdk.Layer(
        "ColumnLayer",
        data=dfcity1,
        get_position=["longitude", "latitude"],
        get_elevation="Feet",
        elevation_scale=1,
        radius=60,
        pickable=True,
        get_fill_color="[255]",
        auto_highlight=True,
    )
    # add tooltip
    tooltip = {
        "html": "",
        "style": {"background": "grey", "color": "white", "font-family": '"Helvetica Neue", Arial', "z-index": "10000"},
    }
    mappy = pdk.Deck(column_layer, initial_view_state=view, tooltip=tooltip)
    st.pydeck_chart(mappy)

elif city == 'Shenzhen':
    st.write(f'You selected {city}')
    st.write(f'Of the tallest 100 skyscrapers, {dfnew["City"].value_counts()[city]} are in {city}')
    #making a 3d map
    # setup default view box
    view = pdk.data_utils.compute_view(dfcity2[["longitude", "latitude"]])
    view.pitch = 70
    # create mapping from population to color
    plasma = cm = plt.get_cmap('plasma')
    cNorm = colors.Normalize(vmin=dfnew["Feet"].min(), vmax=dfcity2["Feet"].max())
    scalarMap = plt.cm.ScalarMappable(norm=cNorm, cmap=plasma)
    dfcity2["color"] = dfcity2.apply(lambda row: scalarMap.to_rgba(row["Feet"]), axis=1)

    # create column layer in pydeck
    column_layer = pdk.Layer(
        "ColumnLayer",
        data=dfcity2,
        get_position=["longitude", "latitude"],
        get_elevation="Feet",
        elevation_scale=1,
        radius=60,
        pickable=True,
        get_fill_color="[255]",
        auto_highlight=True,
    )
    # add tooltip
    tooltip = {
        "html": "",
        "style": {"background": "grey", "color": "white", "font-family": '"Helvetica Neue", Arial', "z-index": "10000"},
    }
    mappy = pdk.Deck(column_layer, initial_view_state=view, tooltip=tooltip)
    st.pydeck_chart(mappy)

elif city == 'Chicago':
    st.write(f'You selected {city}')
    st.write(f'Of the tallest 100 skyscrapers, {dfnew["City"].value_counts()[city]} are in {city}')
    #making a 3d map
    # setup default view box
    view = pdk.data_utils.compute_view(dfcity3[["longitude", "latitude"]])
    view.pitch = 70
    # create mapping from population to color
    plasma = cm = plt.get_cmap('plasma')
    cNorm = colors.Normalize(vmin=dfnew["Feet"].min(), vmax=dfcity3["Feet"].max())
    scalarMap = plt.cm.ScalarMappable(norm=cNorm, cmap=plasma)
    dfcity3["color"] = dfcity3.apply(lambda row: scalarMap.to_rgba(row["Feet"]), axis=1)

    # create column layer in pydeck
    column_layer = pdk.Layer(
        "ColumnLayer",
        data=dfcity3,
        get_position=["longitude", "latitude"],
        get_elevation="Feet",
        elevation_scale=1,
        radius=60,
        pickable=True,
        get_fill_color="[255]",
        auto_highlight=True,
    )
    # add tooltip
    tooltip = {
        "html": "",
        "style": {"background": "grey", "color": "white", "font-family": '"Helvetica Neue", Arial', "z-index": "10000"},
    }
    mappy = pdk.Deck(column_layer, initial_view_state=view, tooltip=tooltip)
    st.pydeck_chart(mappy)

else:
    st.write(f'You selected {city}')
    st.write(f'Of the tallest 100 skyscrapers, {dfnew["City"].value_counts()[city]} are in {city}')
    #making a 3d map
    # setup default view box
    view = pdk.data_utils.compute_view(dfcity4[["longitude", "latitude"]])
    view.pitch = 70
    # create mapping from population to color
    plasma = cm = plt.get_cmap('plasma')
    cNorm = colors.Normalize(vmin=dfnew["Feet"].min(), vmax=dfcity4["Feet"].max())
    scalarMap = plt.cm.ScalarMappable(norm=cNorm, cmap=plasma)
    dfcity4["color"] = dfcity4.apply(lambda row: scalarMap.to_rgba(row["Feet"]), axis=1)

    # create column layer in pydeck
    column_layer = pdk.Layer(
        "ColumnLayer",
        data=dfcity4,
        get_position=["longitude", "latitude"],
        get_elevation="Feet",
        elevation_scale=1,
        radius=60,
        pickable=True,
        get_fill_color="[255]",
        auto_highlight=True,
    )
    # add tooltip
    tooltip = {
        "html": "",
        "style": {"background": "grey", "color": "white", "font-family": '"Helvetica Neue", Arial', "z-index": "10000"},
    }
    mappy = pdk.Deck(column_layer, initial_view_state=view, tooltip=tooltip)
    st.pydeck_chart(mappy)

st.write('-' * 100)

#making a bar chart of skyscrapers

num = st.sidebar.slider('Choose how many of the tallest skyscrapers you would like to view on the graph:', 1, 100)
datatype = st.sidebar.radio('Display the data in feet, meters, or floors?', ('Feet', 'Meters', 'Floors', 'Feet per Floor'))

dfnew['Feet per Floor'] = dfnew['Feet'] / dfnew['Floors']

dfchart = dfnew[datatype][(dfnew.Rank <= num)]
st.subheader('Characteristics of the Tallest Skyscrapers')
st.write('Ordered by Rank')
st.bar_chart(dfchart, y=datatype)

st.sidebar.write('-' * 50)
st.sidebar.write('Want to know the building at a specific index?')
indexcheck = st.sidebar.number_input('Enter a number: ')
namecheck = dfnew.loc[df['Rank'] == indexcheck]
st.sidebar.write(namecheck[['Rank', 'Name', 'City', 'Year Completed']])


#yearlower = st.slider('Choose a starting year:', 1931, 2020)
#yearupper = st.slider('Choose an ending year:', 1931, 2020)

newdf = dfnew.copy()
dfyear = newdf.sort_values(by=['Year Completed'])
dfyear.set_index('Year Completed', inplace=True)
dfchart = dfyear['Feet']
st.write('-' * 100)
st.subheader('How Many Feet of the Top 100 Were Built Over Time')
st.bar_chart(dfchart)


def matfunc():
    materials = []
    for material in dfnew['Materials']:
        if material not in materials:
            materials.append(material)

    matdict = dict.fromkeys(materials, 0)

    for material in materials:
        matcount = dfnew['Materials'].value_counts()[material]
        matdict[material] = matcount

    return matdict


matdict = matfunc()


def funcfunc():
    funcs = ['residential', 'office', 'hotel', 'retail']

    funcdict = dict.fromkeys(funcs, 0)

    for function in funcs:
        xcount = dfnew.Function.str.count(function).sum()
        funcdict[function] = xcount

    return funcdict


funcdict = funcfunc()

st.sidebar.write('-' * 50)
viewchoice = st.sidebar.radio('Would you like to view the frequency of building materials or functions?', ['Materials', 'Functions'])
st.write('-' * 100)

if viewchoice == 'Materials':
    st.subheader('Number of Buildings by Material Type')
    labels = list(matdict.keys())
    vals = list(matdict.values())
    dffun = pd.DataFrame(vals, index=labels, columns=['Count'])
    st.bar_chart(dffun)
else:
    st.subheader('Number of Buildings by Function')
    st.write('Note: Building functions not mutually exclusive')
    labels = list(funcdict.keys())
    vals = list(funcdict.values())
    dffun = pd.DataFrame(vals, index=labels, columns=['Count'])
    st.bar_chart(dffun)

#pivot = dfnew.pivot_table('Feet'.count(dfnew['Feet']), index='Materials', columns='Year Completed')
#st.write(pivot)
