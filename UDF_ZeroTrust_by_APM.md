### Subnet
+ Mgmt Subnet for Client & Server machines visit Internet
+ Data Subnet for Client, Virtual Server(s), MCP server, API server 
  
### Components
+ APM v21.x (with Forward Proxy license)
  + Create Local DB with user(s) & group(s)
  + Create Access Policy for user AuthN
  + Create Pre-request Policy
  + Create iRules

+ Client
  + Ubuntu 24.04 or above with Internet Access
  + Extra NIC on Data Subnet
  + Enable RDP for Candidates
  + Import self-sign CA cert
  + Download Cherry Studio Chatbot and setup HTTP Proxy and MCP Connector(s)

+ MCP & API server
  + Ubuntu 24.04 or above with Internet Access
    + Setup
      + ```
  + Install latest Python, FastMCP, Flask
    + ```
      pip install fastmcp
      pip install Flask
      ```
  + Setup & Run latest FastMCP
    + Setup
      + ```
        mkdir -p ZT_MCP && cd "ZT_MCP"
        ```
    + Run
      + ```
        fastmcp run server_mcp_120_205.py:mcp --transport http --port 8000 --host=0.0.0.0 --path /mcp
        ```
  + Setup & Run lastest Flask
    + Setup
      + ```
        mkdir -p ZT_Flask && cd "ZT_Flask"
        ```
    + Run
      + ```
        flask run --host=0.0.0.0
        ```


