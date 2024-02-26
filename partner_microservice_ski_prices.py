# Author: Howard Whang
# OSU Email Address: whangho@oregonstate.edu
# Assignment Name: Assignment 9
# Due Date: Feb 26, 2024
# Description: Developing a microservice for our course partner. This microservice uses text files as a pipeline to
#   communicate. It will read the text file for a particular ski resort, and return the season pass pricing for that
#   resort. If the resort is not found, it will return an error message to the text file.

# NOTE: All data from https://www.onthesnow.com/united-states/lift-tickets, accessed Feb 21, 2024. The name of
# the resorts are spelled exactly as from this website. Be cautious with variations, such as "Mount" vs "Mt."
# or "and" vs "&".

# NOTE: All items in the dictionary are entered in lower case only. A string with a mix of upper case and
# lower case input is turned into lower case only by using the "casefold()" function prior to searching
# the dictionary.

import time

ski_resort_dictionary = {
    "49 degrees north": 659.00,
    "afton alps": 949.00,
    "alpental": 799.00,
    "alpine valley": 949.00,
    "alpine valley resort": 677.00,
    "alpine valley ski area": 742.00,
    "alta ski area": 1399.00,
    "alyeska resort": 1499.00,
    "andes tower hills ski area": 900.00,
    "angel fire resort": 900.00,

    "anthony lakes mountain resort": 525.00,
    "appalachian ski mountain": 595.00,
    "arapahoe basin ski area": "No Season Pass Pricing Data",
    "arizona snowbowl": 1149.00,
    "aspen snowmass": 3314.00,
    "attitash": 949.00,
    "bear creek mountain resort": 479.00,
    "bear mountain": "No Season Pass Pricing Data",
    "bear valley": 649.00,
    "beaver creek": 949.00,

    "beaver mountain": 800.00,
    "beech mountain resort": 590.00,
    "belleayre": 789.00,
    "berkshire east": 699.00,
    "big boulder": 949.00,
    "big powderhorn mountain": 549.00,
    "big sky": 2550.00,
    "big squaw mountain ski resort": 520.00,
    "bittersweet ski area": 825.00,
    "black mountain": "No Season Pass Pricing Data",

    "blacktail mountain ski area": 500.00,
    "blue hills ski area": 469.00,
    "blue knob": 699.00,
    "blue mountain resort": 777.00,
    "bluewood": 699.00,
    "bogus basin": 549.00,
    "bolton valley": 809.00,
    "boreal mountain resort": 549.00,
    "boston mills": 949.00,
    "bousquet ski area": 579.00,

    "boyne mountain resort": 969.00,
    "bradford ski area": 370.00,
    "brandywine": 949.00,
    "brantling ski slopes": 385.00,
    "breckenridge": 949.00,
    "brian head resort": 1149.00,
    "bridger bowl": 1075.00,
    "brighton resort": 1149.00,
    "bristol mountain": 995.00,
    "bromley mountain": 899.00,

    "bruce mound": 228.00,
    "brundage mountain resort": 999.00,
    "bryce resort": 350.00,
    "buck hill": 495.00,
    "buena vista ski area": 375.00,
    "buffalo ski club ski area": "No Season Pass Pricing Data",
    "burke mountain": 1029.00,
    "caberfae peaks": 329.00,
    "camden snow bowl": 550.00,
    "camelback mountain resort": 679.00,

    "campgaw mountain": 399.00,
    "canaan valley resort": 525.00,
    "cannon mountain": 899.00,
    "cannonsburg": 359.00,
    "cascade mountain": 679.00,
    "cataloochee ski area": 790.00,
    "catamount": 699.00,
    "chestnut mountain resort": 459.00,
    "christie mountain": 435.00,
    "christmas mountain": 275.00,

    "coffee mill ski & snowboard resort": 435.00,
    "cooper": 579.00,
    "cooper spur": 259.00,
    "copper mountain": 849.00,
    "cranmore mountain resort": 1389.00,
    "crested butte mountain resort": 949.00,
    "crotched mountain": 949.00,
    "crystal mountain": 1699.00,
    "crystal mountain, mi": 629.00,
    "dartmouth skiway": 599.00,

    "deer valley resort": 2890.00,
    "devils head": 499.00,
    "diamond peak": 509.00,
    "discovery ski area": 645.00,
    "dodge ridge": 849.00,
    "donner ski ranch": 549.00,
    "dry hill ski area": 360.00,
    "eagle point": 599.00,
    "eagle rock": 599.00,
    "eaglecrest ski area": 870.00,

    "eldora mountain resort": 819.00,
    "elk mountain ski resort": 1050.00,
    "elko snobowl": 1149.00,
    "elm creek winter recreation area": 249.00,
    "enchanted forest ski area": 295.00,
    "four lakes": 350.00,
    "giants ridge resort": 499.00,
    "gore mountain": 1019.00,
    "grand geneva": 575.00,
    "grand targhee resort": 1519.00,

    "granite peak ski area": 900.00,
    "great divide": 500.00,
    "greek peak": 955.00,
    "gunstock": 899.00,
    "hatley point": 750.00,
    "heavenly": 599.00,
    "hidden valley ski area": 949.00,
    "hilltop ski area": 610.00,
    "hogadon basin": 525.00,
    "holiday mountain": 520.00,

    "holiday valley": 1191.00,
    "holimont ski area": 340.00,
    "homewood mountain resort": 949.00,
    "hoodoo ski area": 699.00,
    "howelsen hill": 279.00,
    "hunt hollow ski club": 455.00,
    "hunter mountain": 949.00,
    "hyland ski & snowboard area": 499.00,
    "jack frost": 949.00,
    "jackson hole": 1629.00,

    "jay peak": 1079.00,
    "jiminy peak": 1329.00,
    "june mountain": 1699.00,
    "kelly canyon ski area": 989.00,
    "keystone": 377.00,
    "killington resort": 1369.00,
    "king pine": 639.00,
    "kirkwood": 599.00,
    "kissing bridge": 800.00,
    "labrador mt.": 599.00,

    "lee canyon": 1049.00,
    "liberty": 949.00,
    "little switzerland": "No Season Pass Pricing Data",
    "lookout pass ski area": 479.00,
    "loon mountain": 1449.00,
    "lost trail - powder mtn": 499.00,
    "lost valley": 645.00,
    "loveland ski area": 649.00,
    "lutsen mountains": 900.00,
    "mad river glen": 875.00,

    "mad river mountain": 949.00,
    "magic mountain": 799.00,
    "magic mountain ski area": 390.00,
    "mammoth mountain": 1179.00,
    "maple ski ridge": 399.00,
    "marquette mountain": 386.00,
    "massanutten": 630.00,
    "maverick mountain": 450.00,
    "mccauley mountain ski area": 305.00,
    "meadowlark ski lodge": 485.00,

    "mission ridge": 629.00,
    "mohawk mountain": 749.00,
    "monarch mountain": 629.00,
    "mont ripley": 485.00,
    "montage mountain": 549.00,
    "montana snowbowl": 823.00,
    "mount bohemia": 109.00,
    "mount holly": 825.00,
    "mount kato ski area": 449.00,
    "mount la crosse": 625.00,

    "mount peter ski area": 499.00,
    "mount pleasant of edinboro": 350.00,
    "mount snow": 949.00,
    "mount southington ski area": 750.00,
    "mount sunapee": 949.00,
    "mountain creek resort": 499.99,
    "mountain high": 849.00,
    "mt. abram ski resort": 599.00,
    "mt. ashland": 624.00,
    "mt. bachelor": 1579.00,

    "mt. baker": 1102.40,
    "mt. baldy": 599.00,
    "mt. brighton": 949.00,
    "mt. crescent ski area": 299.00,
    "mt. holiday ski area": 285.00,
    "mt. hood meadows": 519.00,
    "mt. hood skibowl": 1149.00,
    "mt. rose - ski tahoe": 925.00,
    "mt. shasta ski park": 699.00,
    "mt. spokane ski and snowboard park": 849.00,

    "mulligan's hollow ski bowl": 264.00,
    "nashoba valley": 700.00,
    "nordic mountain": 549.00,
    "nordic valley resort": 1149.00,
    "northstar california": 949.00,
    "nubs nob ski area": 700.00,
    "oak mountain": 440.00,
    "ober mountain ski area & adventure park": 399.00,
    "okemo mountain resort": 949.00,
    "otis ridge ski area": 319.00,

    "pajarito mountain ski area": "No Season Pass Pricing Data",
    "palisades tahoe": 1699.00,
    "paoli peaks": 949.00,
    "park city": 949.00,
    "pats peak": 619.00,
    "pebble creak ski area": 568.00,
    "peek'n peak": 572.00,
    "perfect north slopes": 594.00,
    "pico mountain": 1119.00,
    "pine knob ski resort": 825.00,

    "pine mountain": 349.00,
    "plattekill mountain": 499.00,
    "pleasant mountain": 884.00,
    "pomerelle mountain resort": 575.00,
    "powder mountain": 1150.00,
    "powder ridge park": 649.00,
    "powder ridge ski area": 545.00,
    "powderhorn": 699.00,
    "purgatory": 1149.00,
    "ragged mountain resort": 699.00,

    "red lodge mountain": 999.00,
    "red river": 665.00,
    "roundtop mountain resort": 949.00,
    "royal mountain ski area": 450.00,
    "sapphire valley": 1100.00,
    "saskadena six": 529.00,
    "schuss mountain at shanty creek": 400.00,
    "schweitzer": 1049.00,
    "seven oaks": 397.00,
    "seven springs": 949.00,

    "shawnee mountain ski area": 539.00,
    "showdown montana": 750.00,
    "sierra-at-tahoe": 599.00,
    "silver mountain": 609.00,
    "silverton mountain": 699.00,
    "sipapu ski resort": 1149.00,
    "ski apache": 1050.00,
    "ski big bear": 415.00,
    "ski brule": 445.00,
    "ski butternut": 549.00,

    "ski china peak": 849.00,
    "ski granby ranch": 640.00,
    "ski sawmill": 499.00,
    "ski snowstar winter sports park": 275.00,
    "ski sundown": 750.00,
    "ski ward": 665.00,
    "sleeping giant ski resort": 480.00,
    "smugglers notch resort": 699.00,
    "snow creek": 949.00,
    "snow king mountain": 750.00,

    "snow ridge": 455.00,
    "snow snake mountain ski area": 250.00,
    "snow summit": "No Season Pass Pricing Data",
    "snow trails": 625.00,
    "snow valley": "No Season Pass Pricing Data",
    "snowbasin": 1399.00,
    "snowbird": 1549.00,
    "snowriver mountain resort": 700.00,
    "snowshoe mountain": 549.00,
    "snowy range ski & recreation area": 429.00,

    "soda springs": 279.00,
    "soldier mountain ski area": 499.00,
    "solitude mountain resort": 1699.00,
    "song mountain": 599.00,
    "spirit mountain": 619.00,
    "spring mountain ski area": 395.00,
    "steamboat": 1699.00,
    "stevens pass resort": 949.00,
    "stowe mountain": 949.00,
    "stratton mountain": 1699.00,

    "sugar bowl resort": 1299.00,
    "sugar mountain resort": 1200.00,
    "sugarbush": 1699.00,
    "sugarloaf": 1449.00,
    "sun valley": 1699.00,
    "sunburst": 319.00,
    "sundance": 849.00,
    "sunday river": 1449.00,
    "sundown mountain": 420.00,
    "sunlight mountain resort": 499.00,

    "sunrise park resort": 689.00,
    "swain": 765.00,
    "swiss valley": 389.00,
    "tahoe donner": 607.00,
    "tamarack resort": 699.00,
    "taos ski valley": 1475.00,
    "telluride": 2460.00,
    "terry peak ski area": 800.00,
    "teton pass ski resort": 600.00,
    "the highlands": 799.00,

    "the homestead": 299.00,
    "the omni homestead resort": 225.00,
    "the summit at snoqualmie": 799,
    "timber ridge": 520.00,
    "timberline lodge": 1149.00,
    "timberline mountain": 649.00,
    "titus mountain": 629.00,
    "treetops resort": 159.00,
    "trollhaugen": 525.00,
    "tussey mountain": 569.00,

    "tyrol basin": 499.99,
    "vail": 949.00,
    "wachusett mountain ski area": 899.00,
    "waterville valley": 1204.00,
    "welch village": 530.00,
    "west mountain": 899.00,
    "whaleback mountain": 275.00,
    "white pass": 839.00,
    "white pine ski area": 540.00,
    "whitecap mountain": 595.00,

    "whiteface mountain resort": 1119.00,
    "whitetail resort": 949.00,
    "wild mountain ski & snowboard area": 439.00,
    "wildcat mountain": 949.00,
    "willamette pass": 1149.00,
    "willard mountain": 600.00,
    "wilmot mountain": 949.00,
    "windham mountain": 1699.00,
    "winter park": 1699.00,
    "wintergreen resort": 699.00,

    "winterplace ski resort": 699.00,
    "wisp": 699.00,
    "wolf creek ski area": 1297.00,
    "woods valley ski area": 550.00,
    "yawgoo valley": 569.00,
    "yosemite ski & snowboard area": 150.00,
}

while True:
    # Open the text file "ski_resort_name.txt" and read the first line.
    # The program calling this microservice must provide the ski resort name in the text file.
    time.sleep(1)
    text_file_r = open("ski_resort_name.txt", "r")
    resort_name = text_file_r.readline()
    text_file_r.close()

    # If there is text printed in the text file, convert it to lower case then search for it in the dictionary.
    if resort_name != "":
        resort_name_lowercase = resort_name.casefold()

        # If the resort name is found in the dictionary, get the season pass dollar_value of that resort.
        if resort_name_lowercase in ski_resort_dictionary:
            dollar_value = ski_resort_dictionary.get(resort_name_lowercase)

            # Print dollar_value to price_output.txt.
            text_file_w = open("price_output.txt", "w")
            text_file_w.write(str(dollar_value))
            text_file_w.close()

        else:
            # If the resort name is not found in the dictionary, print an error message to price_output.txt.
            text_file_w = open("price_output.txt", "w")
            text_file_w.write("Error: No matching resort name found")
            text_file_w.close()
