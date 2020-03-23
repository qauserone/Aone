###

class MsgBrowser():
    __SIZE = "{0}X{1}px"
    # OPEN BROWSERS
    MSG_OPEN_CHROME = 'Open Chrome browser'
    MSG_OPEN_FIREFOX = 'Open Firefox browser'
    MSG_OPEN_IE= 'Open IE browser'
    MSG_CLOSE_BROWSER = 'Close browser'
    # MAXIMIZE
    MSG_MAXIMIZE = "Maximize the screen of browser"
    # PAGE
    MSG_URL = 'go to url: {}'
    MSG_CURRENT_URL = 'The current URL is: {}'
    MSG_REFRESH = 'Refresh the page'
    # WINDOWS SIZE
    MSG_WINDOW_SIZE = "Get the window size. The size is %s."%__SIZE
    MSG_SET_WINDOW_SIZE = "Set the window's size, the size is %s."%__SIZE
    # TAB
    MSG_NEW_TAB = "Created a new tab with url: {}"
    __TAB = "Change the active tab"
    MSG_CHANGE_TAB = "%s for the tab in position {}"%__TAB
    MSG_CHANGE_TAB_ERROR = "Don't exist a tab in position {}"
    MSG_CLOSE_TAB = "Close the active tab"
    MSG_BACK_PAGE = "Go to previous page"
    MSG_FORWARD_PAGE = "Go to next page"
    # MOBILE
    __MOBILE = 'Open chrome browser with '
    MSG_MOBILE = '%s{} device interface'%__MOBILE
    MSG_MOBILE_SIZE = '%sresolution %s. Pixel ratio {2}'%(__MOBILE, __SIZE)
    

class MsgLog():
    # CREATE LOG
    MSG_CREATE_LOG = "The log is in {}" 


class MsgSearch():
    # SEARCH ELEMENTS
    MSG_SEARCH_ELEM = 'The element {} was found'
    MSG_SEARCH_ELEM_ERROR = "The element {} wasn't found"
    MSG_SEARCH_ELEMS = "Found {0} elements with xpath {1}"
    MSG_SEARCH_ELEM_ID_ERROR = "The element with id {} wasn't found"
    MSG_DOUBLE_SEARCH = 'Start double search'
    MSG_DOUBLE_SEARCH_ERROR = "The searched elements weren't found"
    # COMPARE TEXT
    MSG_COMPARE_TEXT = "The text {0}, show in searched element {1}"
    MSG_COMPARE_TEXT_ERROR = "The text {0}, doesn't show in searched element {1}"
    DSC_COMPARE_TEXT = "Expected value {0}, found value {1}"
    # VERIFY
    MSG_VERIFY = "Verify: {}"
    MSG_VERIFY_ERROR = "Can't verify: {}"
    MSG_VERIFY_VALUES = "Number of element to search = {}"
    __SEARCH = "Number of element to search = {}"
    __FOUNDED = "Number of element found {}"
    MSG_VERIFY_VALUES_RESULT = "%s\n%s\nSearched elements {}"%(__SEARCH, 
                                                               __FOUNDED)
    # CHECK FIELDS
    __F_SEARCH = "Number of fields to search {0}"
    __F_FOUNDED = "Number of fields found = {1}"
    __NOT_FOUND = "Number of fields not found = {2}"
    MSG_RESULT_CHECK_FIELD = "%s\n%s\n%s"%(__F_SEARCH, __FOUNDED, __NOT_FOUND)
    MSG_CHECK_FIELD_ERROR = "Some fields aren't showing"
    MSG_SEARCH_ELEM_BY = "Search elemento by {0} with value {1}"


class MsgImage():
    # SCREEN SHOT
    MSG_SCREENSHOT = 'The screenshot is made. {}'
    MSG_ALLURE = 'Taked a Allure screenshot'
    MSG_SCREENSHOT_BUFFER = "Taked a screenshot"
    MSG_GET_IMAGE = "The image element {0} is save in {1}"
    ####
    MSG_GET_IMAGE_ERROR = "The element {} isn't an image"
    

class MsgMouse():
    # CLICK
    MSG_CLICK_ELEM = 'Click on {}'
    MSG_CLICK_ELEM_ERROR = 'The element could not be clicked'
    MSG_DOUBLE_CLICK = "Double click on {}"
    MSG_DRAG_DROP = "Drag {0} to drop in {1}"


class MsgSelect():
    # SELECT
    MSG_SELECT_OPTION = "Select the {0} option in {1}"
    __OPTION = "The option ism't within"
    __ERROR = "the available options"
    MSG_SELECT_OPTION_ERROR = '%s %s'%(__OPTION, __ERROR)
    MSG_SELECT_OPTION_REVIEW = "Check the option"
    MSG_SELECT_INDEX_ERROR = "The entered index isn't available"
    MSG_SELECT_INDEX = "From element {1}, select option by {0} index"
    MSG_SELECT_VALUE = "From element {1}, select option by {0} value"
    MSG_SELECT_TEXT = "From element {1}, select option by {0} text"
    __SEL_ERROR = "Can't obtain the option {0} by "
    MSG_SELECT_INDEX_ERROR = "%sindex in element {1}"%__SEL_ERROR
    MSG_SELECT_VALUE_ERROR = "%svalue in element {1}"%__SEL_ERROR
    MSG_SELECT_TEXT_ERROR = "%stext in element {1}"%__SEL_ERROR
    MSG_SELECT_ELEMENT_ERROR = "The searched element {}, isn't a select element"
    MSG_SELECT_RANDOM = "An option is selected, randomly"


class MsgKeyboard():
    # WRITE 
    MSG_INPUT = 'Input "{1}" in {0}'
    MSG_INPUT_KEY = "Enter the {0} key in element {1}"
    MSG_INPUT_KEY_ERROR = "The key {}, don't exist"
    # CLEAR
    MSG_CLEAR = "The content of the element {} is deleted"
    MSG_CLEAR_ERROR = "{0}\nCan't delete the content of the element {1}"


class MsgJS():
    # SCROLL
    MSG_SCROLL = 'Scroll to the element {}'
    MSG_HIGHLIGHT = "The element {} is highlighted"
    MSG_CREATE_TAB = "Created a new tab with url: {}"
    MSG_BACK = "Return to previous page"
    

class MsgWebelement():
    # GET TEXT
    MSG_GET_TEXT = "Get text {1} from {0}"
    # ATTRIBUTE
    MSG_ATTRIBUTE = "From item {1}, obtain the attribute {2}: {0}"
    MSG_ATTRIBUTE_ERROR = "Can't get the attribute {0}, from the element {1}"
    MSG_GET_LOCATION = "The location of element {0}, is {1}"
    MSG_GET_SIZE = "The size of element {0}, is {1}"
    MSG_DISPLAYED = "The element {} is displayed"
    MSG_DISPLAYED_ERROR = "The element {} isn't displayed"
    MSG_ENABLED = "The element {} is enabled"
    MSG_ENABLED_ERROR = "The element {} isn't enabled"
    MSG_SELECTED = "The element {} is selected"
    MSG_SELECTED_ERROR = "The element {} isn't selected"
    

class MsgAllure():
    MSG_ATTACH_IMAGE = "Attached the image {} in allure"
    MSG_STEP = "STEP {0}: {1}"
    
    
# RETRY
MSG_RETRY = "Retry selection: {}"

# WAITING
MSG_WAITING = "Pause for {} seconds"

