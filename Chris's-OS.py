#define MENU_OPTION_1 '1'
#define MENU_OPTION_2 '2'
#define MENU_OPTION_3 '3'
#define MENU_OPTION_4 '4'

char menuOption = MENU_OPTION_1;

void setup() {
  Serial.begin(9600);
  Serial.println("Welcome to CHRIS's OS!");
  Serial.println("Please select an option:");
  Serial.println("1. Calculator");
  Serial.println("2. File Manager");
  Serial.println("3. Text Editor");
  Serial.println("4. Exit");
}

void loop() {
  if (Serial.available()) {
    char choice = Serial.read();
    handleMenuChoice(choice);
  }
}

void handleMenuChoice(char choice) {
  switch (choice) {
    case MENU_OPTION_1:
      calculator_menu();
      break;

    case MENU_OPTION_2:
      file_manager_menu();
      break;

    case MENU_OPTION_3:
      text_editor_menu();
      break;

    case MENU_OPTION_4:
      Serial.println("Goodbye!");
      delay(500);
      while (Serial.available()) Serial.read();  // Clear input buffer
      while (true);  // Stop execution
      break;

    default:
      Serial.println("Invalid option. Please try again.");
      break;
  }
}

void calculator_menu() {
  Serial.println("\nCalculator");
  Serial.println("Please select an option:");
  Serial.println("1. Add");
  Serial.println("2. Subtract");
  Serial.println("3. Multiply");
  Serial.println("4. Divide");
  Serial.println("5. Back to Main Menu");

  while (true) {
    if (Serial.available()) {
      char choice = Serial.read();
      float operand1, operand2, result;

      switch (choice) {
        case '1':
          Serial.println("Enter the first number:");
          operand1 = readNumber();
          Serial.println("Enter the second number:");
          operand2 = readNumber();
          result = operand1 + operand2;
          Serial.print("Result: ");
          Serial.println(result);
          return;

        case '2':
          Serial.println("Enter the first number:");
          operand1 = readNumber();
          Serial.println("Enter the second number:");
          operand2 = readNumber();
          result = operand1 - operand2;
          Serial.print("Result: ");
          Serial.println(result);
          return;

        case '3':
          Serial.println("Enter the first number:");
          operand1 = readNumber();
          Serial.println("Enter the second number:");
          operand2 = readNumber();
          result = operand1 * operand2;
          Serial.print("Result: ");
          Serial.println(result);
          return;

        case '4':
          Serial.println("Enter the first number:");
          operand1 = readNumber();
          Serial.println("Enter the second number:");
          operand2 = readNumber();
          if (operand2 != 0) {
            result = operand1 / operand2;
            Serial.print("Result: ");
            Serial.println(result);
          } else {
            Serial.println("Error: Cannot divide by zero.");
          }
          return;

        case '5':
          return;

        default:
          Serial.println("Invalid option. Please try again.");
          break;
      }
    }
  }
}

void file_manager_menu() {
  // File Manager menu functionality
}

void text_editor_menu() {
  // Text Editor menu functionality
}

float readNumber() {
  String inputString = "";
  while (true) {
    if (Serial.available()) {
      char c = Serial.read();
      if (c == '\n') {
        break;
      }
      inputString += c;
    }
  }
  return inputString.toFloat();
}
