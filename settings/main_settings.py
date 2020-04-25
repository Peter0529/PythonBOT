import base64
################################ MAIN SETTINGS ############################################################################

MAIN_SITE                           = "http://www.audiomack.com"

SETTINGS_FOLDER                     = "settings/"

CHROME_DRIVER_PATH                  = SETTINGS_FOLDER + "chromedriver.exe"

PORTABLE_CHROME_PATH                = SETTINGS_FOLDER + "GoogleChromePortable/App/Chrome-bin/chrome.exe"

PAGE_LOAD_TIMEOUT                   = 60

################################ EXTENSION SETTINGS ########################################################################

EXTENSIONS_FOLDER                   = 'Extensions/'

FORCE_EXTENSIONS_PATH               = [ SETTINGS_FOLDER + EXTENSIONS_FOLDER + 'canvasblocker.crx',
                                        SETTINGS_FOLDER + EXTENSIONS_FOLDER + 'ublock_origin.crx',
                                        SETTINGS_FOLDER + EXTENSIONS_FOLDER + 'webrtc.crx',
                                        ]

RANDOM_EXTENSIONS_PATH              = [
                                        SETTINGS_FOLDER + EXTENSIONS_FOLDER + 'ext1.crx',
                                        SETTINGS_FOLDER + EXTENSIONS_FOLDER + 'ext2.crx',
                                        SETTINGS_FOLDER + EXTENSIONS_FOLDER + 'ext3.crx',
                                        ]

################################ WINDOW SIZES SETTINGS ######################################################################

WINDOW_SIZES                        = [
                                        [800,800],
                                        [1200,1000],
                                        [1500,1200],
                                        [1000,800],
                                    ]


################################ CRUD APIS ##################################################################################

CRUDAPI_USERNAME                    = "admin"

CRUDAPI_PASSWORD                    = "admincrud123"

CRUDAPI_AUTH_TOKEN                  = "Bearer " + base64.b64encode((CRUDAPI_USERNAME + ":" + CRUDAPI_PASSWORD).encode("ascii")).decode("ascii")

CRUDAPI_BASE_URL                    = "https://www.dashon.net:10003/admin-crud-demo/cruddb/"

#GET

CRUDAPI_GET_INFOS                   = CRUDAPI_BASE_URL + "get_random_infos/s1-"

CRUDAPI_GET_S1_SETTINGS             = CRUDAPI_BASE_URL + "get_settings/s1"

CRUDAPI_GET_S1_CAMPAIGN             = CRUDAPI_BASE_URL + "get_campaign/s1"

#POST

CRUDAPI_POST_ACCOUNT_FAIL           = CRUDAPI_BASE_URL + "plus_signin_fail"

CRUDAPI_POST_CLOSED_THREAD          = CRUDAPI_BASE_URL + "closed_thread"

CRUDAPI_POST_ERROR_LOG              = CRUDAPI_BASE_URL + "create_error"

CRUDAPI_POST_ACTION_COUNT           = CRUDAPI_BASE_URL + "add_action_count/"




