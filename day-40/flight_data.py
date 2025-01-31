from dataclasses import dataclass


@dataclass
class FlightData:
    price: float
    origin_airport: str
    destination_airport: str
    out_date: str
    return_date: str
    stops: int

    def __init__(
        self, price, origin_airport, destination_airport, out_date, return_date, stops
    ):
        """
        Constructor for initializing a new flight data instance with specific travel details.

        Parameters:
        - price: The cost of the flight.
        - origin_airport: The IATA code for the flight's origin airport.
        - destination_airport: The IATA code for the flight's destination airport.
        - out_date: The departure date for the flight.
        - return_date: The return date for the flight.
        """
        self.price = price
        self.origin_airport = origin_airport
        self.destination_airport = destination_airport
        self.out_date = out_date
        self.return_date = return_date
        self.stops = stops


class NoDataFligthError(Exception):
    pass


def find_cheapest_flight(data) -> FlightData:
    """
    Parses flight data received from the Amadeus API to identify the cheapest flight option among
    multiple entries.

    Args:
        data (dict): The JSON data containing flight information returned by the API.

    Returns:
        FlightData: An instance of the FlightData class representing the cheapest flight found,
        or a FlightData instance where all fields are 'NA' if no valid flight data is available.

    This function initially checks if the data contains valid flight entries. If no valid data is found,
    it returns a FlightData object containing "N/A" for all fields. Otherwise, it starts by assuming the first
    flight in the list is the cheapest. It then iterates through all available flights in the data, updating
     the cheapest flight details whenever a lower-priced flight is encountered. The result is a populated
     FlightData object with the details of the most affordable flight.
    """

    # Handle empty data if no flight or Amadeus rate limit exceeded
    if data is None or not data["data"]:
        raise NoDataFligthError

    # Data from the first flight in the json
    first_flight = data["data"][0]
    lowest_price = float(first_flight["price"]["grandTotal"])
    stops = len(first_flight["itineraries"][0]["segments"]) - 1
    origin = first_flight["itineraries"][0]["segments"][0]["departure"]["iataCode"]
    destination = first_flight["itineraries"][0]["segments"][-1]["arrival"]["iataCode"]
    out_date = first_flight["itineraries"][0]["segments"][0]["departure"]["at"].split(
        "T"
    )[0]
    return_date = first_flight["itineraries"][1]["segments"][0]["departure"][
        "at"
    ].split("T")[0]

    # Initialize FlightData with the first flight for comparison
    cheapest_flight = FlightData(
        price=lowest_price,
        origin_airport=origin,
        destination_airport=destination,
        out_date=out_date,
        return_date=return_date,
        stops=stops,
    )

    for flight in data["data"]:
        price = float(flight["price"]["grandTotal"])
        if price < lowest_price:
            lowest_price = price
            stops = len(flight["itineraries"][0]["segments"]) - 1
            origin = flight["itineraries"][0]["segments"][0]["departure"]["iataCode"]
            destination = flight["itineraries"][0]["segments"][-1]["arrival"][
                "iataCode"
            ]
            out_date = flight["itineraries"][0]["segments"][0]["departure"]["at"].split(
                "T"
            )[0]
            return_date = flight["itineraries"][1]["segments"][0]["departure"][
                "at"
            ].split("T")[0]
            cheapest_flight = FlightData(
                price=lowest_price,
                origin_airport=origin,
                destination_airport=destination,
                out_date=out_date,
                return_date=return_date,
                stops=stops,
            )
            print(f"Lowest price to {destination} is £{lowest_price}")

    return cheapest_flight
