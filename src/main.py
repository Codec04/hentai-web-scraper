# Hentai web scraper
# github.com/Codec04

import os

try:
    import hentai
    import requests

except ModuleNotFoundError as exception:
    hentai = None
    requests = None
    print("module not installed")
    print(f"{exception}")
    input()
    quit()

subreddits = ["hentai", "Nekomimi", "Sukebei"]


def reddit_scraper():
    print("started reddit scraper")
    try:
        os.mkdir("hentai/reddit")
        print("hentai/reddit directory created")

    except FileExistsError:
        print("hentai/reddit directory already exists, data inside it will most likely get overwritten")

    for subreddit in subreddits:
        json_data = requests.get(f"https://www.reddit.com/r/{subreddit}/top.json?limit=69&t=month", headers={"User-agent": ""}).json()

        try:
            for image in range(0, 69):
                image_url = json_data["data"]["children"][image]["data"]["url"]

                try:
                    os.mkdir(f"hentai/reddit/r_{subreddit}")

                except FileExistsError:
                    pass

                if ".jpg" in image_url:
                    print(f"image url found: {image_url}")

                    image_data = requests.get(image_url)
                    open(f"hentai/reddit/r_{subreddit}/image_{str(image)}.jpg", "wb").write(image_data.content)

                elif ".jpeg" in image_url:
                    print(f"image url found: {image_url}")

                    image_data = requests.get(image_url)
                    open(f"hentai/reddit/r_{subreddit}/image_{str(image)}.jpeg", "wb").write(image_data.content)

                elif ".png" in image_url:
                    print(f"image url found: {image_url}")

                    image_data = requests.get(image_url)
                    open(f"hentai/reddit/r_{subreddit}/image_{str(image)}.png", "wb").write(image_data.content)

                elif ".gif" in image_url:
                    print(f"image url found: {image_url}")

                    image_data = requests.get(image_url)
                    open(f"hentai/reddit/r_{subreddit}/image_{str(image)}.gif", "wb").write(image_data.content)

                else:
                    continue

        except IndexError:
            continue

    print("finished scraping subreddits")


def nhentai_scraper():
    print("started nhentai scraper")
    try:
        os.mkdir("hentai/nhentai")
        print("hentai/nhentai directory created")

    except FileExistsError:
        print("hentai/nhentai directory already exists, data inside it will most likely get overwritten")

    for _hentai in hentai.Utils.get_homepage().popular_now:
        for image_url in _hentai.image_urls:
            print(f"image url found: {image_url}")

            try:
                os.mkdir(os.path.join("hentai/nhentai", image_url.split("/")[4]))

            except FileExistsError:
                pass

            image_data = requests.get(image_url)
            open(f"hentai/nhentai/{os.path.join(image_url.split('/')[4], image_url.split('/')[5])}", "wb").write(image_data.content)

    print("finished scraping nhentai")


if __name__ == "__main__":
    print("script started")
    try:
        os.mkdir("hentai")
        print("hentai directory created")

    except FileExistsError:
        pass

    try:
        reddit_scraper()
        nhentai_scraper()

    except KeyboardInterrupt:
        print("script terminated")
        input()
        quit()

    print("script completed")
    input()
