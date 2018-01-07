Vertically scaling your Web Server
----------------------------------

In this particular setup of self-contained web infrastructure, you might benefit from having more horsepower on the web node.


_Note: Using larger instances can raise your AWS costs significantly.  **Remember to tear everything down!**_

During [AWS setup](../getting_started_with_aws.md) we selected `m5-large` instances to keep costs down.  This is at the low-end of what AWS offers; to see specs for all instance types go [here](https://aws.amazon.com/ec2/pricing/on-demand/).  You will probably want to watch your current saleor instance under load using `top` to see what the node is busy doing.  [Digital Ocean](https://www.digitalocean.com/community/tutorials/how-to-use-top-netstat-du-other-tools-to-monitor-server-resources#top) has a good rundown of various system monitoring tools you can use in linux.

A `m5-large` instance has 2 virtual cores and 8GB RAM.  By contrast a `m5.24xlarge` has 96 virtual cores and 384GB RAM.  In an ideal world you'd see at least a 48x improvement in your load capacity by switching to this node.  You'll also pay $4.608 per Hour (vs a dime/hour for the `m5.large`).


_Note:  Sometimes larger instance types take longer to spin up._

## Basic Outline

1. Stop your existing node.  From the EC2 console you can use Actions -> Instance Settings -> Change Instance Type to resize the instance.  More details [here](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-resize.html)
1. Repeat your loadtest passing the new DNS name for the newly provisioned server (using the `--host`) switch.
1. Estabilish a new baseline for this upgraded hardware.  See if this meets your anticipated needs.
1. Watch server resources on the new node to see if it would benefit from a different size instance type.
