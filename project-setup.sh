sudo apt update
sudo apt upgrade -y
sudo apt install python3 python3-pip -y
sudo pip3 install virtualenv
python3 -m venv myenv
pip install -r requirements.txt