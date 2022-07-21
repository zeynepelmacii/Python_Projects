import ssl
import json
import socket
import struct
import binascii


def send_push_message(token, payload):
    # the certificate file generated from Provisioning Portal
    certfile = 'my_app_apns_certificate.pem'

    # APNS server address (use 'gateway.push.apple.com' for production server)
    apns_address = ('gateway.sandbox.push.apple.com', 2195)

    # create socket and connect to APNS server using SSL
    s = socket.socket()
    sock = ssl.wrap_socket(s, ssl_version=ssl.PROTOCOL_SSLv3, certfile=certfile)
    sock.connect(apns_address)

    # generate APNS notification packet
    token = binascii.unhexlify(token)
    fmt = "!cH32sH{0:d}s".format(len(payload))
    cmd = '\x00'
    msg = struct.pack(fmt, cmd, len(token), token, len(payload), payload)
    sock.write(msg)
    sock.close()


if __name__ == '__main__':
    payload = {"aps": {"alert": "You got your emails.", "badge": 9, "sound": "bingbong.aiff"}
               send_push_message("REGISTERED_DEVICE_PUSH_TOKEN_IN_HEX", json.dumps(payload))