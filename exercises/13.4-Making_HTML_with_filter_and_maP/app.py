all_colors = [
	{"label": 'Red', "sexy": True},
	{"label": 'Pink', "sexy": False},
	{"label": 'Orange', "sexy": True},
	{"label": 'Brown', "sexy": False},
	{"label": 'Pink', "sexy": True},
	{"label": 'Violet', "sexy": True},
	{"label": 'Purple', "sexy": False},
]

#Your code go here:
def filter_colors(color):
	if color['sexy'] == True:
		return color

sexy_colors = list(filter(filter_colors, all_colors))

def generate_li(element):
	return '<li>' + element['label'] + '</li>'

html_list = list(map(generate_li, sexy_colors))
print(html_list)
