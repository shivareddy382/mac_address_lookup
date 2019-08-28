# mac_address_lookup

Registered with the https://api.macaddress.io/v1?apiKey=at_vPxEIQqhTXID0OPufpq1KdoZkjLNL&output=json&search=44:38:39:ff:ef:57


Wrote a source code in python to output company name associated with MAC address and requirements.txt .

Wrote a Dockerfile

And run the commands to build a container

docker build -t api (just given a tag as api)

docker images

docker run -e macaddress="44:38:39:ff:ef:57" f85c87545cfd (macaddress and associated docker image id)

OUTPUT :

You entered: 44:38:39:ff:ef:57
Company Name: Cumulus Networks, Inc

Pushed to github.com with publicly accessable .
