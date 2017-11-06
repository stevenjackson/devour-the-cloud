# Ansible Playbooks for CodeMash Precompiler on Locust Load Testing

## Getting Started

1. Install Ansible on your "control" machine (i.e., the laptop you are using)

    * [Ansible Installation](http://docs.ansible.com/ansible/latest/intro_installation.html)
    * On Mac OSX you can use Pip or Brew

1. Spin up an Ubuntu 16.04 LTS EC2 Instance for Saleor

    * Make sure Security Group In-Bound Rules Allow Port 8000 for Django Test
    * ``t2.small`` recommended

1. Spin up an Ubuntu 16.04 LTS EC2 Instance for Locust

    * Make sure Security Group In-Bound Rules Allow Port 8089 for locust
    * ``t2.small`` recommended

2. Copy the file _inventory.ini.template_ to _inventory.ini_

3. Modify _inventory.ini_ where to include the EC2 Instance Hostname

    ```ini
    saleor_instance ansible_ssh_host=<REPLACE WITH saleor EC2 DNS> ansible_user=ubuntu
    locust_instance ansible_ssh_host=<REPLACE WITH locust EC2 DNS> ansible_user=ubuntu
    ```

4. Update your _~/.ssh/config_ to include a configuration entry for your EC2 Instance, something like:

    ```
    Host ec2-52-90-215-210.compute-1.amazonaws.com
        User ubuntu
        ForwardAgent yes
        IdentityFile ~/.ssh/eecs397-spring17.pem
    ```

5. Run the _site.yml_ Ansible playbook:

    ```bash
    $ ansible-playbook site.yml
    ```

6. Log into the EC2 Instance and configure and run Django test server:

    ```bash
    cd saleor
    export ALLOWED_HOSTS="<REPLACE WITH YOUR EC2 DNS>"
    ./manage.py runserver <REPLACE WITH YOUR EC2 DNS>:8000
    ```

    point your browser at ``http://<REPLACE WITH YOUR EC2 DNS>:8000`` and you should get

    ![](doc/images/saleor_landingpage.png)

6. You can also populate the database with some default data:

    ```bash
    python manage.py populatedb
    ```

6. Enjoy!

