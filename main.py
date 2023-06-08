from bs4 import BeautifulSoup
import requests
import pandas as pd
import time

curated_info=[]
def curate_anime_cards():

    html_text=requests.get('https://myanimelist.net/anime/season')
    soup=BeautifulSoup(html_text.text,'html.parser') # instance of Beautiful Soup
    anime_cards=soup.find_all('div',class_="js-anime-category-producer seasonal-anime js-seasonal-anime js-anime-type-all js-anime-type-1")

    # list to store the scraped data 

    for card in anime_cards:
        anime_title=card.find('a',class_="link-title").text # name of the anime
        rel_date=card.find('div',class_='info').span.text   # release data
        click_to_watch_button=card.find('h2',class_='h2_anime_title').a['href'] # link for watching
        ep_nos=card.select('div.info span.item')[1].text.replace('\n','') # ep. no. and duration
        genre_one=card.find('div',class_="genres-inner js-genre-inner").text.replace('\n','') # genre
        synopsis=card.find('div',class_="synopsis js-synopsis").p.text # synopsis
        click_video=card.find('a',class_='ga-click')['href'] # link for watching the anime

        #ep_nos=card.find_all('div',class_='info').span.span.text
        #click_to_watch_button=card.header.h2.a['href']
        #eng_title=card.find_all('h3',class_="h3_anime_subtitle").text
        #genre_two=card.find('span',class_="genre")[1].a.text
        
        
        # appending all the scraped info. into list
        curated_info.append((anime_title,rel_date,genre_one,ep_nos,synopsis,click_video,click_to_watch_button))

        #printing all the scraped info.
        print(f"\n anime title: {anime_title}")
        print(f"release date : {rel_date}")
        print(f"genre: {genre_one}")

        #print(f"english title: {eng_title}")
        # genre=card.select('div span.genre').text
        # texts=[genre.text for g in genre]
        # print(texts[0:2])
        #print(f"{genre_two}")
    
        if '?' in ep_nos:
            print("looks like this anime is ongoing!you are just in time ;)")
            print(f"no of eps and duration of 1 ep: {ep_nos}")
        else:
            print(f"no of eps and duration of 1 ep: {ep_nos}")
        
        print(f"synopsis:{synopsis}")
        print(f"click to watch the anime-->{click_video}")
        print(f"here is the link to find more about the anime: {click_to_watch_button}")

    
inst=curate_anime_cards()
def convert_to_tabular_structure():
    df = pd.DataFrame(curated_info, columns=['anime title', 'release_date', 'genre', 'ep_nos.','synopsis','video_link','more_info.'])
    df['release_date'] = pd.to_datetime(df['release_date'])
    print(df.head())
    df.to_csv('top seasonal anime .csv', index=False, encoding='utf-8')


if __name__=='__main__': 
    while True:  
        curate_anime_cards()
        convert_to_tabular_structure()
        time_wait=10 # change wait time as you want
        print(f"waiting for {time_wait} minutes")
        time.sleep(time_wait*60)

    