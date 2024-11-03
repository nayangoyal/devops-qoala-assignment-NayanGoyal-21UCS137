from flask import Flask, request
import datetime
import socket
import netifaces as ni

app = Flask(__name__)

def get_mac_address():
    try:
        for iface in ni.interfaces():
            try:
                mac = ni.ifaddresses(iface)[ni.AF_LINK][0]['addr']
                if mac:
                    return mac
            except KeyError:
                continue
    except Exception as e:
        return f"Error retrieving MAC address: {e}"
    return "N/A"

@app.route('/')
def user_info():
    user_ip = request.remote_addr
    username = request.headers.get('Username', 'Nayan Goyal-21UCS137')
    mac_address = get_mac_address()
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return f"""
    <html>
    <body>
        <p><b>IP Address:</b> {user_ip}</p>
        <p><b>MAC Address:</b> {mac_address}</p>
        <p><b>Username:</b> {username}</p>
        <p><b>Timestamp:</b> {timestamp}</p>
        <br>
        <h3>Assignment completed successfully!</h3>
    </body>
    </html>
    """

@app.route('/health')
def health():
    return "OK", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
