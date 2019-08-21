import pandas as pd
from bs4 import BeautifulSoup as bs
import requests
from splinter import Browser

def init_browser():
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)

def scrape():
    browser = init_browser()

    nasa_url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
    response = requests.get(nasa_url)
    soup1 = bs(response.text, 'html.parser')

    news_title = soup1.find('div', class_="content_title").text
    news_p = soup1.find('div', class_="rollover_description_inner").text


    jpl_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(jpl_url)
    html = browser.html
    soup = bs(html, 'html.parser')
    image = soup.find('div', class_='carousel_items')
    image_url = image.article['style']
    url = image_url.split('/s')[-1].split('.')[0]
    featured_image_url = 'https://www.jpl.nasa.gov' + '/s' + url + '.jpg'

    #  = image['src']

    # for image in images:
    # featured_image_url = 'https://www.jpl.nasa.gov'+ featured_image
    
    facts_url = 'https://space-facts.com/mars/'
    response = requests.get(facts_url)
    soup = bs(response.text, 'html.parser')
    tables = pd.read_html(facts_url)

    type(tables)
    df = tables[1]
    df.columns = ['Mars Facts','']
    mars_html = df.to_html(index=True, header=True)
    
#Mars Hemisphere Titles and Images
    hemisphere_image_urls = [
        {"title": "Valles Marineris Hemisphere" , "img_url": "http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg"},
        {"title": "Syrtis Major Hemisphere" , "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg"},
        {"title": "Schiaparelli Hemisphere" , "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg"},
        {"title": "Cerberus Hemisphere" , "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg"}
]
    mars_data = {
        "news_title": news_title,
        "news_p": news_p,
        "featured_image_url": featured_image_url,
        "mars_table": mars_html,
        "hemisphere_images": hemisphere_image_urls
    }
    browser.quit()
    return mars_data





