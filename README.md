# WIKIPY
SEARCH WIKIPEDIA
## Wikipedia Search Application

This Python application is a graphical user interface developed using the Tkinter library. It allows users to search for information on the Wikipedia website in a user-friendly manner. Here's how the application works:

### Key Features

1. **User Interface**: The application utilizes Tkinter to create an intuitive graphical interface. The main window displays various elements such as labels, input fields, and buttons to interact with the application.

2. **Search Input Field**: Users can enter the theme or subject of their search in a dedicated input field.

3. **Wikipedia Search**: When the user clicks on the "Launch Search" button, the application retrieves the entered theme and performs a search on Wikipedia using the `wikipedia` library. It fetches the corresponding page and displays a summary of that page.

4. **Reset Functionality**: The application provides a "Reset" button that allows users to clear the content of the search input field and the search result.

5. **Quit the Application**: A "Quit Application" button is available to allow users to close the application.

### Using the Application

1. Enter the theme or subject of your search in the provided input field.

2. Click on the "Launch Search" button to perform the Wikipedia search.

3. The summary of the corresponding page will be displayed in the dedicated text area.

4. You can repeat the above steps to perform new searches by modifying the theme.

5. To clear the content of the search input field and the search result, use the "Reset" button.

6. When you are done, you can close the application by clicking on the "Quit Application" button.

### Requirements

- Python 3.x
- The `wikipedia`, `email.mime`, `multiprocessing.sharedctypes`, `tkinter`, `random` modules should be installed.

### How to Run the Application

1. Ensure that you have Python 3.x installed on your system.

2. Install the necessary modules using the following command:
   ```
   pip install wikipedia
   ```

3. Copy the Python code into a file with a `.py` extension (e.g., `wikipedia_search.py`).

4. Run the Python file using the following command:
   ```
   python wikipedia_search.py
   ```

5. The application will open in a separate window, ready to be used.

### Notes

- Make sure you have an active internet connection for the application to perform searches on Wikipedia.

- If you encounter any issues while running the application, ensure that the required modules are properly installed and your Python environment is correctly configured.

- Feel free to modify and adapt this code to suit your specific needs.

**Author:** Georges Kipre
