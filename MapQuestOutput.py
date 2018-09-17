'''

MapQuest User Interaction Output

---

A module that implements the various outputs. Each kind of output that can be generated by
the program must be implemented as a separate class which contains attributes that configure
it and a method that generates the output given the response from the MapQuest Open APIs.

All of the classes must have a method with the same signature that is used to generate one
kind of output, so the main module can create a list of output generators of various types.
Then it would generate all of its outputs by simply looping through them and asking each to
generate its own output.

---

If no route is found by MapQuest, the program should output a blank line, followed by "NO ROUTE 
FOUND." error message, alone on a line, which includes the scenario where one or more of the 
locations was not valid. On the other hand, if MapQuest returns another kind of error, other than 
no route found, the program should output a blank line, followed by "MAPQUEST ERROR!" error message, 
alone on a line.

After reading the input and processing it (downloading information from MapQuest API),
your program will generate the specified outputs in the forms described below. Each output
must be preceded by a blank line, to set each one off from the others. The outputs must be
written in the order they were specified in the input:

    STEPS output should begin with the word DIRECTIONS, alone on a line, followed by one 
    line of output for each maneuver that needs to be made along the path from the first 
    location to the last.

    TOTALDISTANCE output should begin with the words TOTAL DISTANCE, followed by a colon 
    & space and the total distance (rounded integer number of miles) for the entire trip.

    TOTALTIME output should begin with the words TOTAL TIME, followed by a colon & space
    and the total time (rounded integer number of minutes) required for the entire trip.

    LATLONG output should begin with the word LATLONGS, alone on a line, followed by a
    latitude and longitude, one each per line, for each of the locations specified in the
    input. The latitude should come first, followed by a space and the longitude. 

        LATITUDES format: number of degrees with two decimal places, followed by either
        N for North or S for South.

        LONGITUDES format: number of degrees with two decimal places, followed by either
        W for West or E for East.

After the last output, print the Copy Statement, alone on a line: "Directions Courtesy of MapQuest; 
Map Data Copyright OpenStreetMap Contributors."

'''

class STEPS:
    def map_output(result: 'json'):
        print('DIRECTIONS')
        for item in result['route']['legs']:
            for x in item['maneuvers']:
                print(x['narrative'])
        print()

class TOTALDISTANCE:
    def map_output(result: 'json'):
        print('TOTAL DISTANCES: ' + str(round(result['route']['distance'])) + ' miles.')
        print()

class TOTALTIME:
    def map_output(result: 'json'):
        print('TOTAL TIME: ' + str(round(int(result['route']['time']) / 60)) + ' minutes.')
        print()

class LATLONG:
    def map_output(result: 'json'):
        print('LATLONGS')
        for item in result['route']['locations']:
            lat = item['latLng']['lat']
            if lat > 0:
                latitude = 'N '
            else:
                latitude = 'S '

            long = item['latLng']['lng']
            if long < 0:
                longitude = 'W'
            else:
                longitude = 'E'
            
            print(str("{0:.2f}".format(abs(lat))) + latitude +
                  str("{0:.2f}".format(abs(long))) + longitude)
        print()

def print_map(instructions: list, json_result: 'json'):
    '''
        Runs through output instructions list and evaluates each output in the list
    '''
    try:
        assert json_result['info']['messages'] == []
        for instruction in instructions:
            eval(instruction).map_output(json_result)

    except:
        print('NO ROUTE FOUND' + '\n')