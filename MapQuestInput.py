'''

MapQuest User Interaction Input

---

A module that reads the input and constructs the objects that will generate the program's output. 
This is the only module that should have an if __name__ == '__main__': block to make it executable,
you would execute this module. 

---

The program should not prompt the user in any way, it should simply read whatever input is
typed into the console while assuming that the user knows the precise input format:

    (1) An integer whose value is at least 2, alone on a line, that specifies how many locations
        the trip will consist of.

    (2) If there are N locations, the next N lines of input will describe a location. Each location
        can be a CITY such as Irvine, CA, an ADDRESS such as 4545 Campus Dr, Irvine, CA, or
        ANYTHING the MapQuest API will accept as a location.

    (3) A positive integer whose value is at least 1, alone on a line, that specifies how many
        outputs that need to be generated.

    (4) If there are M outputs, the next M lines of input will describe an output which can be of
        the following:

            STEPS for step-by-step directions and a brief description of each maneuver (e.g. a turn,
            entering/exiting a freeway, etc.).

            TOTALDISTANCE for the total distance traveled if completing the entire trip.

            TOTALTIME for the total estimated time to complete the entire trip.

            LATLONG for the latitude and longitude of each of the locations specified in the input.

'''

import MapQuestAPI
import MapQuestOutput

def trip_locations() -> int:
    '''
        Asks user for input of how many locations they want and returns an integer if it is greater than 1.
    '''
    try:
        number_of_locations = int(input())
        assert (number_of_locations > 1) == True
        return number_of_locations
    
    except:
        print('The number of locations must be greater than 1. Please try again.')
        return trip_locations()

def location_descriptions(n: int) -> list:
    '''
        Asks user for input of the descriptions of the desired locations and returns a list of locations.
    '''
    locations = []
    while n > 0:
        description = str(input())
        locations.append(description)
        n -= 1

    return locations

def program_outputs() -> int:
    '''
        Asks user for input of how many outputs they want and returns an integer if it is greater than 0.
    '''
    try:
        number_of_outputs = int(input())
        assert (number_of_outputs > 0) == True
        return number_of_outputs

    except:
        print('The number of outputs must be greater than 0. Please try again.')
        return program_outputs()

def output_descriptions(n: int) -> list:
    '''
        Asks user for input of what type of outputs they want and returns a list of output instructions.
    '''
    descriptions = [ 'STEPS', 'TOTALDISTANCE', 'TOTALTIME', 'LATLONG' ]

    outputs = []
    while n > 0:
        instruction = str(input())
        if instruction in descriptions:
            outputs.append(instruction)
            n -= 1
        else:
            print('Invalid output type. Please try again.')
            continue
    print()
    
    return outputs

if __name__ == '__main__':
    number_of_locations = trip_locations()
    route = location_descriptions(number_of_locations)

    number_of_outputs = program_outputs()
    instructions = output_descriptions(number_of_outputs)

    mapquest_url = MapQuestAPI.build_route_url(route)
    json_format = MapQuestAPI.http_request(mapquest_url)

    MapQuestOutput.print_map(instructions, json_format)
    print('Directions Courtesy of MapQuest; Map Data Copyright OpenStreetMap Contributors.')