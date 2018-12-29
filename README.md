# Cutup Generator

Software version of the cut-up technique used by William S. Burroughs and David Bowie

https://en.wikipedia.org/wiki/Cut-up_technique

Enter two pieces of text, and the program returns random sections of the two of random lengths.

# Desktop Version:

The standalone desktop version has a GUI made using PyQt5 and is also included as a 
Windows executable (located in /static/).

# Web App Version:

The web app version uses HTML5 and Flask for its interface. It also includes a web scraper
and is capable of recognising a URL.
When a URL is entered in place of text the program will rip the text from that URL
and use it in the cup-up process.

A working example of this code can be seen at: http://www.jimimcdonald.co.uk/cutup/

# 

The list of top level domains used in isUrl.py was found at: https://data.iana.org/TLD/tlds-alpha-by-domain.txt
