# --- Code for creating scatter maps:
# Credits: Manoj Pravakar Saha on https://manojsaha.com/2017/03/08/drawing-locations-google-maps-python/

# --- Code for converting longitude and latitude values to cities:
# https://stackoverflow.com/questions/20169467/how-to-convert-from-longitude-and-latitude-to-country-or-city

import gmplot
import pandas as pd
from random import randint

def plot_map(path_to_csv_file, column_with_geo_codes):

    # Convert column_with_geo_codes to int:
    column_with_geo_codes = int(column_with_geo_codes)

    #Set the cursor
    # cur = db_conn.cursor()
    
    # Initialize two empty lists to hold the latitude and longitude values
    latitude = [40.835295]
    longitude = [-97.700743]
    
    # Import csv with data as dataframe
    df = pd.read_csv(path_to_csv_file)
    
    # TODO: Convert column "geo_location" to longitude and latitude, and scatter randomly for better visualization
    # TODO: 1. Cut df's geo column after first two letters; add column with coordinates. Use for loop but
    # SKIP GOOGLE SEARCH OF LOCATIONS!! But save routine anyway, may be needed later
    
    i = 5
    
    # Convert abbreviated location codes into country, state and area names (as far as applicable)
    df_locations = pd.read_csv('csv/country_codes.csv')
    ### print ("df_locations.iloc[0:3,0:7]", df_locations.iloc[0:3,0:7])
    ### print ("column_with_geo_codes: ", column_with_geo_codes)
    # Extract column with location information from main dataframe
    df_entry_location = df.iloc[:,(column_with_geo_codes-1):(column_with_geo_codes)]
    
    # Get the string element providing the location information from the current row in df_entry_location
    df_entry_location_0 = df_entry_location.iloc[i,0]
    # Determine where the country information ends (and state/area information begins, e.g. in US>TX>632)
    try:
        df_entry_country_index_end = df_entry_location_0.index(">", 0)
        df_entry_country = df_entry_location_0[0:(df_entry_country_index_end)]
    except ValueError:
        # print ("enter EXCEPTION")
        df_entry_country_index_end = len(df_entry_location_0)
        df_entry_country = df_entry_location_0
    ### print ("df_entry_country", df_entry_country)
    ### print (df_entry_country_index_end)
    ### print (type(df_entry_country_index_end))
    ### print ()
    # If an available 2-letter country code is found, look up if there is a corresponding country name in the country_codes series element
    # First, create two series elements from df_locations, one with the country codes and one with the country names
    df_locations_codes = df_locations.iloc[:,1:2]
    df_locations_codes = df_locations_codes.iloc[:,0]
    df_locations_countries = df_locations.iloc[:,0:1]
    df_locations_countries = df_locations_countries.iloc[:,0]


    # Determine length of latitude and longitude lists; create equally long lists with random values
    # from range 0 to 10; add these lists to latitude and longitude arrays
    
    # Close the cursor and the database connection 
    # cur.close()
    
    # Create some statistics on users' geographical location
    # First, create series element of geographical locations
    counts = df_entry_location.iloc[:,0].value_counts()
    print (type(counts))
    print (counts)

if __name__ == "__main__":
    import sys
    if len(sys.argv) is not 3:
        print ("Usage: python plot_map.py path_to_csv_file column_with_geo_codes_element_of{1, 2, 3, ...}")
    else:
        # PATH TO CSV FILE TO BE EXPLORED ON YOUR DISK
        path_to_csv_file = sys.argv[1]
        # NUMBER OF ROWS TO BE SHOWN
        column_with_geo_codes = sys.argv[2]
        plot_map(path_to_csv_file, column_with_geo_codes)
