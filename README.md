# stravaup
Upload files to strava.com from the command line.

## Prerequisites
1.  Sign up at http://www.strava.com/
2. Register your own Strava client at https://www.strava.com/settings/api
3. Create a .stravauprc file in your home directory
~~~
STRAVAUP_CLIENT_ID=FIXME
STRAVAUP_CLIENT_SECRET=FIXME
~~~
4. Get your authorization code
* Go to https://www.strava.com/oauth/authorize?client_id=YOUR_STRAVAUP_CLIENT_ID&response_type=code&redirect_uri=http://localhost/index.php&approval_prompt=force&scope=write
* Select 'Authorize' wich will lead to a redirect URL
* Copy the code from the redirect URL into your .stravauprc,
~~~
STRAVAUP_CODE=FIXME
~~~

## Usage
Upload a sigle fit file

    stravaup file.fit

Use find and xargs to upload everything

    find ~ -name *.fit | xargs stravaup

## More info

Strava API reference https://strava.github.io/api/
