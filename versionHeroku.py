import requests
from bs4 import BeautifulSoup

def main():
    url = "https://udn.com/news/breaknews/1/99#breaknews"

    #analyze the web through BeautifulSoup
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    #print(soup.prettify())  #輸出排版後的HTML內容

    new = soup.find("div", class_="story-list__text").stripped_strings  #getText() #.select("h2")

    # trim the data
    data = list(new)
    data.pop(2)
    content = ""
    for item in data:
        content = content+item+"\n"
    #print(content)
   
    msg = "聯合報更新囉，請到以下網站確認" + url + "\n更新內容為:\n"+str(content)
    result = lineNotify(msg)
    return 0

#send message to line
def lineNotify(message):
    headers = {
        "Authorization": "Bearer " + "5uwsDX23OhoYOAMWQk5DpvpF4R8odBjW6b82q5xj2Qs",   #你的權杖(token)
        "Content-Type": "application/x-www-form-urlencoded"
    }
 
    params = {"message": message}
 
    r = requests.post("https://notify-api.line.me/api/notify",
                      headers=headers, params=params)
    
    return r.status_code  #200 when success


if __name__ == '__main__':
    main()
