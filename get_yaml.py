# get_yaml function
def get_yaml():
    with urllib.request.urlopen('https://labs.alta3.com/courses/pyb/work2do-two') as response:
        html = response.read()
        downloaded_yaml = yaml.load(html)
    return downloaded_yaml 