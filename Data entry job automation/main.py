from get_data import GetData
from put_data import PutData

get = GetData()
put = PutData()

link = get.find_link()
address = get.find_addresses()
prices = get.find_price()

put.open_forms()
put.fill_form(a_list=address, l_link=link, p_list=prices)