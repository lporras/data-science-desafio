from request_func import request

data = request("https://api.coindesk.com/v1/bpi/historical/close.json")["bpi"]
# print(data)

# selected_data = [k for k, v in data.items() if v > 5000]

under_5000 = [v for k, v in data.items() if v > 5000]
data_inv = {v:k for k, v in data.items()}
selected_data = [data_inv[k] for k in under_5000]

print(selected_data)

