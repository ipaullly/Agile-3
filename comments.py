comments = []

class Comments:

	def __init__(self):
		self.db = comments


	def create_comments(self, message, author):

		payload = {
			"id": len(self.db)+1,
			"message": message,
			"timestamp": timestamp,
			"author": author
		}
		self.db.append(payload)
		return payload
