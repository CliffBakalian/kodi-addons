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

If you have an issue running for the first time, (ie, asks you to go to a google
site to authenicate the user), this is probably because you need to create a 
token so you dont need to keep loggining in and the Pi is considered 
trustworthy. This data is saved in a`token.pickle` file. I was able to just copy
the link given and do it on my local computer. I had to make sure that the 
version of python/pip/pickle was the same on my local computer as the Pi, but 
then I could just `scp` the token.pickle file and place it where I needed to.
