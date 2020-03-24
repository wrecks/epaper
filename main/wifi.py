import network
import machine

def do_connect():
    ssid=['Jester','L2L','NeverGonnaGiveYouUp']
    pwrd=['1281chas','Land2Living','Asdf123456+']
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)
    wifi=sta_if.scan()
    wifi_names=[item[0].decode() for item in wifi]
    try:
        for item in ssid:
            for name in wifi_names:
                if item==name:
                    ssid_index=ssid.index(name)
        sta_if.connect(ssid[ssid_index], pwrd[ssid_index])
        while not sta_if.isconnected():
            pass
        print('Wifi connected')
    except:
        print('No matching wifi found')

