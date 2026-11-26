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
  + Setup
    + ```
        sudo apt update && sudo apt upgrade -y
        sudo timedatectl set-timezone Asia/Hong_Kong
        sudo hostnamectl set-hostname Client02
        sudo vi /etc/hosts
          127.0.1.1 Client02
        sudo passwd ubuntu
          ubuntu
        wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
        sudo apt install ./google-chrome-stable_current_amd64.deb -y
      ```
  + Extra NIC on Data Subnet
  + Enable RDP for Candidates <<< ubuntu/ubuntu >>>
  + Import self-sign CA cert
  + Download Cherry Studio Chatbot and setup HTTP Proxy and MCP Connector(s)
    + Setup
    + ```
        https://cherryai.com/download
        sudo apt install ./Cherry-Studio-2.2.3-linux-x64.deb
      ```
    + Run
    + ```

      ```

+ MCP & API server
  + Ubuntu 24.04 or above with Internet Access
    + Setup
      + ```
        sudo apt update && sudo apt upgrade -y
        sudo apt install python3-pip -y
        sudo timedatectl set-timezone Asia/Hong_Kong
        sudo hostnamectl set-hostname API-MCP
        sudo vi /etc/hosts
          127.0.1.1 API-MCP
        ```
  + Install latest Python, FastMCP, Flask
    + ```
      pip install fastmcp
      sudo apt install python3-flask -y
      sudo pip3 install --break-system-packages fastmcp --ignore-installed typing_extensions
      ```
  + Setup & Run latest FastMCP
    + Setup
      + ```
        mkdir -p /home/ubuntu/ZT_MCP && cd "ZT_MCP"
        ```
    + Run
      + ```
        fastmcp run server_mcp_120_205.py:mcp --transport http --port 8000 --host=0.0.0.0 --path /mcp
        ```
  + Setup & Run lastest Flask
    + Setup
      + ```
        mkdir -p /home/ubuntu/ZT_Flask && cd "ZT_Flask"
        ```
    + Run
      + ```
        flask run --host=0.0.0.0
        ```


![alt text](image.png)
![alt text](image-1.png)
sk-d959080495384b9a8b76eba42155e71d

