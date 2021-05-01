# GeoInsightFetcher CLI tool.

This CLI tools is for retrieve some data about cities and countries.

## Getting Started

You need to install python 3.5 or upper and install virtualenv on your os.

### Installing

Please follow this steps to run the project:

After pull this project from GIT go to project folder

1- Create virtualenv

```
virtualenv myenv
```

2- Active virtualenv

```
source myenv/bin/activate
```

3- Install requirements

```
pip install -r requirements.txt
```

That is!

You can use it now

### How to use

All commands that will send to geo.py file

For example please type this:

```
python geo.py -h
```

You will receive a help about CLI functions

Please read [task_examples](task_examples.md) for find out more about function's examples.

## Developers guide

For adding new function to this CLI you should just add functions in supported_functions.py based on below descriptions:

* command => Main command line

* field_name => field name that get from input to send to the API

* request_url => request URL to retrieve data

* request_method => Rest-API request method (POST, GET)

* help => command's description that will showed on help command

* example => example's description that will showed on help command

* success_status_code => This is status code to show when we should search in result

* result_format(Optional) => if you want to format result data to optional dict you should define it as Dictionary

* header(Optional) => if you need add a header in Rest-API request please add this as Dictionary (Ex. API-Key)

* other_body_params(Optional) => if you need add another params in body of Rest-API request add this as Dictionary (Ex.
  limit)

## Authors

* **Soheil Tayyeb Naeini** - *Initial work* - [StarSoheil2007](https://github.com/starsoheil2007)

## License

This project is licensed under the Free License.

## Acknowledgments

* We are
  using [countriesnow.space](https://documenter.getpostman.com/view/1134062/T1LJjU52#c47920fa-af20-4444-b567-efc4f1f46498)
  API for get data

