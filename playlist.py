import scrapy
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

class SongsSpider(scrapy.Spider):
    name = 'songs'
    current_date = datetime.now();
    end_date = current_date - relativedelta(years=3)
    
    def start_requests(self):
        while self.current_date > self.end_date:
            url = 'https://www.deejay.it/programmi/il-volo-del-mattino/playlist/dettaglio/' + self.current_date.strftime("%Y-%m-%d")
            self.current_date = self.current_date - timedelta(days=1)
            yield scrapy.Request(url=url, callback=self.parse)


    def parse(self, response):
        with open('songs', 'a') as f:
            songs = response.css('section.playlist-list').css('span.song::text').getall()

            for s in songs:
                f.write(s + "\n")
