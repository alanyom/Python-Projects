#Extracting from nested data

for res3 in res['statuses']:
    print(res3['user']['screen_name'], res3['user']['created_at'])
