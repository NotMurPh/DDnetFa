# Info:
Basically this app will fix your Persian text on clients that do not support Persian ( Normal : ﻡﺍﻝﺱ / Fixed : سلام )
and its not limited to DDNet and it will work on any other app that has this problem and the font that can support Persian
also you can modify the app to add other Lang's as well

# How to add other langs:
So for adding other langs to the app you have to open the DDNetFa.py
and make instanse of the FarsiConverter Class like this ```python3
Z1=FarsiConverter(name='ذ',isolated='ﺫ',start='ﺫ',mid='ﺬ',end='ﺬ')```
and for the inputs of the instanse you have to open charecter map on windows pick a font that has your lang in it and add the charecters styles like so
btw you have to enter the name manually by keyboard

# Convert to exe:
I used auto-py-to-exe on pip to convert the files to exe thats a good gui of pyinstaller so that make the work ezier
and the config file of auto-py-to-exe is included so you can import it and modify it.
first you have to install auto-py-to-exe for installing that you have to open cmd type pip install auto-py-to-exe.
after install go to the app directory from cmd and type auto-py-to-exe and import the json file and change the address and stuff or do it manually.
