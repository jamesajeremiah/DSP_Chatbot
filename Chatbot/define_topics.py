# Author: James Jeremiah
# james2.jeremiah@uwe.ac.uk
# Student number: 17042447
# 27/04/2021
# 
# Intended to be modified by an adminstrator.
# Define topics for the chatbot to recognise and respond to.
# See the README for more details.

def main():

    ########## DEFINE TOPICS ##########

    return(
    [
    
    ################################ INTENTS ################################


    ######### SIGN_IN #########
    (
        # ID
    "SIGN_IN",

    [   # PATTERNS
    [{'LEMMA': {'IN': ['sign', 'log']}}, {'LOWER': 'in'}],
    [{'LOWER': 'login'}],
    [{'LOWER': 'signin'}],
    ],

    [   # PARENTS AND PATTERN CONNECTIONS
    ],

        # RESPONSE
    '''How can I help you with Adobe?''',

        # IS A SOLUTION?
    False
    ),


    ######### MISSING #########
    (
        # ID
    "MISSING",

    [   # PATTERNS
    [{'LEMMA': {'IN': ['miss', 'disappear', 'go']}}],
    [{'DEP': 'neg'}, {'LEMMA': 'there'}]
    ],

    [   # PARENTS AND PATTERN CONNECTIONS
    ],

        # RESPONSE
    '''Could you repeat what was missing?''',

        # IS A SOLUTION?
    False
    ),


    ######### CAN'T SEND #########
    (
        # ID
    "CANT_SEND",

    [   # PATTERNS
    [{'DEP': 'neg'}, {'LEMMA': 'send'}],
    [{'LEMMA': 'unable'}, {'OP': '?'}, {'LEMMA': 'send'}],
    [{'LEMMA': 'bounce'}, {'LEMMA': 'back'}],
    ],

    [   # PARENTS AND PATTERN CONNECTIONS
    ],

        # RESPONSE
    '''What is it you're unable to send?''',

        # IS A SOLUTION?
    False
    ),


    ######### WORKING_OFFLINE #########
    (
        # ID
    "WORKING_OFFLINE",

    [   # PATTERNS
    [{'LOWER': 'working'}, {'LOWER': 'offline'}]
    ],

    [   # PARENTS AND PATTERN CONNECTIONS
    ],

        # RESPONSE
    '''Where is this 'working offline' issue taking place?''',

        # IS A SOLUTION?
    False
    ),


    ######### LICENCE #########
    (
        # ID
    "LICENCE",

    [   # PATTERNS
    [{'LEMMA': 'licence'}],
    [{'LEMMA': 'license'}]
    ],

    [   # PARENTS AND PATTERN CONNECTIONS
    ],

        # RESPONSE
    '''Which program are you having licensing issues for?''',

        # IS A SOLUTION?
    False
    ),

 

    ################################ SYSTEMS ################################


    ############### ADOBE ###############


    ######### ADOBE #########

    (
        # ID
    "ADOBE",

    [   # PATTERNS
    [{'LOWER': 'adobe'}],
    [{'LOWER': 'pdf'}],
    ],

    [   # PARENTS AND PATTERN CONNECTIONS
    ],

        # RESPONSE
    '''How can I help you with Adobe?''',
    
        # IS A SOLUTION?
    False

    ),


    ######### ADOBE_CREATIVE_CLOUD #########
    (
        # ID
    "ADOBE_CREATIVE_CLOUD",
    [   # PATTERNS
    ],
    [   # PARENTS AND PATTERN CONNECTIONS
    ["ADOBE", ["SIGN_IN", "LICENCE"]],
    ["SIGN_IN", ["ADOBE"]],
    ["LICENCE", ["ADOBE"]],
    ],
        # RESPONSE
    '''You'll need to sign into Adobe Creative Cloud so that it keeps up to date and renews the license.

If Adobe Creative Cloud isn't already installed on your computer, you can find it in the Software Center and install it from there.

Once Creative Cloud is installed, you can open it and sign in as uwe.ac.uk (no password required). Then, once that's signed in, head to the 'Apps' tab where you can install any Adobe software that you need.

If you are unable to sign in with uwe.ac.uk, you can use your UWE email address and login details instead.''',

        # IS A SOLUTION?
    True
    ),



    ############### EMAIL ###############


    ######## EMAIL #########

    (
        # ID
    "EMAIL",

    [   # PATTERNS
    [{'LOWER': 'outlook'}],
    [{'LEMMA': 'email'}]
    ],

    [   # PARENTS AND PATTERN CONNECTIONS
    ],

        # RESPONSE
    '''How can I help you with your emails?''',

        # IS A SOLUTION?
    False
    ),


    ######### GENERIC_MAILBOX #########
    (
        # ID
    "GENERIC_MAILBOX",

    [   # PATTERNS
    ],

    [   # PARENTS AND PATTERN CONNECTIONS
    ['EMAIL', [ [{'LEMMA': {'IN': ['generic', 'share']} }]] ]
    ],

        # RESPONSE
    '''How can I help you with the generic mailbox?''',

        # IS A SOLUTION?
    False
    ),
    

    ######## CAN'T_SEND_EMAILS ########
    (
        # ID
    "CANT_SEND_EMAILS",

    [   # PATTERNS
    ],

    [   # PARENTS AND PATTERN CONNECTIONS
    ["EMAIL", ["CANT_SEND"]],
    ["CANT_SEND", ["EMAIL"]],
    ],

        # RESPONSE
    '''Is this from your own mailbox or from a generic mailbox?''',

        # IS A SOLUTION?
    False
    ),


    ######## WORKING_OFFLINE_OUTLOOK ########
    (
        # ID
    "WORKING_OFFLINE_OUTLOOK",
    [   # PATTERNS
    ],
    [   # PARENTS AND PATTERN CONNECTIONS
    ["EMAIL", ["WORKING_OFFLINE"]],
    ["WORKING_OFFLINE", ["EMAIL"]],
    ["CANT_SEND_EMAILS", [ [{'LEMMA': {'IN': ['my', 'mine', 'own', 'individual']} }] ] ]
    ],
        # RESPONSE
    '''This issue may be because Outlook has set itself to working offline. If you open Outlook and see in the bottom-right corner 'Working Offline', then this is the case.

To resolve this issue, you can head to the 'Send/Receive' tab near the top and then click once on the 'Work Offline' button on the right of the new row. This should set it to work online and your emails will update.
''',

        # IS A SOLUTION?
    True
    ),
    

    ######## CAN'T SEND FROM GENERIC MAILBOX FIX 1 ########
    (
        # ID
    "CANT_SEND_FROM_GENERIC_MAILBOX_1",
    [   # PATTERNS
    ],
    [   # PARENTS AND PATTERN CONNECTIONS
    ['CANT_SEND', [ [{'LEMMA': {'IN': ['generic', 'share']} }]] ],
    ['CANT_SEND_EMAILS', [ [{'LEMMA': {'IN': ['generic', 'share']} }]] ],
    ["GENERIC_MAILBOX", ["CANT_SEND", "CANT_SEND_EMAILS"]]
    ],
        # RESPONSE
    '''Make sure that the custodian has set up the correct permissions for you to access the folders and subfolders of the generic inbox.

If they have done so and you're still receiving this error, you may need to turn off caching in Outlook.
You can turn off caching by opening up Outlook and going to:
- 'File'
- 'Account Settings', then 'Account settings' in the drop-down
- Double-click on your email address in the list.
- Untick the 'Use Cached Exchange Mode'
- Click on 'Next', then 'Finish'
Then restart Outlook and you should be able to see all of the emails in the generic inbox.
''',

        # IS A SOLUTION?
    True
    ),


    ######## CAN'T SEND FROM GENERIC MAILBOX FIX 2 ########
    (
        # ID
    "CANT_SEND_FROM_GENERIC_MAILBOX_2",
    [   # PATTERNS
    ],
    [   # PARENTS AND PATTERN CONNECTIONS
    ["CANT_SEND_FROM_GENERIC_MAILBOX_1", ["UNSOLVED"]],
    ],
        # RESPONSE
    '''Head to the bottom-left search box and search for Control and open up 'Control Panel' that shows up.
Then, search for Mail in the top-right search box and open up Mail (32-bit) that shows up.
Next, click on 'Show Profiles'.
Then click on 'Remove' and click 'Yes' to the popup.
Then click 'Add...' and call the profile name Outlook2. Then click OK.
Next, add in your UWE email address (and password if prompted). Then click 'Next', then 'Finish'.
Finally, click 'Apply' and then 'OK'. 
Once you start Outlook, it should rebuild your profile and load up your UWE emails.
''',

        # IS A SOLUTION?
    True
    ),
    
    

    ############### H_DRIVE ###############


    ######## H_DRIVE ########
    (
        # ID
    "H_DRIVE",

    [   # PATTERNS
    [{'LOWER': 'h', 'OP': '?'}, {'LOWER': 'drive'}]
    ],

    [   # PARENTS AND PATTERN CONNECTIONS
    ],

        # RESPONSE
    '''How can I help you with your H Drive?''',

        # IS A SOLUTION?
    False
    ),


    ######## H_DRIVE_MISSING ########
    (
        # ID
    "H_DRIVE_MISSING",

    [   # PATTERNS
    ],

    [   # PARENTS AND PATTERN CONNECTIONS
    ["MISSING", ["H_DRIVE"]],
    ["H_DRIVE", ["MISSING"]]
    ],

        # RESPONSE
    '''If the H Drive has disappeared, often a computer restart will bring access to the H Drive back.

If a restart doesn't work, you can reconnect the drives with the solution below.
Head to the bottom-left corner search box and type in Reconnect Network Drives.
Then, click on the 'Reconnect Network Drives' app in the list.
This script will take about a minute to reconnect your drives and it will be completed once it opens up File Explorer automatically.

If the H drive still struggles to return, you may also access it by signing into https://xa.uwe.ac.uk/staffmfa ''',

        # IS A SOLUTION?
    True
    ),
    
    
    ############### PASSWORD_RESET ###############
    (
        # ID
    "PASSWORD_RESET",
    [   # PATTERNS
    [{'LEMMA': {'IN': ['forget', 'reset']}}, {'LOWER': 'password'}],
    [{'LEMMA': {'IN': ['forget', 'reset']}}, {}, {'LOWER': 'password'}],
    [{'LEMMA': {'IN': ['forget', 'reset']}}, {}, {}, {'LOWER': 'password'}],
    [{'DEP': 'neg'}, {'LEMMA': 'remember'}, {'LOWER': 'password'}],
    [{'DEP': 'neg'}, {'LEMMA': 'remember'}, {}, {'LOWER': 'password'}],
    [{'DEP': 'neg'}, {'LEMMA': 'remember'}, {}, {}, {'LOWER': 'password'}],
    [{'LOWER': 'password'}, {'LEMMA': 'reset'}],
    [{'LOWER': 'password'}, {}, {'LEMMA': 'reset'}],
    [{'LOWER': 'password'}, {}, {}, {'LEMMA': 'reset'}]
    ],
    [   # PARENTS AND PATTERN CONNECTIONS
    ],
        # RESPONSE
    '''If you need to reset your password, you can do so it via the automated password reset tool at https://password.uwe.ac.uk/

If you're still having issues, please phone us on 0117 32 83612, so we can verify your identity.
We are available 24 hours a day, 7 days a week.
You will be required to provide security information such as student/staff ID, date of birth, postcode or national insurance number.''',

        # IS A SOLUTION?
    True
    ),

    
    ])
    ########## END OF TOPICS ##########
    
    
if __name__ == "__main__":
    main()