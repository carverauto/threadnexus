# Building a custom neo4j image that includes our APOC plugin

```docker
ARG NEO4J_VERSION
FROM --platform=linux/amd64 neo4j:${NEO4J_VERSION}

# copy my-plugins into the Docker image
COPY my-plugins/ /var/lib/neo4j/plugins

# install the apoc core plugin that is shipped with Neo4j
RUN cp /var/lib/neo4j/labs/apoc-* /var/lib/neo4j/plugins
```

```bash
❯ export NEO4J_PASSWORD=""
❯ export NEO4J_VERSION=5.18.0-enterprise
❯ export CONTAINER_REPOSITORY=ghcr.io/carverauto/threadr
❯ export IMAGE_NAME="my-neo4j"
❯ docker build --build-arg NEO4J_VERSION=$NEO4J_VERSION --tag ${CONTAINER_REPOSITORY}/${IMAGE_NAME}:${NEO4J_VERSION} .
```