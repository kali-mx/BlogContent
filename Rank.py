
#!/usr/bin/python3
#How would you rank in another country, say Russsia, Germany or Antartica??
#Let's find out!!
### Author: Thomas Max Ahartz
### Title: Rankor
### Created: 10.01.22
### Credit: tryhackme.com, an amazing cybersecurity learning platform!

import requests, json, os

Countries = {
    'AF': 'Afghanistan',
    'AX': 'Aland\x20Islands',
    'AL': 'Albania',
    'DZ': 'Algeria',
    'AS': 'American\x20Samoa',
    'AD': 'Andorra',
    'AO': 'Angola',
    'AI': 'Anguilla',
    'AQ': 'Antarctica',
    'AG': 'Antigua\x20And\x20Barbuda',
    'AR': 'Argentina',
    'AM': 'Armenia',
    'AW': 'Aruba',
    'AU': 'Australia',
    'AT': 'Austria',
    'AZ': 'Azerbaijan',
    'BS': 'Bahamas',
    'BH': 'Bahrain',
    'BD': 'Bangladesh',
    'BB': 'Barbados',
    'BY': 'Belarus',
    'BE': 'Belgium',
    'BZ': 'Belize',
    'BJ': 'Benin',
    'BM': 'Bermuda',
    'BT': 'Bhutan',
    'BO': 'Bolivia',
    'BA': 'Bosnia\x20And\x20Herzegovina',
    'BW': 'Botswana',
    'BV': 'Bouvet\x20Island',
    'BR': 'Brazil',
    'BN': 'Brunei\x20Darussalam',
    'BG': 'Bulgaria',
    'BF': 'Burkina\x20Faso',
    'BI': 'Burundi',
    'KH': 'Cambodia',
    'CM': 'Cameroon',
    'CA': 'Canada',
    'CV': 'Cape\x20Verde',
    'KY': 'Cayman\x20Islands',
    'CF': 'Central\x20African\x20Republic',
    'TD': 'Chad',
    'CL': 'Chile',
    'CN': 'China',
    'CX': 'Christmas\x20Island',
    'CC': 'Cocos\x20(Keeling)\x20Islands',
    'CO': 'Colombia',
    'KM': 'Comoros',
    'CG': 'Congo',
    'CD': 'Congo,\x20Democratic\x20Republic',
    'CK': 'Cook\x20Islands',
    'CR': 'Costa\x20Rica',
    'CI': 'Cote\x20D\x27Ivoire',
    'HR': 'Croatia',
    'CU': 'Cuba',
    'CY': 'Cyprus',
    'CZ': 'Czech\x20Republic',
    'DK': 'Denmark',
    'DJ': 'Djibouti',
    'DM': 'Dominica',
    'DO': 'Dominican\x20Republic',
    'EC': 'Ecuador',
    'EG': 'Egypt',
    'SV': 'El\x20Salvador',
    'GQ': 'Equatorial\x20Guinea',
    'ER': 'Eritrea',
    'EE': 'Estonia',
    'ET': 'Ethiopia',
    'FK': 'Falkland\x20Islands\x20(Malvinas)',
    'FO': 'Faroe\x20Islands',
    'FJ': 'Fiji',
    'FI': 'Finland',
    'FR': 'France',
    'GF': 'French\x20Guiana',
    'PF': 'French\x20Polynesia',
    'TF': 'French\x20Southern\x20Territories',
    'GA': 'Gabon',
    'GM': 'Gambia',
    'GE': 'Georgia',
    'DE': 'Germany',
    'GH': 'Ghana',
    'GI': 'Gibraltar',
    'GR': 'Greece',
    'GL': 'Greenland',
    'GD': 'Grenada',
    'GP': 'Guadeloupe',
    'GU': 'Guam',
    'GT': 'Guatemala',
    'GG': 'Guernsey',
    'GN': 'Guinea',
    'GW': 'Guinea-Bissau',
    'GY': 'Guyana',
    'HT': 'Haiti',
    'VA': 'Holy\x20See\x20(Vatican\x20City\x20State)',
    'HN': 'Honduras',
    'HK': 'Hong\x20Kong',
    'HU': 'Hungary',
    'IS': 'Iceland',
    'IN': 'India',
    'ID': 'Indonesia',
    'IR': 'Iran,\x20Islamic\x20Republic\x20Of',
    'IQ': 'Iraq',
    'IE': 'Ireland',
    'IM': 'Isle\x20Of\x20Man',
    'IL': 'Israel',
    'IT': 'Italy',
    'JM': 'Jamaica',
    'JP': 'Japan',
    'JE': 'Jersey',
    'JO': 'Jordan',
    'KZ': 'Kazakhstan',
    'KE': 'Kenya',
    'KI': 'Kiribati',
    'KR': 'Korea',
    'KW': 'Kuwait',
    'KG': 'Kyrgyzstan',
    'LA': 'Lao\x20People\x27s\x20Democratic\x20Republic',
    'LV': 'Latvia',
    'LB': 'Lebanon',
    'LS': 'Lesotho',
    'LR': 'Liberia',
    'LY': 'Libyan\x20Arab\x20Jamahiriya',
    'LI': 'Liechtenstein',
    'LT': 'Lithuania',
    'LU': 'Luxembourg',
    'MO': 'Macao',
    'MK': 'Macedonia',
    'MG': 'Madagascar',
    'MW': 'Malawi',
    'MY': 'Malaysia',
    'MV': 'Maldives',
    'ML': 'Mali',
    'MT': 'Malta',
    'MH': 'Marshall\x20Islands',
    'MQ': 'Martinique',
    'MR': 'Mauritania',
    'MU': 'Mauritius',
    'YT': 'Mayotte',
    'MX': 'Mexico',
    'FM': 'Micronesia,\x20Federated\x20States\x20Of',
    'MD': 'Moldova',
    'MC': 'Monaco',
    'MN': 'Mongolia',
    'ME': 'Montenegro',
    'MS': 'Montserrat',
    'MA': 'Morocco',
    'MZ': 'Mozambique',
    'MM': 'Myanmar',
    'NA': 'Namibia',
    'NR': 'Nauru',
    'NP': 'Nepal',
    'NL': 'Netherlands',
    'NC': 'New\x20Caledonia',
    'NZ': 'New\x20Zealand',
    'NI': 'Nicaragua',
    'NE': 'Niger',
    'NG': 'Nigeria',
    'NU': 'Niue',
    'NF': 'Norfolk\x20Island',
    'MP': 'Northern\x20Mariana\x20Islands',
    'NO': 'Norway',
    'OM': 'Oman',
    'PK': 'Pakistan',
    'PS': 'Palestinian\x20Territory,\x20Occupied',
    'PA': 'Panama',
    'PG': 'Papua\x20New\x20Guinea',
    'PY': 'Paraguay',
    'PE': 'Peru',
    'PH': 'Philippines',
    'PN': 'Pitcairn',
    'PL': 'Poland',
    'PT': 'Portugal',
    'PR': 'Puerto\x20Rico',
    'QA': 'Qatar',
    'RE': 'Reunion',
    'RO': 'Romania',
    'RU': 'Russian\x20Federation',
    'RW': 'Rwanda',
    'BL': 'Saint\x20Barthelemy',
    'SH': 'Saint\x20Helena',
    'KN': 'Saint\x20Kitts\x20And\x20Nevis',
    ##'LC': 'Saint\x20Lucia',
    ##'MF': 'Saint\x20Martin',
    'PM': 'Saint\x20Pierre\x20And\x20Miquelon',
    'VC': 'Saint\x20Vincent\x20And\x20Grenadines',
    'WS': 'Samoa',
    'SM': 'San\x20Marino',
    'ST': 'Sao\x20Tome\x20And\x20Principe',
    'SA': 'Saudi\x20Arabia',
    'SN': 'Senegal',
    'RS': 'Serbia',
    'SC': 'Seychelles',
    'SL': 'Sierra\x20Leone',
    'SG': 'Singapore',
    'SK': 'Slovakia',
    'SI': 'Slovenia',
    'SB': 'Solomon\x20Islands',
    'SO': 'Somalia',
    'ZA': 'South\x20Africa',
    'GS': 'South\x20Georgia\x20And\x20Sandwich\x20Isl.',
    'ES': 'Spain',
    'LK': 'Sri\x20Lanka',
    'SD': 'Sudan',
    'SR': 'Suriname',
    'SJ': 'Svalbard\x20And\x20Jan\x20Mayen',
    'SZ': 'Swaziland',
    'SE': 'Sweden',
    'CH': 'Switzerland',
    'SY': 'Syrian\x20Arab\x20Republic',
    'TW': 'Taiwan',
    'TJ': 'Tajikistan',
    'TZ': 'Tanzania',
    'TH': 'Thailand',
    'TL': 'Timor-Leste',
    'TG': 'Togo',
    'TK': 'Tokelau',
    'TO': 'Tonga',
    'TT': 'Trinidad\x20And\x20Tobago',
    'TN': 'Tunisia',
    'TR': 'Turkey',
    'TM': 'Turkmenistan',
    'TC': 'Turks\x20And\x20Caicos\x20Islands',
    'TV': 'Tuvalu',
    'UG': 'Uganda',
    'UA': 'Ukraine',
    'AE': 'United\x20Arab\x20Emirates',
    'GB': 'United\x20Kingdom',
    'US': 'United\x20States',
    'UM': 'United\x20States\x20Outlying\x20Islands',
    'UY': 'Uruguay',
    'UZ': 'Uzbekistan',
    'VU': 'Vanuatu',
    'VE': 'Venezuela',
    'VN': 'Vietnam',
    'VG': 'Virgin\x20Islands,\x20British',
    'VI': 'Virgin\x20Islands,\x20U.S.',
    'WF': 'Wallis\x20And\x20Futuna',
    'EH': 'Western\x20Sahara',
    'YE': 'Yemen',
    'ZM': 'Zambia',
    'ZW': 'Zimbabwe'}

os.system('clear')
import pyfiglet
banner= pyfiglet.figlet_format("Rankor")
print(banner)
num_of_countries = (len(Countries))

MYpoints = int(input('How many points do you have? '))

while True:
    country = input('What country would you like to compare ranks? Enter country code: ')
    if country.upper() in Countries:
        print('Coming right up!\n')
        break 
    else:
        print(f'{country} code not found. Typo?')   
i=0
url = 'https://tryhackme.com/api/leaderboards?country=' + country.lower()
#print(url)
r = requests.get(url)
myJson = r.json() 
rank_list = []
try:
    while True:
        points = myJson['ranks'][i]['points']
        rank_list.append(points)
        print(i+1,points)
        i+=1
except IndexError:
    print('',end='')

sorry= False
rank_index=i=0
list_length = len(rank_list)
while i < list_length:
        if MYpoints < rank_list[list_length-1]:
            print('\n','Sorry, you are not in the Top 50 in ', country.upper())
            sorry = True;break
        elif MYpoints < rank_list[i]:
            rank_index +=1
        i+=1

if MYpoints > rank_list[0]:
    print('\n','You would be ranked #1 in', Countries[country.upper()].upper())           
elif sorry == False:
    print('\n','You would be ranked', rank_index+1, 'in', Countries[country.upper()])       


newdict = {}
for code,ctry in Countries.items():  #key,value: example us,UNITED STATES
    i=0
    url = 'https://tryhackme.com/api/leaderboards?country=' + code.lower()
    #print(url)
    r = requests.get(url)
    myJson = r.json() 
    rank_list = []
    try:
        while True: #loop trys to creates a Top50 list by country
            points = myJson['ranks'][i]['points']
            rank_list.append(points)
            #print(i+1,points)
            i+=1
    except IndexError:
        print('')

    sorry = False
    rank_index = j = 0
    list_length = len(rank_list)
    while j < list_length:
        if MYpoints < rank_list[list_length-1]:
            #print('\n','Sorry, you are not in the Top', list_length, ' in ', ctry.upper())
            sorry = True;break
        elif MYpoints < rank_list[j]:
            rank_index +=1 #count how many I beat
        j+=1

    if MYpoints > rank_list[0]:
        #print(MYpoints,rank_list[0])
        print('\n','You would be ranked #1 in', ctry.upper())   
        newdict[ctry] = 1
        print(newdict)
    elif sorry == False:
        print('\n','You would be ranked', rank_index+1, 'in', ctry.upper()) 
        newdict[ctry] = rank_index+1

print('\n'+'*'*45+'\n')        
# pp = pprint.PrettyPrinter(depth=4)
# pp.pprint(newdict)
print("Country                        Your Ranking",'\n')
for c in newdict:
    #print("{ctry}: {rank}".format(ctry=c, rank=newdict[c]))
    print("{ctry:<35s} {rank}".format(ctry=c, rank=newdict[c]))
c=0
for rank in newdict:
    if newdict[rank] ==1:
        c+=1
print('\n'+'*'*45+'\n')       
print(f'{MYpoints} points makes you #1 in {c} countries out of {num_of_countries} tracked by THM.')
print(f"That's {c/num_of_countries*100:.1f}% worldwide.\n")
print(f"Put another way- you're #1 in {c/num_of_countries*100:.1f}% of all countries on the planet!")
print("Wherever you're ranked don't get too comfy! The competition never sleeps!\nWe can always improve!! Not quite happy where you're at?  Get after it!!\n\n")
