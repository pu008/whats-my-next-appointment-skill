from mycroft import MycroftSkill, intent_file_handler


class WhatsMyNextAppointment(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('appointment.next.my.whats.intent')
    def handle_appointment_next_my_whats(self, message):
        datetime = ''
        eventname = ''

        self.speak_dialog('appointment.next.my.whats', data={
            'datetime': datetime,
            'eventname': eventname
        })


def create_skill():
    return WhatsMyNextAppointment()

