import pyuarm;


arm = pyuarm.get_uarm()
arm.connect()

arm.disconnect()
arm.close()
