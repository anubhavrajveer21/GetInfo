from link import Link
from GetInfo import GetInfo

# Webpage Code here

query = whatever_function_techno_uses_to_get_the_text_of_search_box()

'''
If Link class raises error means that the query is not a link
and if Link class raises error then it calls GetInfo
'''
try:
    any_link = Link(query)

    if any_link.is_safe():
        any_link.open()
    else:
        '''
        Flask code to display that the website is not safe and
        ask user whether to open this website or not
        '''
        user_choosed_to_open = function_to_get_what_user_choosed()
        if user_choosed_to_open == True:
            any_link.open()
        else:
            '''Flask code to go back to home page'''
except:
    info = GetInfo(query)
    Link(info['google_search_link']).open()

    # Flask code to display the info on webpage


