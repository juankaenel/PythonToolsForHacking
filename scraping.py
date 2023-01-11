import urllib.request
import os.path

def getSite():
    url = 'https://lorem2.com/'
    file_name = 'web.html'
    
    # checking if file already exists
    if os.path.exists(file_name):
        print(f'{file_name} already exists')
        return # if exist go to filter

    try:
        with urllib.request.urlopen(url) as response, open(file_name, 'w') as file_web:
            # in web.html -> write response
            file_web.write(response.read().decode())
            print(f"{file_name} downloaded successfully")
    except urllib.error.HTTPError as e:
        print(f"An error occurred while trying to download {file_name}. {e}")
        
def Filter():
    web = open('web.html', 'rt', encoding='utf-8')
    sli = '<li>' # start li
    eli = '</li>' # end li
    print(web)
    for line in web.readlines():
        if sli in line:
            if not "a href" in line:
                start = line.find(sli)
                start = start+len(sli)
                end = line.find(eli)
                print('\n'+line[start:end])
    web.close()
    print("\n ---------- Filter completed ----------")
            

if __name__ == "__main__":
    getSite()
    Filter()