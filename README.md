# Confluence-Scaffolding-Bulk-Page-Creation
**Script is designed for Python 3.9**

**Step 1:** Go to your Confluence instance \
**Step 2:** Create a global template with "test" title \
**Step 3:** Copy the storage format from "test.txt" file and import it in "test" template. To import storage format you can follow https://community.atlassian.com/t5/Confluence-discussions/How-to-import-storage-format/td-p/970905  \
**Step 4:** Install the following python libraries using pip \
"pip install progressbar requests json" \
**Step 5:** Run terminal and change directory to script folder \
**Step 6:** Run the script by typing "python pagecreator.py" in the terminal \
**Step 7:** Insert Confluence URL eg. http://localhost:8090 \
**Step 8:** Insert the number of pages which you want to create \
**Step 9:** Insert the Space key which you want to create the pages on 


**Note:** 
* To add your own storage format you can update test.txt
* If you are using different Scaffolding structure, you can change json file in the ScaffoldingJsonFile.txt file

**Reading materials:**
* https://docs.servicerocket.com/scaffolding/developer-guide/scaffolding-rest-api
* https://docs.atlassian.com/atlassian-confluence/REST/6.6.0/
