## Google Sheets 

I live in a house with some friends while attending university. I bought a 
raspberry Pi for the house and loaded OSMC onto it. Sometimes we need house 
annoucements to be seen or quotes of the day or something. I could not find an
addon which we could do this as OSMC is meant more for a media center. So I 
decided to make my own.

We have a google sheets which has annoucements or inspirational quotes we want 
to display. This addon will querry the sheet, read the data, then display it.

To use this addon requires the Sheets API from google found 
![here](https://developers.google.com/sheets/api/quickstart/python). 

You will need to supply a credentials.json file, a token.pickle file (if needed)
and a google sheets ID with range. 

