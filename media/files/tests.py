import csv

with open('Scheta.csv', encoding='utf-8') as f:
	reader = csv.DictReader(f)
	n = "160" # номер объекта для фильтрации
	for row in reader:
		if n in row["Комментарий"]: # проверяем есть ли желаемый объект в столбце "комментарий"
			if "." in row["Комментарий"]:
				box = row["Комментарий"].split(".")
				l = len(box)
				box = n
				row["Комментарий"] = box
				row["Всего"] = row["Всего"].replace(',', "")
				row["Всего"] = float(row["Всего"]) / l
				print(row)
			elif "," in row["Комментарий"]:
				box = row["Комментарий"].split(",")
				l = len(box)
				box = n
				row["Комментарий"] = box
				row["Всего"] = row["Всего"].replace(',', "")
				row["Всего"] = float(row["Всего"]) / l
				print(row)
			else:
				# box = row["Комментарий"].split(".")
				# l = len(box)
				# box = n
				# row["Комментарий"] = box
				# row["Всего"] = row["Всего"].replace(',', "")
				# row["Всего"] = float(row["Всего"]) / l
				print(row)
			# elif "," in row["Комментарий"]:
			# 	box = row["Комментарий"].split(",")
			# 	row["Комментарий"] = box
			# 	for i in range(len(box)):
			# 		if box[i] == n:
			# 			row["Всего"] = row["Всего"].replace(',', "")
			# 			row["Всего"] = float(row["Всего"]) / len(box)
			# 		else:
			# 			box.remove(box[i])
			# 	row["Комментарий"] = ' '.join(box)
			# 	print(row)
			# else:
			# 	box = row["Комментарий"].split(",")
			# 	row["Комментарий"] = box
			# 	for i in range(len(box)):
			# 		if box[i] == n:
			# 			row["Всего"] = row["Всего"].replace(',', "")
			# 			row["Всего"] = float(row["Всего"]) / len(box)
			# 		else:
			# 			box.remove(box[i])
			# 	row["Комментарий"] = ' '.join(box)
			# 	print(row)