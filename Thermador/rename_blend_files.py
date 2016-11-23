import os 

for f in os.listdir("."):
	if f.endswith(".blend"):
		print("Changing: ", f, "To", f.replace("_", " "))
		os.rename(f, f.replace("_", " "))