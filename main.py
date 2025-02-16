import fofa

fofa_key = "yourFofaKey"
your_email = "FofaRegisteredEmailAddress"
client = fofa.Client(your_email, fofa_key) 

ioc_domain_list = {
   "title": ['myloginpage', 'mycompany'],
   "js_pattern": ['js/jquery'],
   "js_md5": ['82ac3f14327a8b7ba49baa208d4eaa15'],
   "icon_hash": ['-247388890']
}


def iterate(array, key):
    results = []
    if key == "title" and len(array) > 0:
        for value in array:
            query_str = f'title="{value}"'
            data = client.search(query_str, size=5, fields="host,title,ip,domain,port,country,city")
            if data and "results" in data:
                results.append({value: data['results']})     
    elif key == "js_pattern" and len(array) > 0:
        for value in array:
            query_str = f'js_name="{value}"'
            data = client.search(query_str, size=5, fields="host,title,ip,domain,port,country,city")
            if data and "results" in data:
                results.append({value: data['results']})    
    elif key == "js_md5" and len(array) > 0: 
        for value in array:
            query_str = f'js_md5="{value}"'
            data = client.search(query_str, size=5, fields="host,title,ip,domain,port,country,city")
            if data and "results" in data:
                results.append({value: data['results']})    
    elif key == "icon_hash" and len(array) > 0: 
        for value in array:
            query_str = f'icon_hash="{value}"'
            data = client.search(query_str, size=5, fields="host,title,ip,domain,port,country,city")
            if data and "results" in data:
                results.append({value: data['results']})        
    return results

for key, value in ioc_domain_list.items():
    a = iterate(value, key)
    print(a)