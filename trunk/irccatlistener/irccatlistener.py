import socket
from trac.core import *
from trac.ticket.api import ITicketChangeListener

class IrcCatListener(Component):
    implements(ITicketChangeListener)

    def _sendText(self, ticketid, text):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect(("localhost",12345))
            s.send("Trac: ")
	    s.send("ticket #%i (http://trac.snailbyte.com/ayourta/ticket/%i) %s" % (ticketid, ticketid, text))
            s.close()
        except:
	    print "Unexpected error:", sys.exc_info()[0]
            return

    def ticket_created(self, ticket):
        self._sendText(ticket.id, "\"%s\" created by %s." % (ticket.values['summary'][0:100], ticket.values['reporter']))

    def ticket_changed(self, ticket, comment, author, old_values):
	self._sendText(ticket.id, "changed by %s, Comment: %s." % (author, comment[0:100]))

    def ticket_deleted(self, ticket):
        self._sendText(ticket.id, "Ticket deleted")
