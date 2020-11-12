#from pprint import pprint
import json
import requests


#main_link = 'https://api.vk.com/method/users.get'
#?user_id=210700286&v=5.52
#https://api.vk.com/method/users.get
#https://oauth.vk.com/blank.html
#
#access_token=a3fed3eec848e1521eda0de817341d85700d20492dcccb96d9fc5ffee9a974753cad67955c5a6e1c9d3f6
# &expires_in=86400
# &user_id=155984790
#id приложения - 7660892
#sKTyEeniLq6BMpNUIX46
#075661a6075661a6075661a695072284fa00756075661a658fbcfd9f89357ab4ea20157

#link_auth = 'https://oauth.vk.com/authorize'
#https://oauth.vk.com/authorize?client_id=5490057&display=page&redirect_uri=https://oauth.vk.com/blank.html&scope=friends&response_type=token&v=5.52
#https://api.vk.com/method/friends.getOnline?v=5.52&access_token=
#params_auth = {}
#https://api.vk.com/method/friends.getOnline?v=5.52&access_token=
link = 'https://api.vk.com/method/'
command = 'groups.get'
command2 = 'groups.getById'
params = {
    'user_id':155984790,
    'v':5.52,
    'access_token' : 'a3fed3eec848e1521eda0de817341d85700d20492dcccb96d9fc5ffee9a974753cad67955c5a6e1c9d3f6'
}

response = requests.get((link+command), params=params)
#response = requests.get('https://api.vk.com/method/friends.getOnline?v=5.52&access_token=a3fed3eec848e1521eda0de817341d85700d20492dcccb96d9fc5ffee9a974753cad67955c5a6e1c9d3f6')
#access_token=a3fed3eec848e1521eda0de817341d85700d20492dcccb96d9fc5ffee9a974753cad67955c5a6e1c9d3f6
if response.ok:
    j_son = response.json()
    s = ''
    for i in list(j_son["response"]["items"]):
        s = s + str(i)+','
    s = s[0:-1]
    params2 = {
        'group_ids': s,
        'v': 5.52,
        'access_token': 'a3fed3eec848e1521eda0de817341d85700d20492dcccb96d9fc5ffee9a974753cad67955c5a6e1c9d3f6'
    }


    response2 = requests.get((link + command2), params=params2)

    #print(s)

    if response2.ok:
        fil_json = open("groups.json",'w')
        fil_json.write(str(response2.json()['response']))
        fil_json.close()
        print(response2.json()['response'])
    else:
        print('nono')
else:
    print('no')

#response.headers

#response.text
#response.content
