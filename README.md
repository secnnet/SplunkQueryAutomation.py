# Splunk Query Automation

This script utilizes the Splunk Python SDK to automate Splunk search queries and perform day-to-day tasks. It connects to a Splunk service, executes a search query, parses the XML output, and displays the results.

## Prerequisites

- Python 3.x
- Splunk Python SDK (`splunklib`)

## Installation

1. Clone the repository or download the script file.

2. Install the required dependencies by running the following command:

`pip install splunklib`

3. Open the script file and modify the following parameters according to your Splunk environment:

- `username`: The username to authenticate with Splunk.
- `password`: The password corresponding to the username.
- `host`: The IP address or hostname where your Splunk instance is located.
- `port`: The port number for the Splunk service (default: 8089).

4. Save the changes to the script file.

## Usage

To run the script, execute the following command:

`python SplunkQueryAutomation.py`

Make sure to replace `SplunkQueryAutomation.py` with the actual name of the script file.

The script will establish a connection to the specified Splunk instance, execute the search query, parse the XML output, and display the results in the console.

## Customization

- Search Query: Modify the `search_query` variable in the `splunk_search` method to match your desired search query. You can use Splunk's search processing language (SPL) to construct complex queries.

- Display Format: If you want to customize the output format of the parsed results, modify the `display_output` method accordingly.

## License

This project is licensed under the [MIT License](LICENSE).

Feel free to explore, modify, and use this script to automate Splunk search queries and streamline your day-to-day tasks.

For more information on using the Splunk Python SDK, refer to the official [Splunk SDK for Python documentation](https://docs.splunk.com/DocumentationStatic/PythonSDK/1.6.14/index.html).
