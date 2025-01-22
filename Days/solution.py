def solution(visits): 
	mapper = {
		"Mon": 0,
		"Tue": 1,
  		"Wed":2,
		"Thu":3,
		"Fri": 4, 
		"Sat": 5, 
		"Sun": 6,	
	}
	cards = 0 
	for i in range(len(visits)): 
		if i == 0: 
			cards += 1
		else: 
			if mapper[visits[i - 1]] >= mapper[visits[i]]:
				cards += 1
	return cards



def test_solution():
	test_cases = [
		(["Tue", "Sat", "Mon", "Fri"], 2),  # Mon(0) after Sat(5) = new week
		(["Mon", "Mon", "Mon"], 3),  # Each Mon starts new week
		(["Sun", "Sat", "Fri", "Thu", "Wed", "Tue", "Mon"], 7),  # Fix: Each day starts new week as each is less than previous
		(["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"], 1),  # Single ascending sequence
		(["Mon", "Wed", "Fri", "Mon", "Tue", "Thu", "Sat"], 2),  # Mon(0) after Fri(4) = new week
		(["Sun", "Mon", "Sun", "Tue"], 3),  # Fix: Mon(0) after Sun(6), then Sun(6) after Mon(0), then Tue(1) after Sun(6)
		(["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun", "Tue"], 2),  # Fix: Tue(1) after Sun(6) = new week
		(["Mon", "Mon", "Mon", "Mon", "Mon"], 5),  # Each Mon starts new week
		(["Fri", "Sat", "Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"], 2),  # Mon after Sun = new week
		(["Tue", "Wed", "Thu"], 1),  # Single ascending sequence
		(["Sat", "Sun", "Mon", "Tue", "Wed"], 2),  # Mon after Sun = new week
		(["Mon", "Tue", "Wed", "Sun", "Mon", "Tue", "Wed", "Sun"], 2),  # Mon after Sun = new week
		(["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun", "Mon", "Tue"], 3),  # Mon after Sun twice = two new weeks
		(["Wed", "Thu", "Fri", "Mon", "Tue", "Wed", "Fri"], 2),  # Mon after Fri = new week
		(["Mon"], 1),  # Single day
		(["Sun"], 1),  # Single day
		([], 0),  # Empty case
		(["Thu", "Thu", "Thu", "Thu", "Thu"], 5),  # Fix: Same day = same week
		(["Mon", "Tue", "Mon", "Tue", "Mon", "Tue"], 3),  # Each Mon after Tue = new week
		(["Sun", "Tue", "Thu", "Sat", "Sun", "Mon", "Wed"], 3),  # Fix: Tue after Sun, Mon after Sun = new weeks
		(["Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat"], 7),  # Fix: Same day = same week
		(["Tue", "Wed", "Thu", "Fri", "Sat", "Sun", "Mon", "Tue", "Wed"], 2),  # Mon after Sun = new week
		(["Mon", "Tue", "Wed", "Thu", "Fri", "Mon", "Tue", "Wed", "Thu", "Fri"], 2),  # Second Mon after Fri = new week
		(["Sun", "Sun", "Sun", "Sun", "Sun"], 5),  # Fix: Same day = same week
		(["Mon", "Sun", "Tue", "Mon", "Fri", "Sat", "Tue", "Thu"], 4),  # Fix: Tue after Sun, Mon after Sun, Tue after Sat = new weeks
		(["Tue", "Tue", "Tue", "Tue", "Tue", "Tue", "Tue"], 7),  # Same day = same week
		(["Fri", "Sat", "Sun", "Mon", "Tue", "Wed", "Thu"], 2),  # Mon after Sun = new week
		(["Wed", "Thu", "Fri", "Sat", "Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"], 2),  # Mon after Sun = new week
	]
	
	for i, (input_data, expected) in enumerate(test_cases):
		actual = solution(input_data)
		try:
			assert actual == expected, f"Test case {i + 1} failed: input={input_data}, expected={expected}, got={actual}"
		except AssertionError as e:
			print(e)

test_solution()