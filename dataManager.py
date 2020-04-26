def get_awards():
    awards = []
    with open('content_awards.txt') as f:
        lines = f.readlines()
        for line in lines:
            year, title = line.split(':')
            entry = {}
            entry["year"] = year
            entry["title"] = title
            awards.append(entry)
    return awards

def get_title():
    return "Rahul Dravid"

def get_subtitle():
    return "International Cricketer"

def get_image():
    image = {}
    image["url"] = "https://farm3.staticflickr.com/2068/2142956448_26a4a4bbdd_o.jpg"
    image["caption"] = "Batting against Australia at the MCG"
    return image

def get_read_more():
    return "https://en.wikipedia.org/wiki/List_of_awards_and_achievements_of_Rahul_Dravid"