import streamlit as st  
import requests  

#  App Title
st.title("🌍 Country Information Cards")

#  User Input (Country Name)
country_name = st.text_input("Enter a country name:", "Pakistan")  

#  Fetch Country Info Function
def get_country_info(country):
    url = f"https://restcountries.com/v3.1/name/{country}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()[0]  # First result
        return {
            "Name": data.get("name", {}).get("common", "N/A"),
            "Capital": data.get("capital", ["N/A"])[0],
            "Population": f"{data.get('population', 'N/A'):,}",
            "Area (km²)": f"{data.get('area', 'N/A'):,}",
            "Currency": ", ".join(data.get("currencies", {}).keys()) if data.get("currencies") else "N/A",
            "Region": data.get("region", "N/A"),
            "Flag": data.get("flags", {}).get("png", "")
        }
    return None

#  Display Country Info
if st.button("Show Country Info"):
    info = get_country_info(country_name)
    
    if info:
        #  Display Details in a Card Format
        st.subheader(f"🔍 {info['Name']} Information")
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.write(f"**Capital:** {info['Capital']}")
            st.write(f"**Population:** {info['Population']}")
            st.write(f"**Area:** {info['Area (km²)']} km²")
            st.write(f"**Currency:** {info['Currency']}")
            st.write(f"**Region:** {info['Region']}")
        
        with col2:
            if info["Flag"]:
                st.image(info["Flag"], width=120)
    else:
        st.error("🚨 Country not found! Please check the spelling.")


