# zattoo-channel-url-finder
`zattoo-channel-url-finder` is a tool to extract the URL of a TV channel from the [Zattoo](https://zattoo.com/), only by giving a name that resembles the name of the TV channel. It uses the python library [fuzzywuzzy](https://github.com/seatgeek/fuzzywuzzy) to achieve the fuzzy string matching.

## Installation
To install `zattoo-channel-url-finder` you can download the latest release and run
```
pip install zattoo-channel-url-finder-x.y.z.tar.gz
```

## Usage
Let's say we want to get the URL of the TV channel ARTE. We use `zattoo-channel-url-finder` with
```
zattoo-channel-url-finder arte
```
and get
```
https://zattoo.com/watch/DE_arte
```
as the result.


## Generation of the channel list
I have used the following procedure to construct the list of the channel key words `CHANNEL_LIST` in `channel_finder.py`:

First login in the browser and save the JSON containing the channel information as `channels.json`. Then run a beautifier program over this file und use the following:
```
cat channels.json | grep display | cut -d: -f2 | sed s/,//g > 1.txt
cat channels.json | grep cid | cut -d: -f2 | sed s/,//g > 2.txt
cat channels.json | grep "title" | grep '^[[:space:]]\{6\}"' | cut -d: -f2 | sed s/,//g | sed s/HD//g | sed s/" "\"/\"/g > 3.txt
paste 1.txt 2.txt 3.txt -d, | sed 's/^/[/' | sed 's/$/],/'
```
The result of this procedure can be used to generate the list `CHANNEL_LIST`. Feel free to fork this project and adopt it to your own purposes.
