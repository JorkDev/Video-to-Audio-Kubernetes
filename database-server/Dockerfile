FROM postgres:13

ENV POSTGRES_USER=postgres
ENV POSTGRES_PASSWORD=postgres
ENV POSTGRES_DB=conversion_db

COPY init.sql /docker-entrypoint-initdb.d/
