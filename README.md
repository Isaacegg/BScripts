# BSripts
This is a repository of random security related scripts I have written over time. 

## lterangeextenderpassgen.py
This script was written to automatically generate the **DEFAULT** admin password for the Verizon 4g LTE extender (Cant find the model number, but the sku on their website is `ASK-SFE116`). I would say the most interesting part of this script is that it uses the API of the device itself *unauthenticated* to collect it's mac address! 