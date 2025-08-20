import scrapy

class DmtSpider(scrapy.Spider):
    name = "dmt"
    allowed_domains = ["erowid.org"]

    def start_requests(self):
        base_url = "https://www.erowid.org/experiences/exp.cgi?S1=18"
        yield scrapy.Request(base_url, callback=self.parse_listing)

        for start in range(100, 2600, 100):
            paginated_url = f"{base_url}&ShowViews=0&Cellar=0&Start={start}&Max=100"
            yield scrapy.Request(paginated_url, callback=self.parse_listing)

    def parse_listing(self, response):
        rows = response.xpath('//tr[td/a[contains(@href, "exp.php?ID=")]]')
        for row in rows:
            title = row.xpath('.//a[contains(@href, "exp.php?ID=")]/text()').get()
            relative_link = row.xpath('.//a[contains(@href, "exp.php?ID=")]/@href').get()
            full_url = response.urljoin(relative_link)
            substance = row.xpath('./td[3]/text()').get()

            yield scrapy.Request(
                url=full_url,
                callback=self.parse_report,
                meta={'title': title, 'report_url': full_url, 'substance': substance}
            )

    def parse_report(self, response):
        title = response.meta.get('title')
        report_url = response.meta.get('report_url')
        substance = response.meta.get('substance')

        paragraphs = response.css('div.report-text-surround ::text').getall()
        report_text = ''.join(p.strip() for p in paragraphs if p.strip())

        age = response.css('td.footdata-ageofexp::text').get()
        weight = response.css('td.bodyweight-amount::text').get()
        gender_text = response.css('td.footdata-gender::text').get()
        gender = gender_text.replace("Gender: ", "") if gender_text else None

        yield {
            'title': title,
            'report_url': report_url,
            'substance': substance,
            'report_text': report_text,
            'age': age,
            'weight': weight,
            'gender': gender
        }
