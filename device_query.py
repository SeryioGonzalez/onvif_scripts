import requests
import sys

if len(sys.argv) < 2:
    print("ERROR - Please specify ONVIF camera IP")
    print("USAGE: python3 {} ONVIF_CAMERA_IP".format(sys.argv[0]))
    sys.exit(1)

device_ip = sys.argv[1]

onvif_resource_url = "http://{}/onvif/device_service".format(device_ip)

xml_onvif_payload_no_password = """<?xml version='1.0' encoding='utf-8'?>
<soap-env:Envelope xmlns:soap-env="http://www.w3.org/2003/05/soap-envelope">
   <soap-env:Header>
   </soap-env:Header>
   <soap-env:Body>
       <ns0:GetCapabilities xmlns:ns0="http://www.onvif.org/ver10/device/wsdl">
           <ns0:Category>All</ns0:Category>
       </ns0:GetCapabilities>
   </soap-env:Body>
</soap-env:Envelope>'"""

onvif_request = requests.post(onvif_resource_url, data = xml_onvif_payload_no_password)

print("Onvif response code was: {}".format(onvif_request.status_code))
print("Onvif response content was: ")
print(onvif_request.content.decode('UTF-8'))
