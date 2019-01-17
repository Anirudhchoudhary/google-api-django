from __future__ import print_function
from apiclient import discovery
from httplib2 import Http
from oauth2client import file, client, tools

SCOPES = 'https://www.googleapis.com/auth/calendar'
store = file.Storage('storage.json')
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('C:\\Users\\anny\\Desktop\\image_work\\customimage\\customimage\\client_secret.json', SCOPES)
    creds = tools.run_flow(flow, store)
GCAL = discovery.build('calendar', 'v3', http=creds.authorize(Http()))

GMT_OFF = '+05:30'      # PDT/MST/GMT-7

EVENT = {
    'summary': 'Dinner with friends',
    'start':  {'dateTime': '2019-01-16T14:30:00%s' % GMT_OFF},
    'end':    {'dateTime': '2019-01-16T15:00:00%s' % GMT_OFF},
    'attendees': [
        {'email': 'anirudhchoudary007@gmail.com'},
        {'email': 'anirudh.malik@adypu.edu.in'},
    ],
}

print(EVENT['start'])
e = GCAL.events().insert(calendarId='primary',
        sendNotifications=True, body=EVENT).execute()


# service.events().delete(calendarId='primary', eventId='eventId').execute()


print('''*** %r event added:
    Start: %s
    End:   %s
    id: %s''' % (e['summary'].encode('utf-8'),
        e['start']['dateTime'], e['end']['dateTime'],
        e['id']))