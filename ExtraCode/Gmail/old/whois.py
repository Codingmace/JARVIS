from tld import get_tld
import whois # pip install python-whois

def stripUrl(url):
    # url = 'https://www.honchosearch.com/blog/seo/14-elements-every-successful-outreach-campaign-need/' #URL to strip. Change this URL to whatever you want.
     
    res = get_tld(url, as_object=True) #Get the root as an object
    return url
#    print (res.fld) #res.fld to extract the domain




##def is_registered(domain_name):
##    """
##    A function that returns a boolean indicating 
##    whether a `domain_name` is registered
##    """
###    print(domain_name)
##    try:
##        w = whois.whois(domain_name)
##        print(w)
##    except Exception:
##        return False
##    else:
##        return bool(w.domain_name)

# print(is_registered(stripUrl("https://www.google.com/")))


def main():
    domains = [
        "thepythoncode.com",
        "google.com",
        "github.com",
        "unknownrandomdomain.com",
        "notregistered.co"
    ]
    # iterate over domains
    for domain in domains:
        print(domain, "is registered" if is_registered(domain) else "is not registered")

print(whois.whois("google.com"))

# main()
