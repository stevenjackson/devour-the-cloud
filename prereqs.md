# Prerequisites for Devour the Cloud

You will need an AWS account to participate in the workshop.  We will use a couple EC2 instances to host our load test and system under test.

We estimate the cost of this workshop to be around **$1**

## To sign up for an AWS account

1. Open [https://aws.amazon.com/](https://aws.amazon.com/), and then choose **Create an AWS Account**.

2. Follow the online instructions.

3. Part of the sign-up procedure involves giving AWS credit card information.  This workshop will cost around **$1**

4. Part of the sign-up procedure involves receiving a phone call and entering a PIN using the phone keypad.

In order to access the instances in AWS you will also need to be setup for ssh.

## SSH for Mac

Mac has ssh built-in.  Make sure you can launch a terminal and type `ssh`.  

If this is your first time using AWS and ssh, you might benefit from setting up a free instance and attempting to connect.  For the workshop we will use Ubuntu 16.04, so pick that AMI type during step 1.  Ubuntu instances have a login of ubuntu.

Getting started with EC2: [http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EC2_GetStarted.html#ec2-connect-to-instance-linux](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EC2_GetStarted.html#ec2-connect-to-instance-linux)

## SSH for Windows


If you have the [Windows Subsystem for Linux](https://docs.microsoft.com/en-us/windows/wsl/install-win10) already installed, you may have ssh already configured.  Try to launch a terminal and type `ssh`.

If not, a popular ssh client for windows is PuTTY.  You can download it here:  [https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html)


If you’re unfamiliar with AWS and ssh, it’s _highly recommended_ you practice setting up a free instance.  For the workshop we will use Ubuntu 16.04, so pick that AMI type during step 1.  Ubuntu instances have a login of ubuntu.  During step 2, use the instructions for [Connecting to Your Linux Instance from Windows Using PuTTY](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/putty.html).

Getting Started with EC2: [http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EC2_GetStarted.html#ec2-connect-to-instance-linux](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EC2_GetStarted.html#ec2-connect-to-instance-linux)

