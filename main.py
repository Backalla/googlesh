import mechanicalsoup
import utils
from torrequest import TorRequest

browser = mechanicalsoup.Browser()


def get_new_ip(n):
    with TorRequest(proxy_port=9001, ctrl_port=9002, password=None) as tr:
        for i in range(n):
            print(i)
            response = tr.get('http://ipecho.net/plain')
            print(response.text)  # not your IP address
            tr.reset_identity()

# browser.set_handle_robots(False)
# browser.addheaders=[('User-agent','chrome')]

def google_search(q,n):
    with TorRequest(proxy_port=9001, ctrl_port=9002, password=None) as tr:
        for i in range(n):
            print(i)
            q = q.replace(" ","+")
            
            query = "http://www.google.com/search?q="+q
            htmltext = tr.get(query).text
            results_headings = utils.get_results(htmltext)
            print(results_headings)
            print(len(results_headings))
            if len(results_headings)==0:
                print(htmltext)
                response = tr.get('http://ipecho.net/plain')
                print(response.text)
                print("Got captcha.. Resetting..")
                tr.reset_identity()

    # print(htmltext.text)
    # print(dir(htmltext))

if __name__ == '__main__':
    google_search("sample search",100)
    # get_new_ip(100)
    # for i in range(100):
    #     print(i)
    #     get_new_ip()
        # google_search("sample search")