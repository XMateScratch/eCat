import requests
import scratchattach as scratch3

# Define the base URL for the Flask API
BASE_URL = 'https://xmatetech.pythonanywhere.com/'  # Replace with your Flask server's address

# Set up Scratch session
session = scratch3.Session(".eJxVUEFOwzAQ_IvPbbBjt4l7oxIXoBygQuUUrZ1NYpLYVeKoKoi_s5Z66W01szM7s79smXHyMCLbsdMBIq6PaDu2YhUssasSW7maSK1yVZZcEBVxjjaE3iXRJUw91vcCA7ZHn1QJQx-dheiCz27EnL3jebiB-9sy-QYaSNTkUG4LbgslrJK8AZ2DsXRciVwagzu17K_d6xGfdbgcTp_m44nro76O6qUkmyG0zq_dmZzEpsgUz0qdCVmkjAP4doE2BadTK1Z_ExCq6Eb8CT7BjyNOlOzhDS_VF3W7b9bB3CWtVtLmQnLRGGkp4tbUhhcSgaNIb-IIG-rA_v4BR4Fw9g:1rqB1Y:mvK3meMYrb2j55LzCd4V8ICAM2M", username="XMate-Tech") #replace with your session_id and username
conn = session.connect_cloud("992146957") #replace with your project id
client = scratch3.CloudRequests(conn)

# Define functions directly inside the client function
@client.request
def give(sender, receiver, amount): #called when client receives request
    # Function to send coins
    url = f'{BASE_URL}/send_coins'
    data = {'sender': sender, 'receiver': receiver, 'amount': amount}
    response = requests.post(url, json=data)
    return response.text

@client.request
def get_balance(username):
    # Function to check balance
    url = f'{BASE_URL}/balance/{username}'
    response = requests.get(url)
    return response.text

@client.request
def create_acc(username):
    # Function to create an account
    url = f'{BASE_URL}/create_account'
    data = {'username': username}
    response = requests.post(url, json=data)
    return response.text

@client.request
def get_leaderboard():
    # Function to get top richest users
    url = f'{BASE_URL}/top_richest'
    response = requests.get(url)
    if response.status_code == 200:
        richest_users = response.json()
        result = ''
        for i, user in enumerate(richest_users[:3], start=1):
            result += f"#{i}. {user['username']} - Balance: {user['balance']}\n"
        return result
    else:
        return 'Failed to retrieve top richest users'

@client.event
def on_ready():
    print("Request handler is running")

client.run()
