Setting up a Load Balancer
--------------------------

Most production websites will use a load balancer to scale out resources and provide redundancy.  A load balancer allows a website to live at a single DNS location (https://www.google.com) while using multiple servers to serve requests.

[Key CDN](https://www.keycdn.com/support/load-balancing/) has a good explanation of how it works.

![Load Balancing](https://cdn.keycdn.com/support/wp-content/uploads/2015/12/load-balancing.png)


In theory, you can support any load as long as you keep adding machines to handle it.  That's not true in practice, but it's a good way to get started.

With our current saleor architecture, our web server machine also hosts the database.  So if we just replicate it, we'll end up in a strange place where the data will be inconsistent - machine one will think it has more hoodies that actually exist in inventory, because machine two has sold them.  For this reason we almost always have a single shared database between instances in a web tier.  So you might want to start with [Setting up RDS](rds.md).  But since this is a completely imaginary scenario you might just spin up a load balancer and see what happens.

_Note: More machines and the ALB is going to raise your costs for the workshop.  **Remember to tear everything down!**_

## Basic Outline

1. If you have perf changes on your existing saleor node, you'll need to figure out how to get those to your new nodes.  Creating an AMI is probably the easiest, but it will require [additional cleanup](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/deregister-ami.html#clean-up-ebs-ami) after the workshop to avoid ongoing charges
  1. To create an AMI, select your existing instance and use Actions -> Image -> Create Image.  See [here](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/creating-an-ami-ebs.html) for more details.
1. Create a second saleor EC2 instance following the instructions in [Setup AWS](../getting_started_with_aws.md).
1. Create an Application Load Balancer.  In the AWS EC2 web console scroll the left sidebar and select Load Balancers.
1. Pick a name for the ALB, then select the VPC and Availability Zones your ec2 nodes are in.
1. Create a new security group for the ALB, keeping the default of port 80 open to everyone.
1. Use a new target group and give it a name.
1. Pick your saleor nodes and add them to the target group
1. Verify saleor is running at the DNS name for the new ALB
1. Repeat your loadtest passing the ALB DNS name(using the `--host`) switch.
1. Estabilish a new baseline.

_Note: Provisioning takes some time_

Full docs [here](https://aws.amazon.com/elasticloadbalancing/getting-started/)

_Note: **Remember to tear everything down!**_
