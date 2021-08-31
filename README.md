# nichunter
ok so with this script you can plow a lot of .ir (.ir is the Internet country code top-level domain for Iran) domains and see if they are avaliable or not.
it's really handy and easy to use, just make a csv file and write the domains into it for example:
```
digikala.ir
amazon.ir
former.ir
apple.ir
....
```
NOTE: It's only working with .ir domains for now. happy me with your pull requests 😆

## How to use ?
```
usage: run.py [-h] -i  [-o]
optional arguments:
  -h, --help      show this help message and exit
  -i , --input    Input the CSV file that contains domains
  -o , --output   Output the results into a CSV file
```
- ```git clone https://github.com/fahamjv/nichunter.git && cd nichunter```
- ```cp .env.example .env```
- ```python3 run.py -i input.csv -o output.csv```
- enjoy the result!


![https://www.nic.ir/](https://user-images.githubusercontent.com/20015479/131530988-e27becf8-85bd-4652-b3aa-7f0ea0d440a8.png)\
the result (out.csv):
```domain,is_domain_available,datetime
digikala.ir,,2021-08-31 19:50:29.793493
radisa.ir,False,2021-08-31 19:50:29.972483
plusgram.ir,False,2021-08-31 19:50:30.124198
rond.ir,False,2021-08-31 19:50:30.292795
khoonegi.ir,False,2021-08-31 19:50:30.446368
setme.ir,False,2021-08-31 19:50:31.684090
loxwork.ir,False,2021-08-31 19:50:31.857444
itamozesh.ir,False,2021-08-31 19:50:32.033248
...
```

