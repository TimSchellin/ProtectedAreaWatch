import urllib.request, json


# api_token = 'api_key=szvbj9zZLao7J4flDav0lgCJoQah0MUFCZEovD58'
# url = 'https://eonet.sci.gsfc.nasa.gov/api/v2.1/events'

event_dict = {}

with urllib.request.urlopen(
        "https://eonet.sci.gsfc.nasa.gov/api/v2.1/events?api_key=szvbj9zZLao7J4flDav0lgCJoQah0MUFCZEovD58") as url:
    # loads the JSON file from NASA's API
    data = json.loads(url.read().decode())
    count = 0
    # iterate through the data object to scrape for the coordinates and event type
    for i in data['events']:
        try:
            # create a tuple as event_dict key that contains my logitude and latitude
            coord = (data['events'][count]['geometries'][0]['coordinates'][0],
                     data['events'][count]['geometries'][0]['coordinates'][1])
            event = data['events'][count]['title']
            coord = str(coord)
            # put the data inside a dictionary
            event_dict.update({coord: event})

        except IndexError:
            pass

        finally:
            count = count + 1

    # print out the dictionary
    for i in event_dict:
        item = event_dict[i]
        print(item, i)

    with open('result.json', 'w') as fp:
        json.dump(event_dict, fp)

    # print(len(event_dict))

    fp.flush()
    fp.close()

    # House keeping:
    # test if point is inside a polygon -- check
    # convert a dictionary to cvs file -- uncheck
