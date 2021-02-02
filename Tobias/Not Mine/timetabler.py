from datetime import datetime, date

class Timetabler(object):
    def __init__(self):
        self.events = None

    def getEvents(self):
        with open('schedule.txt', 'r') as file:
            self.events = file.read().split('\n')
        file.close()
        return self.events

    def autocheckEvents(self):
        events = str(self.getEvents()).split()
        present = datetime.now()
        present = str(str(present).split('-')[2]).split(' ')
        presentDate = date(int(present[0]), int(present[1]), int(present[2]))
        for line in self.events:
            if str(line) != '':
                event = str(line).split(', ')[1].split('/')
                eventDate = date(int(event[0]), int(event[1]), int(event[2]))
                daysLeft = presentDate - eventDate
                if daysLeft.days < 0:
                    self.removeEvent(str(line).split(', ')[0])
                elif daysLeft.days == 0:
                    print('The event {} is happening/due today'.format(str(line).split(', ')[0]))
                else:
                    print('There are {} days till the event {}'.format(daysLeft.days, str(line).split(', ')[0]))

    def manualCheckEvent(self, name):
        events = str(self.getEvents()).split('\n')
        present = datetime.now()
        present = str(present).split('-')
        present[2] = str(present[2]).split(' ')
        presentDate = date(int(present[0]), int(present[1]), int(present[2][0]))
        for line in self.events:
            if str(line) != '':
                if str(line).split(', ')[0].lower() == str(name).lower():
                    event = str(line).split(', ')[1].split('/')
                    eventDate = date(int(event[0]), int(event[1]), int(event[2]))
                    daysLeft = presentDate - eventDate
                    if daysLeft.days > 0:
                        self.removeEvent(str(line).split(', ')[0])
                    elif daysLeft.days == 0:
                        print('The event {} is happening/due today'.format(str(line).split(', ')[0]))
                    else:
                        print('There are {} days till the event {}'.format(abs(daysLeft.days), str(line).split(', ')[0]))
                    break

    def addEvent(self, name, date):
        with open('schedule.txt', 'a') as file:
            file.write('\n{}, {}'.format(name, str(date).replace(' ', '')))
        file.close()

    def removeEvent(self, name):
        events = self.getEvents()
        for line in self.events:
            if str(line) != '':
                if str(str(line).split(',')[0]).lower() == str(name).lower():
                    self.events.remove(str(line))
        with open('schedule.txt', 'w') as file:
            for line in self.events:
                file.write('{}\n'.format(line))
        file.close()

    def clearEvents(self):
        with open('schedule.txt', 'w') as file:
            file.write('')
        file.close()