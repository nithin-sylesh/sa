#!/usr/bin/env python
# coding: utf-8

# In[1]:


import xml.etree.ElementTree as ET
import csv

# Load the pom.xml file
tree = ET.parse('pom.xml')
root = tree.getroot()

# Namespace for Maven's POM
ns = {'maven': 'http://maven.apache.org/POM/4.0.0'}

# Find all the dependency elements
dependencies = root.findall('.//maven:dependency', namespaces=ns)

# Create a list to store dependency information
dependency_info = []

# Iterate through dependencies and extract information
for dependency in dependencies:
    group_id = dependency.find('maven:groupId', namespaces=ns).text
    artifact_id = dependency.find('maven:artifactId', namespaces=ns).text
    version = dependency.find('maven:version', namespaces=ns).text
    dependency_info.append((f"{group_id}:{artifact_id}", version))

# Write dependency information to a CSV file
with open('dependencies.csv', 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['dependencyName', 'currentVersion'])
    csv_writer.writerows(dependency_info)

print("Dependency information written to dependencies.csv")


# In[2]:


import xml.etree.ElementTree as ET
import csv

# Load the pom.xml file
tree = ET.parse('pom.xml')
root = tree.getroot()

# Namespace for Maven's POM
ns = {'maven': 'http://maven.apache.org/POM/4.0.0'}

# Find all the dependency elements
dependencies = root.findall('.//maven:dependency', namespaces=ns)

# Create a list to store dependency information
dependency_info = []

# Iterate through dependencies and extract information
for dependency in dependencies:
    group_id = dependency.find('maven:groupId', namespaces=ns).text
    artifact_id = dependency.find('maven:artifactId', namespaces=ns).text
    version_element = dependency.find('maven:version', namespaces=ns)
    version = version_element.text if version_element is not None else "No version specified"
    dependency_info.append((f"{group_id}:{artifact_id}", version))

# Write dependency information to a CSV file
with open('dependencies.csv', 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['dependencyName', 'currentVersion'])
    csv_writer.writerows(dependency_info)

print("Dependency information written to dependencies.csv")


# In[3]:


import xml.etree.ElementTree as ET
import csv

# Load the pom.xml file
tree = ET.parse('pom.xml')
root = tree.getroot()

# Namespace for Maven's POM
ns = {'maven': 'http://maven.apache.org/POM/4.0.0'}

# Find all the dependency elements
dependencies = root.findall('.//maven:dependency', namespaces=ns)

# Create a list to store dependency information
dependency_info = []

# Iterate through dependencies and extract information
for dependency in dependencies:
    group_id = dependency.find('maven:groupId', namespaces=ns).text
    artifact_id = dependency.find('maven:artifactId', namespaces=ns).text
    version_element = dependency.find('maven:version', namespaces=ns)
    if version_element is not None:
        version = version_element.text
        dependency_info.append((f"{group_id}:{artifact_id}", version))

# Write dependency information to a CSV file
with open('dependencies.csv', 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['dependencyName', 'currentVersion'])
    csv_writer.writerows(dependency_info)

print("Dependency information written to dependencies.csv")


# In[7]:


import xml.etree.ElementTree as ET
import csv

# Load the pom.xml file
tree = ET.parse('pom.xml')
root = tree.getroot()

# Namespace for Maven's POM
ns = {'maven': 'http://maven.apache.org/POM/4.0.0'}

# Find all the dependency elements
dependencies = root.findall('.//maven:dependency', namespaces=ns)

# Create a list to store dependency information
dependency_info = []

# Iterate through dependencies and extract information
for dependency in dependencies:
    group_id = dependency.find('maven:groupId', namespaces=ns).text
    artifact_id = dependency.find('maven:artifactId', namespaces=ns).text
    version_element = dependency.find('maven:version', namespaces=ns)
    if version_element is not None:
        version = version_element.text
        # Correct version format (e.g., 4.01 to 4.0.1)
        version = '.'.join(map(str, version.split('.')))
        dependency_info.append((f"{group_id}:{artifact_id}", version))

# Write dependency information to a CSV file
with open('dependencies.csv', 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['dependencyName', 'currentVersion'])
    csv_writer.writerows(dependency_info)

print("Dependency information written to dependencies.csv")


# In[5]:


import xml.etree.ElementTree as ET
import csv

# Load the pom.xml file
tree = ET.parse('pom.xml')
root = tree.getroot()

# Namespace for Maven's POM
ns = {'maven': 'http://maven.apache.org/POM/4.0.0'}

# Find all the dependency elements
dependencies = root.findall('.//maven:dependency', namespaces=ns)

# Create a list to store dependency information
dependency_info = []

# Function to correct version format
def correct_version_format(version):
    if version.count('.') == 1:
        version_parts = version.split('.')
        if len(version_parts[1]) == 1:
            version_parts[1] = '0' + version_parts[1]
        return '.'.join(version_parts)
    return version

# Iterate through dependencies and extract information
for dependency in dependencies:
    group_id = dependency.find('maven:groupId', namespaces=ns).text
    artifact_id = dependency.find('maven:artifactId', namespaces=ns).text
    version_element = dependency.find('maven:version', namespaces=ns)
    if version_element is not None:
        version = correct_version_format(version_element.text)
        dependency_info.append((f"{group_id}:{artifact_id}", version))

# Write dependency information to a CSV file
with open('dependencies.csv', 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['dependencyName', 'currentVersion'])
    csv_writer.writerows(dependency_info)

print("Dependency information written to dependencies.csv")


# In[9]:


import csv
import requests

# Load existing dependency information from CSV
dependency_data = []
with open('dependencies.csv', 'r') as csvfile:
    csv_reader = csv.DictReader(csvfile)
    for row in csv_reader:
        dependency_data.append(row)

# Update the data with the latest versions
for dependency in dependency_data:
    group_id, artifact_id = dependency['dependencyName'].split(':')
    response = requests.get(f"https://search.maven.org/solrsearch/select?q=g:{group_id}+AND+a:{artifact_id}&core=gav&rows=1&wt=json")
    latest_version = response.json()["response"]["docs"][0]["v"]
    dependency['latestVersion'] = latest_version

# Update the CSV file with the new 'latestVersion' column
with open('dependencies.csv', 'w', newline='') as csvfile:
    fieldnames = ['dependencyName', 'currentVersion', 'latestVersion']
    csv_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    csv_writer.writeheader()
    csv_writer.writerows(dependency_data)

print("Updated dependency information with latest versions.")


# In[11]:


import csv
import xml.etree.ElementTree as ET

# Load the CSV file
dependency_versions = []
with open('dependencies.csv', 'r') as csvfile:
    csv_reader = csv.DictReader(csvfile)
    for row in csv_reader:
        dependency_versions.append(row)

# Load the pom.xml file
tree = ET.parse('pom.xml')
root = tree.getroot()

# Namespace for Maven's POM
ns = {'maven': 'http://maven.apache.org/POM/4.0.0'}

# Function to correct version format
def correct_version_format(version):
    if version.count('.') == 1:
        version_parts = version.split('.')
        if len(version_parts[1]) == 1:
            version_parts[1] = '0' + version_parts[1]
        return '.'.join(version_parts)
    return version

# Update the pom.xml with latest versions
for dependency in dependency_versions:
    dependency_name = dependency['dependencyName']
    latest_version = correct_version_format(dependency['latestVersion'])

    # Find the dependency element in the pom.xml
    for dependency_elem in root.findall('.//maven:dependency', namespaces=ns):
        group_id = dependency_elem.find('maven:groupId', namespaces=ns).text
        artifact_id = dependency_elem.find('maven:artifactId', namespaces=ns).text
        if f"{group_id}:{artifact_id}" == dependency_name:
            version_elem = dependency_elem.find('maven:version', namespaces=ns)
            if version_elem is not None:
                version_elem.text = latest_version

# Save the updated pom.xml
tree.write('pom.xml', encoding='UTF-8', xml_declaration=True)

print("pom.xml updated with latest versions.")


# In[17]:


import csv
import xml.etree.ElementTree as ET

# Load the CSV file
dependency_versions = []
with open('dependencies.csv', 'r') as csvfile:
    csv_reader = csv.DictReader(csvfile)
    for row in csv_reader:
        dependency_versions.append(row)

# Load the pom.xml file
tree = ET.parse('pom.xml')
root = tree.getroot()

# Remove the namespace prefix from the tags in the XML
for elem in root.iter():
    if '}' in elem.tag:
        elem.tag = elem.tag.split('}', 1)[1]  # Remove namespace prefix

# Function to correct version format
def correct_version_format(version):
    if version.count('.') == 1:
        version_parts = version.split('.')
        if len(version_parts[1]) == 1:
            version_parts[1] = '0' + version_parts[1]
        return '.'.join(version_parts)
    return version

# Update the pom.xml with latest versions
for dependency in dependency_versions:
    dependency_name = dependency['dependencyName']
    latest_version = correct_version_format(dependency['latestVersion'])

    # Find the dependency element in the pom.xml
    for dependency_elem in root.findall('.//dependency'):
        group_id = dependency_elem.find('groupId').text
        artifact_id = dependency_elem.find('artifactId').text
        if f"{group_id}:{artifact_id}" == dependency_name:
            version_elem = dependency_elem.find('version')
            if version_elem is not None:
                version_elem.text = latest_version

# Save the updated pom.xml
tree.write('pom.xml', encoding='UTF-8', xml_declaration=True)

print("pom.xml updated with latest versions.")


# In[18]:


get_ipython().system('pip install gitpython')


# In[19]:


import csv
import xml.etree.ElementTree as ET
import git

# Load the CSV file
dependency_versions = []
with open('dependencies.csv', 'r') as csvfile:
    csv_reader = csv.DictReader(csvfile)
    for row in csv_reader:
        dependency_versions.append(row)

# Load the pom.xml file
tree = ET.parse('pom.xml')
root = tree.getroot()

# Remove the namespace prefix from the tags in the XML
for elem in root.iter():
    if '}' in elem.tag:
        elem.tag = elem.tag.split('}', 1)[1]  # Remove namespace prefix

# Function to correct version format
def correct_version_format(version):
    if version.count('.') == 1:
        version_parts = version.split('.')
        if len(version_parts[1]) == 1:
            version_parts[1] = '0' + version_parts[1]
        return '.'.join(version_parts)
    return version

# Update the pom.xml with latest versions
for dependency in dependency_versions:
    dependency_name = dependency['dependencyName']
    latest_version = correct_version_format(dependency['latestVersion'])

    # Find the dependency element in the pom.xml
    for dependency_elem in root.findall('.//dependency'):
        group_id = dependency_elem.find('groupId').text
        artifact_id = dependency_elem.find('artifactId').text
        if f"{group_id}:{artifact_id}" == dependency_name:
            version_elem = dependency_elem.find('version')
            if version_elem is not None:
                version_elem.text = latest_version

# Save the updated pom.xml
tree.write('pom.xml', encoding='UTF-8', xml_declaration=True)

# Commit the changes using GitPython
repo = git.Repo('.')  # Initialize a Git repository instance
branch_name = 'dependency-update'
repo.git.checkout('-b', branch_name)  # Create and checkout a new branch
repo.index.add(['pom.xml'])  # Stage the pom.xml file
repo.index.commit('Update pom.xml with latest versions')  # Commit the changes
repo.remotes.origin.push(branch_name)  # Push the new branch to the remote

print("pom.xml updated, committed, and pushed to a new branch.")


# In[20]:


import csv
import xml.etree.ElementTree as ET
import subprocess

# Load the CSV file
dependency_versions = []
with open('dependencies.csv', 'r') as csvfile:
    csv_reader = csv.DictReader(csvfile)
    for row in csv_reader:
        dependency_versions.append(row)

# Load the pom.xml file
tree = ET.parse('pom.xml')
root = tree.getroot()

# Remove the namespace prefix from the tags in the XML
for elem in root.iter():
    if '}' in elem.tag:
        elem.tag = elem.tag.split('}', 1)[1]  # Remove namespace prefix

# Function to correct version format
def correct_version_format(version):
    if version.count('.') == 1:
        version_parts = version.split('.')
        if len(version_parts[1]) == 1:
            version_parts[1] = '0' + version_parts[1]
        return '.'.join(version_parts)
    return version

# Update the pom.xml with latest versions
for dependency in dependency_versions:
    dependency_name = dependency['dependencyName']
    latest_version = correct_version_format(dependency['latestVersion'])

    # Find the dependency element in the pom.xml
    for dependency_elem in root.findall('.//dependency'):
        group_id = dependency_elem.find('groupId').text
        artifact_id = dependency_elem.find('artifactId').text
        if f"{group_id}:{artifact_id}" == dependency_name:
            version_elem = dependency_elem.find('version')
            if version_elem is not None:
                version_elem.text = latest_version

# Save the updated pom.xml
tree.write('pom.xml', encoding='UTF-8', xml_declaration=True)

# Specify the full path to the Git executable
git_executable = r'D:/Git/mingw64/libexec/git-core/git.exe'  # Replace with your Git executable path

# Git operations using subprocess with the specified Git executable
subprocess.run([git_executable, 'checkout', '-b', 'dependency-update'])
subprocess.run([git_executable, 'add', 'pom.xml'])
subprocess.run([git_executable, 'commit', '-m', 'Update pom.xml with latest versions'])
subprocess.run([git_executable, 'push', 'origin', 'dependency-update'])

print("pom.xml updated, committed, and pushed to a new branch.")


# In[23]:


git_executable = r'D:/Git/mingw64/libexec/git-core/git.exe'


# In[24]:


subprocess.run([git_executable, 'commit', '-m', 'Update pom.xml with latest versions'])


# In[31]:


subprocess.run([git_executable, 'commit', '-m', "update please"])


# In[32]:


subprocess.run([git_executable, 'push', 'origin', 'dependency-update'])


# In[33]:


import requests

# Replace with your GitHub credentials
username = "nithin-sylesh"
password = "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"

# Repository details
owner = 'nithin-sylesh'
repo = "loan-application-backend"

# Pull request details
base = 'master'  # The target branch where you want to merge the changes
head = 'dependency-update'  # The source branch with your changes
title = 'Update Dependencies'
body = 'Pull Request Description'

# Create a pull request using the GitHub API
url = f'https://api.github.com/repos/{owner}/{repo}/pulls'
headers = {
    'Accept': 'application/vnd.github.v3+json'
}
data = {
    'title': title,
    'body': body,
    'head': head,
    'base': base
}

response = requests.post(url, json=data, auth=(username, password), headers=headers)

if response.status_code == 201:
    print("Pull request created successfully.")
else:
    print("Failed to create pull request.")
    print("Response:", response.content.decode('utf-8'))


# In[ ]:




