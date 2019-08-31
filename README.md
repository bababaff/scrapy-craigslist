# Scrapy Craigslist
This is a Scrapy project to scrape jobs from http://losangeles.craigslist.org.

## Extracted data

This project extracts quotes, combined with the respective author names and tags.
The extracted data looks like this sample:
    
    [
        {
          "date": "2019-08-29 17:38", 
          "title": "Architectural; Draftsperson", 
          "link": "https://losangeles.craigslist.org/lac/egr/d/los-angeles-architectural-draftsperson/6967597993.html", 
          "compensation": "Compensation based upon experience and abilities", 
          "employment_type": "full-time", 
          "images": [
              'https://images.craigslist.org/00909_3HfJpygSmf9_600x450.jpg',
              'https://images.craigslist.org/00Y0Y_7FbOIsehvH2_600x450.jpg'
          ], 
          "description": "Studio AR&D Architects is seeking a........."
        }
     ]


## Spiders

This project contains a spider and you can list them using the `list`
command:

    $ scrapy list
    jobs

## Running the spiders

You can run a spider using the `scrapy crawl` command, such as:

    $ scrapy crawl jobs

If you want to save the scraped data to a file, you can pass the `-o` option:
    
    $ scrapy crawl jobs -o jobs.json
