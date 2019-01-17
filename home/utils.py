from __future__ import print_function
from apiclient import discovery
from httplib2 import Http
from oauth2client import file, client, tools

def add_event(startime , endtime ,name):
    SCOPES = 'https://www.googleapis.com/auth/calendar'
    store = file.Storage('C:\\Users\\anny\\Desktop\\image_work\\customimage\\storage.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('C:\\Users\\anny\\Desktop\\image_work\\customimage\\customimage\\client_secret.json', SCOPES)
        creds = tools.run_flow(flow, store)
    GCAL = discovery.build('calendar', 'v3', http=creds.authorize(Http()))


    start = '{a}'.format(a=startime)
    start = start.replace(' ','T')
    end =  '{a}'.format(a=endtime)
    end = end.replace(' ','T')

    EVENT = {
    'summary': '%s' %name,
    'start':  {'dateTime': '%s' % start},
    'end':    {'dateTime': '%s' % end},
    }

    e = GCAL.events().insert(calendarId='primary',
        sendNotifications=True, body=EVENT).execute()

    print('''*** %r event added:
        Start: %s
        End:   %s''' % (e['summary'].encode('utf-8'),
            e['start']['dateTime'], e['end']['dateTime']))
    return e['id']        


def delete_event(delete_id):
    SCOPES = 'https://www.googleapis.com/auth/calendar'
    store = file.Storage('C:\\Users\\anny\\Desktop\\image_work\\customimage\\storage.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('C:\\Users\\anny\\Desktop\\image_work\\customimage\\customimage\\client_secret.json', SCOPES)
        creds = tools.run_flow(flow, store)
    GCAL = discovery.build('calendar', 'v3', http=creds.authorize(Http()))

    e = GCAL.events().delete(calendarId='primary', eventId=delete_id).execute()

    print(e)

    return e
