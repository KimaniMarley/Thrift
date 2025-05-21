import psycopg2
import folium
from folium import plugins

# Connect to your PostgreSQL database
POSTGRES_USER = "postgres"
POSTGRES_PASSWORD = "Kimani"
POSTGRES_DB = "Morphius"
def connect_to_postgres():
    try:
        conn = psycopg2.connect(
            user=POSTGRES_USER,
            password=POSTGRES_PASSWORD,
            database=POSTGRES_DB,
            host="localhost",
            port="5432",
        )
        print("Successfully connected to the PostgreSQL database")
        return conn
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error while connecting to PostgreSQL", error)

# Call the function to connect to the database
conn = connect_to_postgres()
conn.autocommit = False
if conn is not None:
    cur = conn.cursor()
    cur.execute('SELECT "name", "x", "y" FROM "Health"')
    rows = cur.fetchall()

    cur.execute('SELECT "school_nam", "x_coord", "y_coord" FROM "Schools"')
    school_rows = cur.fetchall()

    # Create the map
m = folium.Map(location=(-1.286389, 36.817223), zoom_start=15)

    # Create a feature group for health markers
health_group = folium.FeatureGroup(name="Health Facilities")
for row in rows:
        name, x, y = row
        health_group.add_child(
            folium.Marker(
                location=[y, x],  # Note: Folium expects coordinates as [latitude, longitude]
popup=folium.Popup(f"<b>Name:</b> {name}"),
                icon=folium.Icon(color='green', icon='hospital', prefix='fa', size=(20,30)),  # Adjust size
)
        )

    # Create a feature group for school markers
school_group = folium.FeatureGroup(name="Schools")
for school_row in school_rows:
        name, x, y = school_row
        school_group.add_child(
            folium.Marker(
                location=[y, x],
                popup=folium.Popup(f"<b>Name:</b> {name}"),
                icon=folium.Icon(color='blue', icon='graduation-cap', prefix='fa', size=(20,30)),  # Adjust size and icon
)
        )

    # Add the feature groups to the map
m.add_child(health_group)
m.add_child(school_group)

    # Add LayerControl to the map
folium.LayerControl().add_to(m)

# Save the map to HTML file
m.save("C:/Users/chrid/anaconda3/envs/Webmap_project/pythonproject/index.html")