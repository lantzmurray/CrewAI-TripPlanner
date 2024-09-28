from crew import SurpriseTravelCrew


def run_crew():
    inputs = {
        'origin': 'Pittsburgh, PIT',
        'destination': 'Ocean City, MDE',
        'age': 36,
        'adults': 4,
        'children': 1,
        'infants': 0,
        'hotel_location': 'Ocean City',
        'flight_information': 'PIT to MDE, leaving 10:00AM July 10th, 2025 - coming back 10:00PM July 15th, 2025',
        'trip_duration': '5 days',
        'special_requests': 'Two listed as adults, but are actually 15 year olds.'
    }

    result = SurpriseTravelCrew().crew().kickoff(inputs=inputs)
    print(result)

run_crew()
    
