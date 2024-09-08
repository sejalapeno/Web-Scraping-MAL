import streamlit as st
import requests
from bs4 import BeautifulSoup
import pandas as pd

curated_info = []

def curate_anime_cards():
    try:
        response = requests.get('https://myanimelist.net/anime/season')
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching data: {e}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')
    anime_cards = soup.find_all('div', class_="js-anime-category-producer seasonal-anime js-seasonal-anime js-anime-type-all js-anime-type-1")

    for card in anime_cards[:10]:  # Limit to top 10 anime
        try:
            anime_title = card.find('a', class_="link-title").text.strip()
            rel_date = card.find('div', class_='info').span.text.strip()
            click_to_watch_button = card.find('h2', class_='h2_anime_title').a['href']
            ep_nos = card.select('div.info span.item')[1].text.strip().replace('\n', '')
            genre_one = card.find('div', class_="genres-inner js-genre-inner").text.strip().replace('\n', '')
            synopsis = card.find('div', class_="synopsis js-synopsis").p.text.strip()
            click_video = card.find('a', class_='ga-click')['href']

            # Fetch image URL
            image_tag = card.find('img', class_='lazyload')
            image_url = None  # Default to None if no image is found
            if image_tag:
                if 'data-src' in image_tag.attrs:
                    image_url = image_tag['data-src']
                elif 'src' in image_tag.attrs:
                    image_url = image_tag['src']

            curated_info.append((anime_title, rel_date, genre_one, ep_nos, synopsis, click_video, click_to_watch_button, image_url))

        except AttributeError as e:
            st.warning(f"Missing data for a card: {e}")
            continue

def convert_to_dataframe():
    if not curated_info:
        st.error("No data to convert.")
        return pd.DataFrame()

    df = pd.DataFrame(curated_info, columns=['Anime Title', 'Release Date', 'Genre', 'Episodes', 'Synopsis', 'Video Link', 'More Info', 'Image URL'])
    df['Release Date'] = pd.to_datetime(df['Release Date'], errors='coerce')
    return df

# Streamlit UI
st.title("Top 10 Seasonal Anime")

# Button to scrape anime data
if st.button('Fetch Top 10 Anime'):
    curated_info.clear()  # Clear old data
    curate_anime_cards()
    df = convert_to_dataframe()

    if not df.empty:
        st.write("Top 10 Anime This Season")
        
        # Display each anime with details and image
        for i, row in df.iterrows():
            st.subheader(row['Anime Title'])
            if row['Image URL']:
                st.image(row['Image URL'], caption=row['Anime Title'], use_column_width=True)
            else:
                st.write("No image available")
            st.write(f"Release Date: {row['Release Date']}")
            st.write(f"Genre: {row['Genre']}")
            st.write(f"Episodes: {row['Episodes']}")
            st.write(f"Synopsis: {row['Synopsis']}")
            st.markdown(f"[Watch Here]({row['Video Link']})")
            st.markdown(f"[More Info]({row['More Info']})")
else:
    st.write("Click the button to fetch the top 10 anime.")
