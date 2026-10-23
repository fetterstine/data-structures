from random import randint


MIN_NUMBER = 1
MAX_NUMBER = 10


def ask_to_continue():
	while True:
		answer = input("Do you want to insert another number? [y/n] ").strip().lower()
		if answer in ("y", "n"):
			return answer == "y"

		print("Invalid option. Please enter y or n.")


def main():
	numbers = []

	while len(numbers) < MAX_NUMBER:
		number = randint(MIN_NUMBER, MAX_NUMBER)

		if number in numbers:
			print(f"Generated number: {number}")
			print("This number is already registered in the list.")
		else:
			numbers.append(number)

		print(f"Display List: {numbers}")
		print(f"Total Rows: {len(numbers)}")

		if len(numbers) == MAX_NUMBER:
			print("All numbers from 1 to 10 are registered.")
			break

		if not ask_to_continue():
			break

	print("Program finished.")


if __name__ == "__main__":
	main()
