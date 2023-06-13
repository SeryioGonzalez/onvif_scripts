# Supportive ONFIV scripts for device discovery and device capability retrieval

This project has 2 main scripts intended for ONVIF device interworking. Additionally, some sample packet captures have been added to the traces folder.
For the scripts to work, you need to install wsdiscovery via pip manager.

The first script would discover all ONVIF compliance cameras in a network segment:

```
$ python3 device_discovery.py
ONVIF SCOPES FOUND:
onvif://www.onvif.org/location/country/china
onvif://www.onvif.org/name/Amcrest
onvif://www.onvif.org/hardware/IP2M-841B-EIG-IT
onvif://www.onvif.org/Profile/Streaming
onvif://www.onvif.org/type/Network_Video_Transmitter
onvif://www.onvif.org/extension/unique_identifier
----------

Number of devices detected: 1
192.168.1.203
```

The second script, would allow for obtaining the ONVIF profile of a given device in the network segment

```
$ python3 device_query.py 192.168.1.203
Onvif response code was: 200
Onvif response content was:
<?xml version="1.0" encoding="utf-8" standalone="yes" ?><s:Envelope xmlns:sc="http://www.w3.org/2003/05/soap-encoding" xmlns:s="http://www.w3.org/2003/05/soap-envelope" xmlns:tds="http://www.onvif.org/ver10/device/wsdl" xmlns:tt="http://www.onvif.org/ver10/schema"><s:Header/><s:Body><tds:GetCapabilitiesResponse><tds:Capabilities><tt:Analytics><tt:XAddr>http://192.168.1.203/onvif/analytics_service</tt:XAddr><tt:RuleSupport>true</tt:RuleSupport><tt:AnalyticsModuleSupport>true</tt:AnalyticsModuleSupport></tt:Analytics><tt:Device><tt:XAddr>http://192.168.1.203/onvif/device_service</tt:XAddr><tt:Network><tt:IPFilter>false</tt:IPFilter><tt:ZeroConfiguration>false</tt:ZeroConfiguration><tt:IPVersion6>false</tt:IPVersion6><tt:DynDNS>false</tt:DynDNS>
```