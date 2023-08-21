l = ["72", "164", "160"]
n = "160"

for i in l:
	if i == n:
		print(i)
	else:
		l.remove(i)
print(l)