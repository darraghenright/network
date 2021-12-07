# Network

A "minimum viable project" to demonstrate how two independent Docker Compose projects can share a network, which we can use to facilitate networked communication (e.g: HTTP) between containers in each project.

To get started:

1. Run `make up` to kick off Composer for the `api` project and `service` project. This will also create a shared network called `api_network`. See the `docker-compose.yaml` file in each project for information and usage.

2. Visit http://localhost:5000/ which issues a request to the `api` container. This makes a subsequent request to the `service` container and you should see a response from `api` containing some information from `service` with status 200.

When you are finished run `make down` which will stop and remove everything. That's it!

---