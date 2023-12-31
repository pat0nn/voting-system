# VOTING SYSTEM USING BLOCKCHAIN

---

## Instructions to run the application

Clone the project,

```sh
git clone https://github.com/pat0nn/voting-system.git
```

Install the dependencies,

```sh
cd voting-system
pip install -r requirements.txt
```

Start blockchain server,
```sh
python app.py
```
*or*
```sh
python3 app.py
```

One instance of our blockchain node is now up and running at port 8000.

You can change the port by adding the "port "variable (such as 8001)
```sh
python3 app.py 8001
```
Here are a few screenshots

##### 1. Login

![image.png](./img/login.png)

##### 2. Register

![image.png](./img/register.png)

##### 3. Homepage

![image.png](./img/homepage.png)

##### 4. Votepage

![image.png](./img/vote.png)

##### 5. Result (Admin only)

![image.png](./img/result.png)

**Note**: You can change admin in [credentials.py](./credentials.py) file. Login with the admin account and go to the result page by adding the /adminPortal endpoint

##### 6. Chain

![image.png](./img/chain.png)



***

To play around by spinning off multiple custom nodes, use the `register_with/` endpoint to register a new node. You can do this by run a new port in another terminal.
Example:
```sh
python3 app.py 8001
```
Then you can use the following cURL requests to register the nodes at port 8001 with the already running 8000.
```
curl -X POST \
  http://127.0.0.1:8001/register_with \
  -H 'Content-Type: application/json' \
  -d '{"node_address": "http://127.0.0.1:8000"}'
```
*Or using Powershell :*

```sh
Invoke-RestMethod -Uri 'http://127.0.0.1:8001/register_with' -Method Post -Headers @{'Content-Type'='application/json'} -Body '{"node_address": "http://127.0.0.1:8000"}'

```
This will make the node at port 8000 aware of the nodes at port 8001 and make the newer nodes sync the chain with the node 8000, so that they are able to actively participate in the mining process post registration.

Once you do all this, you can run the application, create transactions (post vote via the web inteface), and once you mine the transactions, all the nodes in the network will update the chain. The chain of the nodes can also be inspected by inovking `/chain` endpoint using cURL.

```sh
http://localhost:8001/chain
```



Use [JSON Viewer](https://chromewebstore.google.com/detail/json-viewer/gbmdgpbipfallnflgajpaliibnhdgobh) extension  to display the chain visually
## References
[BLOCKCHAIN-VOTING-SYSTEM](https://github.com/hariharan1412/BLOCKCHAIN-VOTING-SYSTEM.git)

[E-voting-system-using-blockchain-and-python](https://github.com/ramesh-adhikari/E-voting-system-using-blockchain-and-python)
