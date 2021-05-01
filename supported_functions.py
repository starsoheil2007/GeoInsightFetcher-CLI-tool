"""
 ==>  Supported function list:
 For adding new function, you need to add a new one in this list based on below descriptions:
 command => Main command line
 field_name => field name that get from input to send to the API
 request_url => request URL to retrieve data
 request_method => Rest-API request method (POST, GET)
 help => command's description that will showed on help command
 example => example's description that will showed on help command
 success_status_code => This is status code to show when we should search in result
 result_format(Optional) => if you want to format result data to optional dict you should define it as Dictionary
 header(Optional) => if you need add a header in Rest-API request please add this as Dictionary (Ex. API-Key)
 other_body_params(Optional) => if you need add another params in body of Rest-API request add this as Dictionary (Ex. limit)
 ============================================================================================================================
"""

functions = [
    {
        "command": "population",
        "field_name": "city",
        "request_url": "https://countriesnow.space/api/v0.1/countries/population/cities",
        "request_method": "POST",
        "success_status_code": 200,
        "result_format": {
            "country": "data.country",
            "population Counts": "data.populationCounts[0].value"
        },
        "help": "Get population and country name based on city's name",
        "example": "./geo.py population lagos"
    },
    {
        "command": "country_currency",
        "field_name": "country",
        "request_url": "https://countriesnow.space/api/v0.1/countries/currency",
        "request_method": "POST",
        "success_status_code": 200,
        "result_format": {
            "currency": "data.currency"
        },
        "help": "Get currency name based on country's name",
        "example": "./geo.py country_currency nigeria"
    },
    {
        "command": "city_of_country",
        "field_name": "country",
        "request_url": "https://countriesnow.space/api/v0.1/countries/cities",
        "request_method": "POST",
        "success_status_code": 200,
        "result_format": {
            "cities_list": "data"
        },
        "help": "Get cities of a specified country",
        "example": "./geo.py city_of_country nigeria"
    },
    {
        "command": "dial_codes",
        "field_name": "country",
        "request_url": "https://countriesnow.space/api/v0.1/countries/codes",
        "request_method": "POST",
        "success_status_code": 200,
        "help": "Get list of dial codes of country",
        "example": "./geo.py dial_codes nigeria"
    }
]
