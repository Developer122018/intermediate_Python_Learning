from urllib.request import urlopen
import sys

url = 'www.google.com'
while url != '':
    try:
        handynames = {}
        if len(handynames) >= 1:
            yesorno = input('Do you want to use one of your names kept handy(yes or no)?').lower()
            if yesorno == 'yes':
                namewhichishandy = input('What was your name kept handy?')
                if namewhichishandy in handynames:
                    print(handynames.get(namewhichishandy,))
        urll = input('What is your url?')
        handynameofurl = input('What is your shortcut name for this?')
        website = urlopen(urll).read()
        print(website)
        if handynameofurl != '':
            handynames = [handynameofurl], website
        else:
            pass
    except Exception:
        print('**********\nUnexpected Error*******', sys.exc_info()[0])
        stoporproceed = input('Do you want to stop or proceed? Please type 1 if yes and type anything else if you want to continue.')
        if stoporproceed == 1:
            pass
        else:
            sys.exit()




    