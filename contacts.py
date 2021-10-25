contacts = {
	"number": 4,
	"students": [
		{"name": "Harry", "email": "hpotter@hogwarts.com"},
		{"name": "Ron", "email": "rweasley@hogwarts.com"}
	]
}

for student in contacts["students"]:
    print(student["name"])