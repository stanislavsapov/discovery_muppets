#! /usr/bin/python

import webbrowser
#
#

# region = "cz"
# name = " black john"
# url = "https://www.google.%s/?q=%s" % (region, name)
# b = webbrowser.get("open -a /Applications/Google\ Chrome.app %s")
#         # b.open_new_tab(url)
# b.open(url, new=1, autoraise=True)
def open_browser(url):

    # OPEN A NEW TAB WITH URL

    b = webbrowser.get("open -a /Applications/Google\ Chrome.app %s")
    b.open_new_tab(url)

def google_search(name,region):

    #   GOOGLE SEARCH DEPENDS ON THE REGION


    url = "https://www.google.%s/?gfe_rd=cr&ei=SwhPVqKhIIjZ8Aeb-aioCg#q=%s" % (region, name)
    open_browser(url)

def linkedin_search(name, region_abr):

    #   LINKEDIN SEARCH BY PEOPLE
    strange_var = "%3A0"
    url = "https://www.linkedin.com/vsearch/p?orig=FCTD&keywords=%s&openFacets=N,G,CC&f_G=%s%s" % (name, region_abr, strange_var)
    open_browser(url)


def facebook_search(name):

    #   FACEBOOK SEARCH BY PEOPLE

    url = "https://www.facebook.com/search/str/%s/keywords_users" % name.replace("+", "%20")
    open_browser(url)

def twitter_search(name):

    #   TWITTER SEARCH

    url = "https://twitter.com/search?f=users&vertical=default&q=%s&src=typd" % name.replace("+", "%20")
    open_browser(url)

def xing_search(name):

    #   XING SEARCH
    strange_var = "members?facets%5B%5D=country&facets%5B%5D=contact_level&filters%5Bcountry%5D%5B%5D=de&keywords="
    url = "https://www.xing.com/search/%s%s&page=1&sort=relevance" % (strange_var, name)
    open_browser(url)


def germany(name):

    print "Germany search"
    google_search(name, "de")
    linkedin_search(name, "de")
    facebook_search(name)
    twitter_search(name)
    xing_search(name)

#
def france(name):
    print "France search"
    google_search(name, "fr")
    linkedin_search(name, "fr")
    facebook_search(name)
    twitter_search(name)
#
def belgium(name):
    print "belgium search"
    google_search(name, "be")
    linkedin_search(name, "be")
    facebook_search(name)
    twitter_search(name)
#
def switz(name):
    print "switz search"
    google_search(name, "ch")
    linkedin_search(name, "ch")
    facebook_search(name)
    twitter_search(name)

#
def uae():
    print "uae search"
    google_search(name, "ae")
    linkedin_search(name, "ae")
    facebook_search(name)
    twitter_search(name)
#
def netherlands():
    print "netherlands search"
    google_search(name, "ae")
    linkedin_search(name, "ae")
    facebook_search(name)
    twitter_search(name)


def errhandler ():
   print "Your input has not been recognised"

def main():
    #MAIN FUNCTION TO START A SEARCH DEPENDS ON THE REGION

    print  "======================================="
    print "List of countries where we will look for"
    print  "======================================="
    print "1 Germany"
    print "2 France"
    print "3 Belgium"
    print "4 Switzerland"
    print "5 UAE"
    print "6 Netherlands"
    print "======================================="
    print " "

    x = int(raw_input("Hey Muppet in which region are you???"
                      "Choose the number from 1 till 6"))

    # setup a dictionary of action search
    takeaction = {
        1 : germany,
        2 : france,
        3 : belgium,
        4: switz,
        5: uae,
        6: netherlands
    }
    print  "======================================="
    print " WHO ARE YOU LOOKING FOR???"
    print  "======================================="

    name_str = str(raw_input("Please tell me the name: "))

    #replace spaces with ++++++++++
    name = name_str.replace(" ", "+")
    takeaction[x](name)


if __name__ == '__main__':
    main()