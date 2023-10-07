def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Enter user name"
        except ValueError:
            return "Give me name and phone please"
        except IndexError:
            return "Command is incomplete"

    return wrapper


class BotAssistant:
    def __init__(self):
        self.contacts = {}

    @input_error
    def add_contact(self, args):
        name, phone = args.split()
        self.contacts[name] = phone
        return f"Added {name} with phone {phone}"

    @input_error
    def change_contact(self, args):
        name, phone = args.split()
        if name in self.contacts:
            self.contacts[name] = phone
            return f"Changed phone for {name} to {phone}"
        else:
            return f"Contact {name} does not exist"

    @input_error
    def get_phone(self, name):
        if name in self.contacts:
            return f"{name}'s phone: {self.contacts[name]}"
        else:
            return f"Contact {name} does not exist"

    def show_all(self):
        result = "Contacts:\n"
        for name, phone in self.contacts.items():
            result += f"{name}: {phone}\n"
        return result

    def process_command(self, command):
        command = command.lower()
        if command == "hello":
            return "How can I help you?"
        elif command.startswith("add "):
            return self.add_contact(command[4:])
        elif command.startswith("change "):
            return self.change_contact(command[7:])
        elif command.startswith("phone "):
            return self.get_phone(command[6:])
        elif command == "show all":
            return self.show_all()
        elif command in ("good bye", "close", "exit"):
            return "Good bye!"
        else:
            return "Unknown command"

    def run(self):
        print("Bot Assistant. Type 'hello' to start. Type 'good bye' to exit.")
        while True:
            command = input("> ")
            result = self.process_command(command)
            print(result)
            if result == "Good bye!":
                break


if __name__ == "__main__":
    assistant = BotAssistant()
    assistant.run()
