
class ToorChatProtocol():
	''' This is a class to allow for easy of use with anything to do with messaging '''
	def __init__(self, device):
		self.PACKET_START = "\xFF\xDE\xAD\xFF"
		self.PACKET_END = "\xFF\xBE\xEF\xFF"
		self.device = device

	def send_message(self, message = "", user = None):
		''' This is used to send a simple message over the toorchat protocol '''
		msg = ToorChatMessage(message, user)
		self.device.RFxmit(msg.to_string())

	@classmethod
	def get_packet_start(cls):
		return "\xFF\xDE\xAD\xFF"
	
	@classmethod
	def get_packet_end(cls):
		return "\xFF\xBE\xEF\xFF"

class ToorChatMessage():
	''' This is a simple Message object wrapper to make things cleaner '''

	def __init__(self, message = "", user = None):
		self.start = ToorChatProtocol.get_packet_start()
		self.xid = self.get_random_xid()
		if user != None:
			self.user = user
		else:
			self.user = "\x00"*32
		self.data = message
		self.end = ToorChatProtocol.get_packet_end()

	def get_random_xid(self):
		return "44444444"

	def __str__(self):
		return self.start + self.xid + self.user + self.data + self.end

	def to_string(self):
		return self.__str__()