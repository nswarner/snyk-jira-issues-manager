#!/usr/bin/env python3

import requests
import json
import os
import sys


class SnykSync(object):

    snyk_url = ""
    snyk_token = ""
    snyk_org = ""
    jira_url = ""
    jira_token = ""
    disclosure = False
    analysis_frequency = 70
    snyk_headers = {}
    jira_headers = {}

    def __init__(self):
        self.snyk_url = os.getenv("SNYK_URL")
        self.snyk_token = os.getenv("SNYK_TOKEN")
        self.snyk_org = os.getenv("SNYK_ORG")
        self.jira_url = os.getenv("JIRA_URL")
        self.jira_token = os.getenv("JIRA_ENCODED_TOKEN")
        self.snyk_headers = {
            "Content-Type": "application/json",
            "Authorization": self.snyk_token
        }
        self.jira_headers = {
            "Content-Type": "application/json",
            "Authorization": self.jira_token
        }

        if self.snyk_url is None:
            raise Exception("SNYK_URL environment variable is not set.")
            sys.exit(20)
        if self.snyk_token is None:
            raise Exception("SNYK_TOKEN environment variable is not set.")
            sys.exit(21)
        if self.jira_url is None:
            raise Exception("JIRA_URL environment variable is not set.")
            sys.exit(12)
        if self.jira_token is None:
            raise Exception("JIRA_ENCODED_TOKEN environment variable is not set.")
            sys.exit(13)
        print("Snyk URL: {}".format(self.snyk_url))
        if self.disclosure:
            print("Snyk Token: {}".format(self.snyk_token))

    def __del__(self):
        pass

    def snyk_get_project_vulnerabilities(self, project_key=""):
        # Snyk API URL for getting all the projects
        # url = 'https://snyk.io/api/v1/org/YOUR_ORG_ID/projects'
        url = f'{self.snyk_url}/api/v1/org/{self.snyk_org}/projects'

        # Send GET request to Snyk
        response = requests.get(
            url,
            headers=self.snyk_headers,
        )

        # Raise an exception if the request was unsuccessful
        response.raise_for_status()

        # Load response to JSON
        data = response.json()

        # Print all project names
        for project in data['projects']:
            print(project['name'])

    def snyk_cleanup_issue(self, key, tags):
        pass

    def snyk_reset_issue(self, key):
        pass

    def snyk_get_projects_data(self):
        pass

    def snyk_get_last_analysis_time(self, project_key):
        pass

    def snyk_analyze_last_analysis_time(self):
        pass


if __name__ == '__main__':
    snyker = SnykSync()
    snyker.snyk_get_project_vulnerabilities()