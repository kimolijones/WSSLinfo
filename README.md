# WSSLinfo

<p>This project is a simple python scraper that looks for the latest weather information for pilots operating out of WSSL - Seletar Airport, Singapore. Information includes decoded METAR and TAF, and rain areas.</p>

Dependencies
-----
The script requires the following dependencies to run on your local machine:
* [streamlit](https://streamlit.io/)
* [pandas](http://pandas.pydata.org/)
* [datetime](https://docs.python.org/3/library/datetime.html)
* [pytz](https://github.com/stub42/pytz)
* [lxml](https://lxml.de/)

These packages can be installed using [pip](https://pip.pypa.io/en/stable/) via `pip install -r requirements.txt` in the `WSSLinfo` base directory.

Run This Webapp
-----
To run on your computer via localhost, clone this repository and `cd` into it. Then run `streamlit run app.py` in the terminal. Otherwise, try out the app [here](https://kimolijones-wsslinfo-app-lb4n89.streamlit.app/).
