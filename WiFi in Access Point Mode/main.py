import network

wifi = network.WLAN(network.AP_IF)

wifi.active(True)
wifi.config(essid='Akash Wifi',authmode=network.AUTH_WPA_WPA2_PSK, password='12345678')
print(wifi.ifconfig())