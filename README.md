# harvardartmuseums_pkg

A package for getting datasets from the Harvard Art Museums API.

## Installation

```bash
$ pip install harvardartmuseums_pkg
```

## Usage

`harvardartmuseums_pkg` is to get datasets from the Harvard Art Museums API. In order to use this package and get datasets, you first need to create your api key at their official website: https://harvardartmuseums.org/collections/api


There are 3 different functions that will let you create 3 types of datasets of items in the Harvard Art Museums collections.
( Examples of the usage of functions can be found `Vignette_for_package_functions.ipynb` )

1. `get_title_classification(url)` : Get a dataset of all titles with a word you choose and its classification

2. `get_artist(url)` : Get a dataset of all female or male artists who are from a country(culture) you choose

3. `get_exhibitions(url)` : Get a dataset of all exhibitions that were held in the selected period


Each function requires a URL or a HTTPResponse. 
The following functions will make the URLs/HTTPResponse for you with the parameters you choose!

1. `get_url_for_title(text, apikey)` : Get a url for get_title_classification()

    - text: str
        A string of a word that you wish to find in the titles of artwork
    - apikey: str
        A string of your apikey, given by Harvard Art Museums
      
      
2. `get_url_for_artist(country, gender, apikey)` : Get a url for get_artist()

    - country: str
        A string of a culture name that you wish to find in artists
    - gender: str
        A string of gender (female/male) that you wish to find in artists
    - apikey: str
        A string of your apikey, given by Harvard Art Museums
    
        
3. `get_url_for_exhibition(after, before, apikey)` : Get a url for get_exhibitions()

    - after: str
        A string of a starting year of a period when exhibitions were held
    - before: str
        A string of an ending year of a period when exhibitions were held
    - apikey: str
        A string of your apikey, given by Harvard Art Museums


## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`harvardartmuseums_pkg` was created by Hyunyoung Shin. It is licensed under the terms of the MIT license.

## Credits

`harvardartmuseums_pkg` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
