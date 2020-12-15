import urllib.request
import json

urlAPI = 'https://tinyurl.com/y22a99qm'

class Converter:

	rates = {}
	

	def __init__(self):
		req = urllib.request.Request(urlAPI, headers={'User-Agent': 'Live Currency Bot'})
		data = urllib.request.urlopen(req).read()
		data = json.loads(data.decode('utf-8'))
		self.rates = data["rates"]

	def convert(self, amount, from_currency, to_currency):
		initial_amount = amount
		if from_currency != "EUR":
			amount = amount / self.rates[from_currency]
		if to_currency == "EUR":
			print(f"\n\n=> {initial_amount} {from_currency} = {round(amount,2)} {to_currency,2}")
			# use return statement if you want to use these values further in your program
			# return initial_amount, from_currency, '=', amount, to_currency
		else:
			print(f"\n\n=> {initial_amount} {from_currency} = {round(amount*self.rates[to_currency],2)} {to_currency}")
			# use return statement if you want to use these values further in your program
			# return initial_amount, from_currency, '=', amount * self.rates[to_currency], to_currency


