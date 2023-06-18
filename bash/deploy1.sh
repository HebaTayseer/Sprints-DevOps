#!/bin/bash 

# 1.Install dependencies and build app 
sudo apt-get update
sudo apt-get install -y curl dirmngr apt-transport-https lsb-release ca-certificates
curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
sudo apt-get install -y nodejs postgresql git
sudo apt install npm
npm install dotenv express pg pine sequelize swagger-ui-express

# 2.Set static IP
sudo tee -a /etc/network/interfaces.d/eth0.cfg <<EOF
auto eth0
iface eth0 inet static
address 172.17.0.1
netmask 255.255.255.0
gateway 192.168.1.1
EOF
ip_regex='([0-9]{1,3}\.){3}[0-9]{1,3}'
ip_address=$(ifconfig | grep -oP "$ip_regex" | head -n 1)
echo $ip_address


# 3.Create Linux user called node
# Create the user
sudo useradd -m node
# Set the user's password
sudo passwd node
# Add the user to the sudo group (optional)
sudo usermod -aG sudo node

# 4.Start Postgres
sudo systemctl start postgresql

# 5.Create the database and user
sudo -u postgres psql -c "CREATE DATABASE node"
sudo -u postgres psql -c "CREATE USER heba WITH PASSWORD 'node'"
sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE myapp TO node"

# 6.clone the repository of the app
git clone https://github.com/omarmohsen/pern-stack-example.git
cd pern-stack-example

# 7.Install and build frontend  
cd ui 
npm install 
npm run build

# 8.Build backend
cd ..
sed -i.bak "/if (environment === 'demo') {/,/};/c \\
if (environment === 'demo') { \\
  ENVIRONMENT_VARIABLES = { \\
    'process.env.HOST': JSON.stringify('$ip_address'), \\
    'process.env.USER': JSON.stringify('node'), \\
    'process.env.DB': JSON.stringify('node'), \\
    'process.env.DIALECT': JSON.stringify('postgres'), \\
    'process.env.PORT': JSON.stringify('5432'), \\
    'process.env.PG_CONNECTION_STR': JSON.stringify('postgres://node:node@localhost:5432/node') \\
  }; \\
}" api/webpack.config.js

export PG_CONNECTION_STR=postgres://node:node@localhost:5432/node

cd ui 
ENVIRONMENT=demo npm run build

# 9.Start server
cd ..
cp -r  ui api
cd api && npm start  


# 10.Handle errors
if [ $? -ne 0 ]; then
    echo "Failed to start server" 
    exit 3

