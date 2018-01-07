Setting up a Shared Database
----------------------------

Many production websites will use a dedicated server for the database.  This allows us to:

1.  Scale the web tier independently
1.  Use hardware and OS optimizations to support the different responsibilities of each server type.  For instance we might want to use faster and more expensive hard drives on the database to speed up database I/O.
1.  Restrict direct access to the database.  A web developer will likely need superuser permissions to troubleshoot a web server, but may not need that same level of access at the database.  Since the database often has sensitive information we may want to limit liability.


While you can run and administer a dedicated database server on EC2, the [AWS RDS](https://aws.amazon.com/rds/) service provides a simple way to add a shared database without getting deep into the specifics of configuration and data maintenance.

With the Saleor instance only serving web requests we should see a performance improvement if our bottleneck was database CPU or memory sharing.


_Note: Launching RDS will raise your costs for the workshop.  **Remember to tear everything down!**_

## Basic Outline

1. Launch RDS with postgres [docs](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_GettingStarted.CreatingConnecting.PostgreSQL.html)
1. Create and configure security groups so the saleor web node can reach RDS [docs](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.RDSSecurityGroups.html).`5432` is the port normally used to talk to postgres.  The RDS security group will need to be configured to allow web nodes to connect.
1. Copy the current data from from the Saleor EC2 instance of postgres to RDS. [pg_dump](https://www.postgresql.org/docs/8.1/static/backup.html#BACKUP-DUMP) allows us to make a backup that the psql client can restore.
1. Point Saleor at the new RDS location.  Modify the `setting.py` file. [docs](https://docs.djangoproject.com/en/1.11/ref/settings/#databases)
1. Restart uwsgi
1. Verify saleor is running correctly with the new database
  1. Does the site come up?
  1. Are the products displayed correctly?
1. Repeat your loadtest passing the ALB DNS name(using the `--host`) switch.
1. Estabilish a new baseline.

