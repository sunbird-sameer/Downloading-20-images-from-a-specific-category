import mechanicalsoup
import os
import wget

browser = mechanicalsoup.StatefulBrowser()
url = "https://www.google.com/imghp?hl=en"
browser.open(url)


while True:
    browser.select_form()

    search_term = input("Enter The Image You Want To Download: ")
    browser["q"] = search_term
    response = browser.submit_selected()

    new_url = browser.get_url()
    browser.open(new_url)

    page = browser.get_current_page()
    all_images = page.find_all('img')

    image_source = []
    for image in all_images:
        image = image.get('src')
        image_source.append(image)



    image_source = [image for image in image_source if image.startswith('http')]

    path_t = os.getcwd() + "/basedata/train"
    path_v = os.getcwd() + "/basedata/validation"
    path_ts = os.getcwd() + "/basedata/test"




    path_t = os.path.join(path_t, search_term)

    os.mkdir(path_t)

    counter = 0
    for image in image_source:
        save_as = os.path.join(path_t, search_term + str(counter) + '.png')
        wget.download(image, save_as)
        counter += 1

#-------------------------------------------------------------------------------------------------------------------------------


    path_v = os.path.join(path_v, search_term)

    os.mkdir(path_v)

    #counter = 0
    #for image in image_source:
    #   save_as = os.path.join(path_v, search_term + str(counter) + '.png')
    #   wget.download(image, save_as)
    #   counter += 1

#_________________________________________________________________________________________________________________________________
    path_ts = os.path.join(path_ts, search_term)
    os.mkdir(path_ts)


