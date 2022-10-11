from bs4 import BeautifulSoup
import requests

url = "https://www.zillow.com/san-francisco-ca/rentals/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22San%20Francisco%2C%20CA%22%2C%22mapBounds%22%3A%7B%22west%22%3A-122.61529005957031%2C%22east%22%3A-122.25136794042969%2C%22south%22%3A37.645372745296726%2C%22north%22%3A37.904982256934254%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A20330%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22min%22%3A0%2C%22max%22%3A925043%7D%2C%22mp%22%3A%7B%22min%22%3A0%2C%22max%22%3A3000%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A11%7D"

headers = {
    "user-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36',
    "accept-language": 'en-US,en;q=0.9'
}
response = requests.get(url, headers=headers)


class GetData:
    def __init__(self):
        self.soup = BeautifulSoup(response.text, "html.parser")

    def find_price(self):
        """
        Find the prices of all houses
        :return: list of prices of all houses
        """
        raw_house_prices = self.soup.find_all(class_="list-card-price")
        house_prices = [(str(price.getText())) for price in raw_house_prices]
        for i in range(len(house_prices)):
            if house_prices[i].find("/mo") != -1:
                house_prices[i] = house_prices[i].replace("/mo", "")
            elif house_prices[i].find("+") != -1:
                house_prices[i] = house_prices[i].split("+")[0]
            # elif house_prices[i].find("est") != -1:
            #     house_prices[i] = house_prices[i].split(" ")[0]
        return house_prices

    def find_addresses(self):
        """
        Find the addresses of all houses
        :return: list of addresses of all houses
        """
        raw_house_addresses = self.soup.find_all(class_="list-card-addr")
        house_addresses = [address.getText() for address in raw_house_addresses]
        return house_addresses

    def find_link(self):
        """
        Find the links of all houses
        :return: list of links of all houses
        """
        raw_house_links = self.soup.findAll(name="a", class_="list-card-link")
        house_links = [link.get("href") for link in raw_house_links]
        for index in range(len(house_links)):
            if not house_links[index].startswith("http"):
                house_links[index] = 'https://www.zillow.com' + house_links[index]
        return house_links

if __name__ == '__main__':
    house_finder = GetData()
    prices = house_finder.find_price()
    # print(house_finder.find_link.__doc__)
    print(prices)
    addresses = house_finder.find_addresses()
    print(addresses)
    links = house_finder.find_link()
    print(links)
