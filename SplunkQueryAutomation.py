import sys
import xml.etree.ElementTree as ET
import splunklib.results as results
import splunklib.client as client


class QuickSearch:
    def __init__(self):
        self.service = self.check_connection()  # Establish a connection to Splunk
        self.query_results = self.splunk_search(self.service)  # Execute the search query
        self.out_raw_list = self.parse_xml(self.query_results)  # Parse the XML output
        self.display_output(self.out_raw_list)  # Display the results

    def check_connection(self):
        """
        Establish a connection to Splunk.
        """
        try:
            service = client.connect(
                username="admin",
                password="yourpassword",
                host="localhost",  # Change this to the IP address of your Splunk instance
                port=8089
            )
            return service
        except:
            print("[+] Splunk login authentication failure encountered\n\n")

    def splunk_search(self, service):
        """
        Execute the Splunk search query using the Splunk SDK.
        """
        search_query = 'search source="wineventlog:security" EventCode IN (4625,4624) | table _time Account_Name Keywords Source_Network_Address'
        kwargs_oneshot = {"earliest_time": "-7d", "latest_time": "now"}
        query_results = service.jobs.oneshot(search_query, **kwargs_oneshot)
        return query_results

    def parse_xml(self, res):
        """
        Parse the XML raw output of the Splunk query to extract specific fields.
        """
        out_raw_list = []
        tree = ET.parse(res)
        root = tree.getroot()

        for node in root.iter('field'):
            holder = ""
            children = node.getchildren()
            for c in children:
                for i in c.iter('text'):
                    if len(children) > 1:
                        holder = holder + i.text
                    else:
                        holder = i.text
            out_raw_list.append(holder)
        return out_raw_list

    def display_output(self, raw_list):
        """
        Display the parsed results.
        """
        for i in range(0, len(raw_list), 4):
            if raw_list[i] is not None or raw_list[i] != "":
                print("timestamp: {0} user: {1} status: {2} src: {3}".format(
                    raw_list[i], raw_list[i + 1], raw_list[i + 2], raw_list[i + 3]))
            else:
                continue


def main():
    qs = QuickSearch()

if __name__ == "__main__":
    main()
