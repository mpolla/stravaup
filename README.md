# stravaup
Upload FIT, TCX and GPX files to strava.com from the command line.

## Prerequisites
* POSIX shell
* cURL
* Python 3

## Setup
1.  Sign up at http://www.strava.com/
2. Register your own Strava client at https://www.strava.com/settings/api
3. Create a .stravauprc file in your home directory:
~~~
STRAVAUP_CLIENT_ID=FIXME
STRAVAUP_CLIENT_SECRET=FIXME
~~~
4. Get your authorization code
  On the first run of the program, you will be prompted to visit a URL
  with your browser and click `Authorize`.
  The browser must be running on the same computer as the _stravaup_ script.
  Alternatively, after clicking on `Authorize`, copy the `code` parameter
  from the redirect URL into your .stravauprc:
~~~
STRAVAUP_CODE=FIXME
~~~

## Usage
Upload a single file:

    stravaup file.fit

Use find and xargs to upload everything:

    find -iname \*.fit | xargs stravaup

## More info

Strava API reference https://strava.github.io/api/
