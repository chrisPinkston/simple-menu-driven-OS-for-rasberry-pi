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
}

void file_manager_menu() {
  Serial.println("\nFile Manager");
  Serial.println("Please select an option:");
  Serial.println("1. List Files");
  Serial.println("2. Create File");
  Serial.println("3. Delete File");
  Serial.println("4. Back to Main Menu");
}

void text_editor_menu() {
  Serial.println("\nText Editor");
  Serial.println("Please select an option:");
  Serial.println("1. Create File");
  Serial.println("2. Edit File");
  Serial.println("3. Delete File");
  Serial.println("4. Back to Main Menu");
}
